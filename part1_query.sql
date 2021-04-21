# 1
INSERT INTO `covidvaccineapp`.`patients` (`username`, `password`, `firstname`, `lastname`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `latitude`, `longitude`, `groupNumber`) VALUES ('Bryan', 'XXX', 'Bryan', 'CC.', '123456789', '2003-02-12', '1234567890', 'bryan@gmail.com', '40 W 40th St', 'New York', 'New York', 'United States', '10018', '30', '40.73003889197802', '-74.00136170694712', '3');

# 2
INSERT INTO `covidvaccineapp`.`appointment` (`appointmentid`, `ProviderUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES ('7', 'cvs_1', '2021-05-12 10:00:00', '17', '3');
INSERT INTO `covidvaccineapp`.`providers` (`username`, `password`, `name`, `phone`, `email`, `providerType`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `latitude`, `longitude`) VALUES ('cvs_1', 'XXXX', 'cvs', '+12122266111', 'cvs1@gmail.com', 'pharmacy', '298 Mulberry St', 'New York', 'New York', 'United States', '10012', '40.72711549627752', '-73.99416331767502');
INSERT INTO `covidvaccineapp`.`offerappointment` (`appointmentid`, `PatientUsername`, `status`, `expiretime`) VALUES ('7', 'Bryan', 'finished', '2021-05-20 12:00:00');

# 3
WITH patientAvailableAppointment AS(
    select p.username, u.appointmentid, pr.name, u.appointmentDate,
		p.latitude as patientLatitude, p.longitude as patientLongitude,
        pr.latitude as providerLatitude, pr.longitude as providerLongitude,
        pr.addressLine1, pr.city, pr.state, pr.country, pr.zipcode
    from covidvaccineapp.patients p
    left join covidvaccineapp.timepreference t on t.PatientUsername = p.username
    inner join covidvaccineapp.appointment u on u.slotid = t.slotid
    inner join covidvaccineapp.providers pr on pr.username = u.ProviderUsername
)
SELECT username, name as provider, appointmentDate,
       CONCAT_WS(', ', addressLine1, city, state, country, zipcode) as address,
       (6371 * acos(
                cos( radians(providerLatitude) )
              * cos( radians( patientLatitude ) )
              * cos( radians(patientLongitude) - radians(providerLongitude) )
              + sin( radians(providerLatitude) )
              * sin( radians(patientLatitude) )
                ) ) as distanceInKM
from patientAvailableAppointment
where username = 'Joe'
order by distanceInKM;

# 4
WITH patientGroupStatus AS(
    select p.username as patientUsername, p.groupNumber, COALESCE(o.status, 'waiting') as status
    from covidvaccineapp.patients p
    left join covidvaccineapp.offerappointment o on o.PatientUsername = p.username
)
select pg.groupNumber, sum(pgs.status = 'finished') as received, sum(pgs.status = 'accepted') as scheduled,
		sum(pgs.status = 'waiting') as waiting
from covidvaccineapp.prioritygroup pg
left join patientGroupStatus pgs on pg.groupNumber = pgs.groupNumber
group by pg.groupNumber;

#5
select p.username, p.groupNumber, pg.EligibleDate
from covidvaccineapp.patients p
left join covidvaccineapp.prioritygroup pg on p.groupNumber = pg.groupNumber;

# 6
select o.PatientUsername, CONCAT_WS(' ',p.firstName, p.lastName) as name
from covidvaccineapp.offerappointment o
inner join covidvaccineapp.patients p on o.PatientUsername = p.username
group by o.PatientUsername, p.firstname
having sum(o.status = 'cancel') >= 3 or sum(o.status = 'miss') >= 2;

# 7
with providerUploadNumber as ( select u.ProviderUsername, sum(u.availableNumber) as number
from covidvaccineapp.appointment u
group by u.ProviderUsername)
select temp.ProviderUsername, providers.name, temp.number
from providerUploadNumber temp
inner join providers on temp.ProviderUsername = providers.username
where temp.number in (select max(number) from providerUploadNumber);