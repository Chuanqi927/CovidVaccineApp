-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2021 at 05:07 AM
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

-- --------------------------------------------------------

--
-- Table structure for table `definepriority`
--

CREATE TABLE `definepriority` (
  `AdminUsername` varchar(255) NOT NULL,
  `PatientUsername` varchar(255) NOT NULL,
  `priorityGroupNumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `offerappointment`
--

CREATE TABLE `offerappointment` (
  `appointmentid` int(11) NOT NULL,
  `PatientUsername` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `expireTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `maxDistancePreference` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL,
  `latitude` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`username`, `password`, `firstName`, `lastName`, `SSN`, `dob`, `phone`, `email`, `addressLine1`, `addressLine2`, `city`, `state`, `country`, `zipcode`, `maxDistancePreference`, `longitude`, `latitude`) VALUES
('user1', '123456', '', '', 1231451, '2021-04-19', '73227777', 'xcx657@nyu.edu', 'dsadwada', '', '', '', '', '', '50', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `prioritygroup`
--

CREATE TABLE `prioritygroup` (
  `groupNumber` int(11) NOT NULL,
  `EligibleDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `longitude` varchar(255) NOT NULL,
  `latitude` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `timepreference`
--

CREATE TABLE `timepreference` (
  `patientUsername` varchar(255) NOT NULL,
  `slotid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `uploadappointment`
--

CREATE TABLE `uploadappointment` (
  `appointmentid` int(11) NOT NULL,
  `ProviderUsername` varchar(255) NOT NULL,
  `appointmentDate` datetime NOT NULL,
  `availableNumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `weeklytimeslot`
--

CREATE TABLE `weeklytimeslot` (
  `slotid` int(11) NOT NULL,
  `weekday` varchar(255) NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
-- Indexes for table `definepriority`
--
ALTER TABLE `definepriority`
  ADD PRIMARY KEY (`AdminUsername`,`PatientUsername`),
  ADD KEY `definepriority_patients_username_fk` (`PatientUsername`),
  ADD KEY `definepriority_prioritygroup_groupNumber_fk` (`priorityGroupNumber`);

--
-- Indexes for table `offerappointment`
--
ALTER TABLE `offerappointment`
  ADD PRIMARY KEY (`appointmentid`,`PatientUsername`),
  ADD KEY `offerappointment_patients_username_fk` (`PatientUsername`);

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
  ADD PRIMARY KEY (`groupNumber`);

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
-- Indexes for table `uploadappointment`
--
ALTER TABLE appointment
  ADD PRIMARY KEY (`appointmentid`),
  ADD KEY `uploadappointment_providers_username_fk` (`ProviderUsername`);

--
-- Indexes for table `weeklytimeslot`
--
ALTER TABLE `weeklytimeslot`
  ADD PRIMARY KEY (`slotid`);

--
-- Constraints for dumped tables
--

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
  ADD CONSTRAINT `offerappointment_patients_username_fk` FOREIGN KEY (`PatientUsername`) REFERENCES `patients` (`username`),
  ADD CONSTRAINT `offerappointment_uploadappointment_appointmentid_fk` FOREIGN KEY (`appointmentid`) REFERENCES appointment (`appointmentid`);

--
-- Constraints for table `timepreference`
--
ALTER TABLE `timepreference`
  ADD CONSTRAINT `timepreference_patients_username_fk` FOREIGN KEY (`patientUsername`) REFERENCES `patients` (`username`),
  ADD CONSTRAINT `timepreference_weeklytimeslot_slotid_fk` FOREIGN KEY (`slotid`) REFERENCES `weeklytimeslot` (`slotid`);

--
-- Constraints for table `uploadappointment`
--
ALTER TABLE appointment
  ADD CONSTRAINT `uploadappointment_providers_username_fk` FOREIGN KEY (`ProviderUsername`) REFERENCES `providers` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
