
USE covidVaccineApp;


# 1
# Create a new patient account, together with email, password, name, date of birth, etc.
INSERT INTO patients VALUES ('sampleP1','samplePassword1','p1FirstName','p1LastName',
                             1234123412,'2000-01-12','732-111-1111',
                             'sampleP1@gmail.com','151 Centre St','apt1314','Bayonne',
                             'NJ','US','07002',30.0,40.677300,-74.100640);

# 2
# Insert a new appointment offered by provider
INSERT INTO providers VALUES ('provider1','providerPassword1','CVS','733-111-1111',
                              'provider1@gmail.com','Pharmacy','18-40 Goldsborough Dr',
                              '', 'Bayonne', 'NJ','US','07002',40.672090,-74.105480);
INSERT INTO weeklytimeslot VALUES(1,1,'08:00:00','12:00:00');
INSERT INTO appointment VALUES(1,'provider1','2021-04-20 11:00:00' ,1,3);
# 3
# Write a query that, for a given patient, finds all available (not currently assigned)
# appointments that satisfy the constraints on the patient’s weekly schedule, sorted by
# increasing distance from the user’s home address.
INSERT INTO timepreference VALUES('sampleP1',1);
WITH satisfiedAppointmentAddr AS(
    SELECT a.appointmentid, p.longitude, p.latitude
    FROM appointment a LEFT JOIN providers p ON a.ProviderUsername = p.username
    WHERE a.slotid IN (
        SELECT slotid
        FROM timepreference
        WHERE patientUsername = 'sampleP1'
        )
),
     appointmentDistance AS(
         SELECT saa.appointmentid, ROUND(((
             (acos(sin((saa.latitude * pi()/180)) * sin((p.latitude * pi()/180)) +
                   cos((saa.latitude * pi()/180)) * cos((p.latitude * pi()/180)) *
                   cos(((saa.longitude- p.longitude) * pi()/180)))) * 180/pi()) * 60
                                              * 1.1515),2) AS distance
         FROM satisfiedAppointmentAddr saa, patients p
         WHERE p.username = 'sampleP1'
     )
SELECT appointmentid, distance
FROM appointmentDistance
ORDER BY distance ASC;
# 4
# For each priority group, list the number of patients that have already received the
# vaccination, the number of patients currently scheduled for an appointment, and the
# number of patients still waiting for an appointment.
INSERT INTO prioritygroup VALUES(1,'2021-01-01');
INSERT INTO prioritygroup VALUES(2,'2021-02-01');
INSERT INTO prioritygroup VALUES(3,'2021-03-01');
INSERT INTO prioritygroup VALUES(4,'2021-04-01');
INSERT INTO prioritygroup VALUES(5,'2021-05-01');

INSERT INTO administrators VALUES('Chuanqi','ChuanqiPass123','cx657@nyu.edu');

INSERT INTO definepriority VALUES('Chuanqi','sampleP1',1);

INSERT INTO offerappointment VALUES(1,'Chuanqi','sampleP1','finished',
                                    DATE_ADD(NOW(), INTERVAL 2 DAY ));

WITH allPatientStatus AS(
    SELECT p.username, IFNULL(o.status, 'waiting') AS status
    FROM patients p LEFT JOIN offerappointment o ON p.username = o.PatientUsername
)
SELECT pg.groupNumber,SUM(aps.status='finished') AS alreadyReceived,
       SUM(aps.status='accepted') AS scheduled,SUM(aps.status='waiting') AS waiting
FROM prioritygroup pg
    LEFT JOIN definepriority d ON pg.groupNumber = d.priorityGroupNumber
    LEFT JOIN allPatientStatus aps ON d.patientUsername = aps.username
GROUP BY pg.groupNumber;

# 5
# For each patient, output the name and the date when the patient becomes eligible
# for vaccination.
SELECT p.firstName, p.lastname, pg.eligibleDate
FROM patients p
    LEFT JOIN definepriority d on p.username = d.PatientUsername
    JOIN prioritygroup pg on d.priorityGroupNumber = pg.groupNumber;

# 6
# Output all patients that have cancelled at least 3 appointments, or that did not show
# up for at least two confirmed appointments that they did not cancel.
WITH patientCancelTimes AS(
    SELECT o.patientUsername, COUNT(o.status) AS cnt
    FROM offerappointment o
    WHERE o.status = 'canceled'
    GROUP BY o.patientUsername
),
     patientMissTimes AS(
         SELECT o.patientUsername, COUNT(o.status) AS cnt
        FROM offerappointment o
        WHERE o.status = 'miss'
        GROUP BY o.patientUsername
     )
SELECT pct.patientUsername
FROM patientCancelTimes pct
WHERE pct.cnt >= 3
UNION
SELECT pmt.patientUsername
FROM patientMissTimes pmt
WHERE pmt.cnt >= 2;

# 7
# Output the name of the provider that has performed the largest number of vaccinations.
WITH uploadCount AS (
    SELECT a.providerUsername, COUNT(*) AS cnt
    FROM appointment a
    GROUP BY a.providerUsername
)
SELECT p.username, p.name
FROM uploadCount uc JOIN providers p ON uc.providerUsername = p.username
WHERE uc.cnt = (SELECT MAX(cnt) FROM uploadCount);