-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 20, 2021 at 06:08 AM
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
(1, 'provider1', '2021-04-20 11:00:00', 1, 3);

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
('Chuanqi', 'sampleP1', 1);

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
(1, 'Chuanqi', 'sampleP1', 'finished', '2021-04-22 00:06:04');

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
  `addressLine2` varchar(255) NOT NULL,
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
('provider1', 'providerPassword1', 'CVS', '733-111-1111', 'provider1@gmail.com', 'Pharmacy', '18-40 Goldsborough Dr', '', 'Bayonne', 'NJ', 'US', '07002', '40.67209000', '-74.10548000');

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
(1, 1, '08:00:00', '12:00:00');

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
