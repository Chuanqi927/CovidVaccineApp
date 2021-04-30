-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 20, 2021 at 07:50 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covidvaccineapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `administrators`
--

CREATE TABLE `administrators` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `administrators`
--

INSERT INTO `administrators` (`username`, `password`, `email`) VALUES
('admin1', 'XXXX', 'admin1@gmail.com'),
('admin2', 'XXXX', 'admin2@gmail.com'),
('Chuanqi', 'ChuanqiPass123', 'cx657@nyu.edu');

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `appointmentid` int(11) NOT NULL,
  `providerUsername` varchar(255) NOT NULL,
  `appointmentDate` datetime NOT NULL,
  `slotid` int(11) NOT NULL,
  `availableNumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`appointmentid`, `providerUsername`, `appointmentDate`, `slotid`, `availableNumber`) VALUES
(1, 'provider1', '2021-04-20 11:00:00', 1, 3),
(2, 'walgreens_1', '2021-05-01 09:00:00', 20, 5),
(3, 'walgreens_2', '2021-05-11 13:00:00', 23, 5),
(4, 'walgreens_1', '2021-05-11 17:00:00', 30, 8),
(5, 'walgreens_1', '2021-05-16 17:00:00', 35, 5),
(6, 'walgreens_2', '2021-05-14 11:00:00', 19, 5),
(7, 'cvs_1', '2021-05-12 10:00:00', 17, 3);

-- --------------------------------------------------------

--
-- Table structure for table `definepriority`
--

CREATE TABLE `definepriority` (
  `adminUsername` varchar(255) NOT NULL,
  `patientUsername` varchar(255) NOT NULL,
  `priorityGroupNumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `definepriority`
--

INSERT INTO `definepriority` (`adminUsername`, `patientUsername`, `priorityGroupNumber`) VALUES
('admin2', 'Mia', 1),
('Chuanqi', 'sampleP1', 1),
('admin1', 'Kiki', 2),
('admin1', 'Bryan', 3),
('admin1', 'Joe', 4),
('admin2', 'Mike_abc', 5);

-- --------------------------------------------------------

--
-- Table structure for table `offerappointment`
--

CREATE TABLE `offerappointment` (
  `appointmentid` int(11) NOT NULL,
  `adminUsername` varchar(255) NOT NULL,
  `patientUsername` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `expireTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `offerappointment`
--

INSERT INTO `offerappointment` (`appointmentid`, `adminUsername`, `patientUsername`, `status`, `expireTime`) VALUES
(1, 'Chuanqi', 'sampleP1', 'finished', '2021-04-22 00:06:04'),
(2, 'admin2', 'Joe', 'miss', '2021-05-20 12:00:00'),
(3, 'admin2', 'Kiki', 'declined', '2021-05-20 12:00:00'),
(4, 'admin2', 'Mia', 'cancel', '2021-05-20 12:00:00'),
(5, 'admin1', 'Mia', 'pending', '2021-05-20 12:00:00'),
(6, 'admin2', 'Joe', 'accepted', '2021-05-20 12:00:00'),
(7, 'admin1', 'Bryan', 'finished', '2021-05-20 12:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `SSN` int(11) NOT NULL,
  `dob` date NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `addressLine1` varchar(255) NOT NULL,
  `addressLine2` varchar(255) DEFAULT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `zipcode` varchar(255) NOT NULL,
  `maxDistancePreference` float NOT NULL,
  `longitude` decimal(11,8) NOT NULL,
  `latitude` decimal(10,8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`username`, `password`, `firstName`, `lastName`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `addressLine2`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `longitude`, `latitude`) VALUES
('Bryan', 'XXX', 'Bryan', 'CC.', 123456789, '2003-02-12', '1234567890', 'bryan@gmail.com', '40 W 40th St', NULL, 'New York', 'New York', 'United States', '10018', 30, '-74.00136171', '40.73003889'),
('Joe', 'XXX', 'Joe', 'CC.', 567891234, '2003-03-12', '1234567890', 'joe@gmail.com', '101 Liberty St Suite 1415', NULL, 'New York', 'New York', 'United States', '10006', 30, '-74.01201111', '40.71044366'),
('Kiki', 'XXX', 'Kiki', 'Z.', 341841340, '2000-03-12', '1341341349', 'kk@gmail.com', '6 MetroTech Center', NULL, 'Brooklyn', 'New York', 'United States', '11201', 30, '-73.98663265', '40.69438254'),
('Mia', 'XXX', 'Mia', 'H.', 341321340, '1999-03-12', '1341341332', 'mia@gmail.com', '2922 Broadway ', NULL, 'New York', 'New York', 'United States', '10027', 30, '-73.98663265', '40.69438254'),
('Mike_abc', 'XXX', 'Mike', 'J.', 341341340, '2001-03-12', '1341341340', 'mike_abc@gmail.com', '420 Grand St', NULL, 'Jersey City', 'New Jersey', 'United States', '07302', 30, '-74.05274854', '40.71927416'),
('Mike_noGroup', 'XXX', 'Mike', 'J.', 341341380, '2001-03-12', '1351341340', 'mike_noGroup@gmail.com', '420 Grand St', NULL, 'Jersey City', 'New Jersey', 'United States', '07302', 30, '-74.05274854', '40.71927416'),
('sampleP1', 'samplePassword1', 'p1FirstName', 'p1LastName', 1234123412, '2000-01-12', '732-111-1111', 'sampleP1@gmail.com', '151 Centre St', 'apt1314', 'Bayonne', 'NJ', 'US', '07002', 30, '40.67730000', '-74.10064000');

-- --------------------------------------------------------

--
-- Table structure for table `prioritygroup`
--

CREATE TABLE `prioritygroup` (
  `groupNumber` int(11) NOT NULL,
  `eligibleDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prioritygroup`
--

INSERT INTO `prioritygroup` (`groupNumber`, `eligibleDate`) VALUES
(1, '2021-01-01'),
(2, '2021-02-01'),
(3, '2021-03-01'),
(4, '2021-04-01'),
(5, '2021-05-01');

-- --------------------------------------------------------

--
-- Table structure for table `providers`
--

CREATE TABLE `providers` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `providerType` varchar(255) NOT NULL,
  `addressLine1` varchar(255) NOT NULL,
  `addressLine2` varchar(255) DEFAULT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `zipcode` varchar(255) NOT NULL,
  `longitude` decimal(11,8) NOT NULL,
  `latitude` decimal(10,8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `providers`
--

INSERT INTO `providers` (`username`, `password`, `name`, `phone`, `email`, `providerType`, `addressLine1`, `addressLine2`, `city`, `state`, `country`, `zipcode`, `longitude`, `latitude`) VALUES
('cvs_1', 'XXXX', 'cvs', '+12122266111', 'cvs1@gmail.com', 'pharmacy', '298 Mulberry St', NULL, 'New York', 'New York', 'United States', '10012', '-73.99416332', '40.72711550'),
('provider1', 'providerPassword1', 'CVS', '733-111-1111', 'provider1@gmail.com', 'Pharmacy', '18-40 Goldsborough Dr', '', 'Bayonne', 'NJ', 'US', '07002', '40.67209000', '-74.10548000'),
('walgreens_1', 'XXXX', 'walgreens', '+17186432146', 'walgreen1@gmail.com', 'pharmacy', '120 Court St,', NULL, 'Brooklyn', 'New York', 'United States', '11201', '-73.99254232', '40.69025087'),
('walgreens_2', 'XXXX', 'walgreens', '+17188553980', 'walgreen2@gmail.com', 'pharmacy', '16 Court St', NULL, 'Brooklyn', 'New York', 'United States', '11241', '-73.99081699', '40.69374350');

-- --------------------------------------------------------

--
-- Table structure for table `timepreference`
--

CREATE TABLE `timepreference` (
  `patientUsername` varchar(255) NOT NULL,
  `slotid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `timepreference`
--

INSERT INTO `timepreference` (`patientUsername`, `slotid`) VALUES
('Bryan', 17),
('Bryan', 19),
('Bryan', 20),
('Bryan', 23),
('Bryan', 30),
('Bryan', 35),
('Joe', 17),
('Joe', 19),
('Joe', 20),
('Kiki', 23),
('Kiki', 35),
('Mia', 23),
('Mia', 30),
('Mike_abc', 19),
('Mike_abc', 30),
('Mike_abc', 35),
('sampleP1', 1);

-- --------------------------------------------------------

--
-- Table structure for table `weeklytimeslot`
--

CREATE TABLE `weeklytimeslot` (
  `slotid` int(11) NOT NULL,
  `weekday` int(11) NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `weeklytimeslot`
--

INSERT INTO `weeklytimeslot` (`slotid`, `weekday`, `startTime`, `endTime`) VALUES
(1, 1, '00:00:00', '04:00:00'),
(2, 2, '00:00:00', '04:00:00'),
(3, 3, '00:00:00', '04:00:00'),
(4, 4, '00:00:00', '04:00:00'),
(5, 5, '00:00:00', '04:00:00'),
(6, 6, '00:00:00', '04:00:00'),
(7, 7, '00:00:00', '04:00:00'),
(8, 1, '04:00:00', '08:00:00'),
(9, 2, '04:00:00', '08:00:00'),
(10, 3, '04:00:00', '08:00:00'),
(11, 4, '04:00:00', '08:00:00'),
(12, 5, '04:00:00', '08:00:00'),
(13, 6, '04:00:00', '08:00:00'),
(14, 7, '04:00:00', '08:00:00'),
(15, 1, '08:00:00', '12:00:00'),
(16, 2, '08:00:00', '12:00:00'),
(17, 3, '08:00:00', '12:00:00'),
(18, 4, '08:00:00', '12:00:00'),
(19, 5, '08:00:00', '12:00:00'),
(20, 6, '08:00:00', '12:00:00'),
(21, 7, '08:00:00', '12:00:00'),
(22, 1, '12:00:00', '16:00:00'),
(23, 2, '12:00:00', '16:00:00'),
(24, 3, '12:00:00', '16:00:00'),
(25, 4, '12:00:00', '16:00:00'),
(26, 5, '12:00:00', '16:00:00'),
(27, 6, '12:00:00', '16:00:00'),
(28, 7, '12:00:00', '16:00:00'),
(29, 1, '16:00:00', '20:00:00'),
(30, 2, '16:00:00', '20:00:00'),
(31, 3, '16:00:00', '20:00:00'),
(32, 4, '16:00:00', '20:00:00'),
(33, 5, '16:00:00', '20:00:00'),
(34, 6, '16:00:00', '20:00:00'),
(35, 7, '16:00:00', '20:00:00'),
(36, 1, '20:00:00', '00:00:00'),
(37, 2, '20:00:00', '00:00:00'),
(38, 3, '20:00:00', '00:00:00'),
(39, 4, '20:00:00', '00:00:00'),
(40, 5, '20:00:00', '00:00:00'),
(41, 6, '20:00:00', '00:00:00'),
(42, 7, '20:00:00', '00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrators`
--
ALTER TABLE `administrators`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `administrators_username_uindex` (`username`);

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`appointmentid`),
  ADD KEY `uploadappointment_providers_username_fk` (`providerUsername`),
  ADD KEY `appointment_weeklytimeslot_slotid_fk` (`slotid`);

--
-- Indexes for table `definepriority`
--
ALTER TABLE `definepriority`
  ADD PRIMARY KEY (`adminUsername`,`patientUsername`),
  ADD KEY `definepriority_patients_username_fk` (`patientUsername`),
  ADD KEY `definepriority_prioritygroup_groupNumber_fk` (`priorityGroupNumber`);

--
-- Indexes for table `offerappointment`
--
ALTER TABLE `offerappointment`
  ADD PRIMARY KEY (`appointmentid`,`adminUsername`,`patientUsername`),
  ADD KEY `offerappointment_patients_username_fk` (`patientUsername`),
  ADD KEY `offerappointment_administrators_username_fk` (`adminUsername`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `patients_SSN_uindex` (`SSN`),
  ADD UNIQUE KEY `patients_username_uindex` (`username`);

--
-- Indexes for table `prioritygroup`
--
ALTER TABLE `prioritygroup`
  ADD PRIMARY KEY (`groupNumber`),
  ADD UNIQUE KEY `prioritygroup_groupNumber_uindex` (`groupNumber`);

--
-- Indexes for table `providers`
--
ALTER TABLE `providers`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `providers_username_uindex` (`username`);

--
-- Indexes for table `timepreference`
--
ALTER TABLE `timepreference`
  ADD PRIMARY KEY (`patientUsername`,`slotid`),
  ADD KEY `timepreference_weeklytimeslot_slotid_fk` (`slotid`);

--
-- Indexes for table `weeklytimeslot`
--
ALTER TABLE `weeklytimeslot`
  ADD PRIMARY KEY (`slotid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_weeklytimeslot_slotid_fk` FOREIGN KEY (`slotid`) REFERENCES `weeklytimeslot` (`slotid`),
  ADD CONSTRAINT `uploadappointment_providers_username_fk` FOREIGN KEY (`ProviderUsername`) REFERENCES `providers` (`username`);

--
-- Constraints for table `definepriority`
--
ALTER TABLE `definepriority`
  ADD CONSTRAINT `definepriority_administrators_username_fk` FOREIGN KEY (`AdminUsername`) REFERENCES `administrators` (`username`),
  ADD CONSTRAINT `definepriority_patients_username_fk` FOREIGN KEY (`PatientUsername`) REFERENCES `patients` (`username`),
  ADD CONSTRAINT `definepriority_prioritygroup_groupNumber_fk` FOREIGN KEY (`priorityGroupNumber`) REFERENCES `prioritygroup` (`groupNumber`);

--
-- Constraints for table `offerappointment`
--
ALTER TABLE `offerappointment`
  ADD CONSTRAINT `offerappointment_administrators_username_fk` FOREIGN KEY (`adminUsername`) REFERENCES `administrators` (`username`),
  ADD CONSTRAINT `offerappointment_patients_username_fk` FOREIGN KEY (`PatientUsername`) REFERENCES `patients` (`username`),
  ADD CONSTRAINT `offerappointment_uploadappointment_appointmentid_fk` FOREIGN KEY (`appointmentid`) REFERENCES `appointment` (`appointmentid`);

--
-- Constraints for table `timepreference`
--
ALTER TABLE `timepreference`
  ADD CONSTRAINT `timepreference_patients_username_fk` FOREIGN KEY (`patientUsername`) REFERENCES `patients` (`username`),
  ADD CONSTRAINT `timepreference_weeklytimeslot_slotid_fk` FOREIGN KEY (`slotid`) REFERENCES `weeklytimeslot` (`slotid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;