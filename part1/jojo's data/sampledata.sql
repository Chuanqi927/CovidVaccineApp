# provider
INSERT INTO `covidvaccineapp`.`providers` (`username`, `password`, `name`, `phone`, `email`, `providerType`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `latitude`, `longitude`) VALUES ('walgreens_1', 'XXXX', 'walgreens', '+17186432146', 'walgreen1@gmail.com', 'pharmacy', '120 Court St,', 'Brooklyn', 'New York', 'United States', '11201', '40.690250867579806', ' -73.992542317');
INSERT INTO `covidvaccineapp`.`providers` (`username`, `password`, `name`, `phone`, `email`, `providerType`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `latitude`, `longitude`) VALUES ('walgreens_2', 'XXXX', 'walgreens', '+17188553980', 'walgreen2@gmail.com', 'pharmacy', '16 Court St', 'Brooklyn', 'New York', 'United States', '11241', '40.69374349939101', '-73.9908169869943');
INSERT INTO `covidvaccineapp`.`providers` (`username`, `password`, `name`, `phone`, `email`, `providerType`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `latitude`, `longitude`) VALUES ('cvs_1', 'XXXX', 'cvs', '+12122266111', 'cvs1@gmail.com', 'pharmacy', '298 Mulberry St', 'New York', 'New York', 'United States', '10012', '40.72711549627752', '-73.99416331767502');

# patients
INSERT INTO `covidvaccineapp`.`patients` (`username`, `password`, `firstname`, `lastname`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `latitude`, `longitude`) VALUES ('Joe', 'XXX', 'Joe', 'CC.', '567891234', '2003-03-12', '1234567890', 'joe@gmail.com', '101 Liberty St Suite 1415', 'New York', 'New York', 'United States', '10006', '30', '40.7104436575887', ' -74.01201110704014');
INSERT INTO `covidvaccineapp`.`patients` (`username`, `password`, `firstname`, `lastname`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `latitude`, `longitude`) VALUES ('Bryan', 'XXX', 'Bryan', 'CC.', '123456789', '2003-02-12', '1234567890', 'bryan@gmail.com', '40 W 40th St', 'New York', 'New York', 'United States', '10018', '30', '40.73003889197802', '-74.00136170694712');
INSERT INTO `covidvaccineapp`.`patients` (`username`, `password`, `firstname`, `lastname`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `latitude`, `longitude`) VALUES ('Mike_abc', 'XXX', 'Mike', 'J.', '341341340', '2001-03-12', '1341341340', 'mike_abc@gmail.com', '420 Grand St', 'Jersey City', 'New Jersey', 'United States', '07302', '30', '40.71927415716855', '-74.05274854455092');
INSERT INTO `covidvaccineapp`.`patients` (`username`, `password`, `firstname`, `lastname`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `latitude`, `longitude`) VALUES ('Kiki', 'XXX', 'Kiki', 'Z.', '341841340', '2000-03-12', '1341341349', 'kk@gmail.com', '6 MetroTech Center', 'Brooklyn', 'New York', 'United States', '11201', '30', '40.69438254044251', '-73.98663264650904');
INSERT INTO `covidvaccineapp`.`patients` (`username`, `password`, `firstname`, `lastname`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `latitude`, `longitude`) VALUES ('Mia', 'XXX', 'Mia', 'H.', '341321340', '1999-03-12', '1341341332', 'mia@gmail.com', '2922 Broadway ', 'New York', 'New York', 'United States', '10027', '30', '40.69438254044251', '-73.98663264650904');
INSERT INTO `covidvaccineapp`.`patients` (`username`, `password`, `firstname`, `lastname`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `latitude`, `longitude`) VALUES ('Mike_noGroup', 'XXX', 'Mike', 'J.', '341341380', '2001-03-12', '1351341340', 'mike_noGroup@gmail.com', '420 Grand St', 'Jersey City', 'New Jersey', 'United States', '07302', '30', '40.71927415716855', '-74.05274854455092');

# upload appointment
INSERT INTO `covidvaccineapp`.`uploadappointment` (`appointmentid`, `ProviderUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES ('1', 'cvs_1', '2021-05-12 10:00:00', '17', '3');
INSERT INTO `covidvaccineapp`.`uploadappointment` (`appointmentid`, `ProviderUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES ('2', 'walgreens_1', '2021-05-01 9:00:00', '20', '5');
INSERT INTO `covidvaccineapp`.`uploadappointment` (`appointmentid`, `ProviderUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES ('3', 'walgreens_2', '2021-05-11 13:00:00', '23', '5');
INSERT INTO `covidvaccineapp`.`uploadappointment` (`appointmentid`, `ProviderUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES ('4', 'walgreens_1', '2021-05-11 17:00:00', '30', '8');
INSERT INTO `covidvaccineapp`.`uploadappointment` (`appointmentid`, `ProviderUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES ('5', 'walgreens_1', '2021-05-16 17:00:00', '35', '5');
INSERT INTO `covidvaccineapp`.`uploadappointment` (`appointmentid`, `ProviderUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES ('6', 'walgreens_2', '2021-05-14 11:00:00', '19', '5');

#admin
INSERT INTO `covidvaccineapp`.`Administrators` (`username`, `password`, `email`) VALUES ('admin1', 'XXXX', 'admin1@gmail.com');
INSERT INTO `covidvaccineapp`.`Administrators` (`username`, `password`, `email`) VALUES ('admin2', 'XXXX', 'admin2@gmail.com');

# priority group
INSERT INTO `covidvaccineapp`.`prioritygroup` (`groupNumber`, `EligibleDate`) VALUES ('1', '2021-02-15');
INSERT INTO `covidvaccineapp`.`prioritygroup` (`groupNumber`, `EligibleDate`) VALUES ('2', '2021-02-28');
INSERT INTO `covidvaccineapp`.`prioritygroup` (`groupNumber`, `EligibleDate`) VALUES ('3', '2021-03-15');
INSERT INTO `covidvaccineapp`.`prioritygroup` (`groupNumber`, `EligibleDate`) VALUES ('4', '2021-03-25');
INSERT INTO `covidvaccineapp`.`prioritygroup` (`groupNumber`, `EligibleDate`) VALUES ('5', '2021-04-10');
INSERT INTO `covidvaccineapp`.`prioritygroup` (`groupNumber`, `EligibleDate`) VALUES ('6', '2021-04-30');

# define priority
INSERT INTO `covidvaccineapp`.`definepriority` (`AdminUsername`, `PatientUsername`, `priorityGroupNumber`) VALUES ('admin1', 'Bryan', '3');
INSERT INTO `covidvaccineapp`.`definepriority` (`AdminUsername`, `PatientUsername`, `priorityGroupNumber`) VALUES ('admin1', 'Joe', '4');
INSERT INTO `covidvaccineapp`.`definepriority` (`AdminUsername`, `PatientUsername`, `priorityGroupNumber`) VALUES ('admin2', 'Mike_abc', '5');
INSERT INTO `covidvaccineapp`.`definepriority` (`AdminUsername`, `PatientUsername`, `priorityGroupNumber`) VALUES ('admin1', 'Kiki', '2');
INSERT INTO `covidvaccineapp`.`definepriority` (`AdminUsername`, `PatientUsername`, `priorityGroupNumber`) VALUES ('admin2', 'Mia', '1');

# time preference
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Bryan', '17');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Bryan', '20');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Bryan', '23');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Bryan', '19');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Bryan', '35');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Bryan', '30');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Joe', '17');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Joe', '20');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Joe', '19');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Mike_abc', '35');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Mike_abc', '30');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Mike_abc', '19');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Kiki', '23');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Mia', '30');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Mia', '23');
INSERT INTO `covidvaccineapp`.`timepreference` (`patientUsername`, `slotid`) VALUES ('Kiki', '35');


# offer
INSERT INTO `covidvaccineapp`.`offerappointment` (`appointmentid`, `PatientUsername`, `AdminUsername`, `status`, `expiretime`) VALUES ('1', 'Bryan', 'admin1', 'finished', '2021-05-20 12:00:00');
INSERT INTO `covidvaccineapp`.`offerappointment` (`appointmentid`, `PatientUsername`, `AdminUsername`, `status`, `expiretime`) VALUES ('2', 'Joe', 'admin2', 'miss', '2021-05-20 12:00:00');
INSERT INTO `covidvaccineapp`.`offerappointment` (`appointmentid`, `PatientUsername`, `AdminUsername`, `status`, `expiretime`) VALUES ('3', 'Kiki', 'admin2', 'declined', '2021-05-20 12:00:00');
INSERT INTO `covidvaccineapp`.`offerappointment` (`appointmentid`, `PatientUsername`, `AdminUsername`, `status`, `expiretime`) VALUES ('4', 'Mia', 'admin2', 'cancel', '2021-05-20 12:00:00');
INSERT INTO `covidvaccineapp`.`offerappointment` (`appointmentid`, `PatientUsername`, `AdminUsername`, `status`, `expiretime`) VALUES ('5', 'Mia', 'admin1', 'pending', '2021-05-20 12:00:00');
INSERT INTO `covidvaccineapp`.`offerappointment` (`appointmentid`, `PatientUsername`, `AdminUsername`, `status`, `expiretime`) VALUES ('6', 'Joe', 'admin2', 'accepted', '2021-05-20 12:00:00');



# weeklytimeslot
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('1', '1', '00:00:00', '04:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('2', '2', '00:00:00', '04:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('3', '3', '00:00:00', '04:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('4', '4', '00:00:00', '04:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('5', '5', '00:00:00', '04:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('6', '6', '00:00:00', '04:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('7', '7', '00:00:00', '04:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('8', '1', '04:00:00', '08:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('9', '2', '04:00:00', '08:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('10', '3', '04:00:00', '08:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('11', '4', '04:00:00', '08:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('12', '5', '04:00:00', '08:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('13', '6', '04:00:00', '08:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('14', '7', '04:00:00', '08:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('15', '1', '08:00:00', '12:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('16', '2', '08:00:00', '12:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('17', '3', '08:00:00', '12:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('18', '4', '08:00:00', '12:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('19', '5', '08:00:00', '12:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('20', '6', '08:00:00', '12:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('21', '7', '08:00:00', '12:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('22', '1', '12:00:00', '16:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('23', '2', '12:00:00', '16:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('24', '3', '12:00:00', '16:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('25', '4', '12:00:00', '16:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('26', '5', '12:00:00', '16:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('27', '6', '12:00:00', '16:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('28', '7', '12:00:00', '16:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('29', '1', '16:00:00', '20:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('30', '2', '16:00:00', '20:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('31', '3', '16:00:00', '20:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('32', '4', '16:00:00', '20:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('33', '5', '16:00:00', '20:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('34', '6', '16:00:00', '20:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('35', '7', '16:00:00', '20:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('36', '1', '20:00:00', '00:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('37', '2', '20:00:00', '00:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('38', '3', '20:00:00', '00:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('39', '4', '20:00:00', '00:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('40', '5', '20:00:00', '00:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('41', '6', '20:00:00', '00:00:00');
INSERT INTO `covidvaccineapp`.`weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES ('42', '7', '20:00:00', '00:00:00');
