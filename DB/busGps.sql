-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 30, 2017 at 10:47 AM
-- Server version: 5.7.19-0ubuntu0.16.04.1
-- PHP Version: 7.0.22-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `busGps`
--
CREATE DATABASE IF NOT EXISTS `busGps` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `busGps`;

-- --------------------------------------------------------

--
-- Table structure for table `Gps`
--

DROP TABLE IF EXISTS `Gps`;
CREATE TABLE `Gps` (
  `ID` bigint(11) NOT NULL,
  `Lat` double NOT NULL,
  `Lon` double NOT NULL,
  `Time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Memory`
--

DROP TABLE IF EXISTS `Memory`;
CREATE TABLE `Memory` (
  `Id` int(11) NOT NULL,
  `What` tinytext NOT NULL,
  `Value` double NOT NULL,
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Temp`
--

DROP TABLE IF EXISTS `Temp`;
CREATE TABLE `Temp` (
  `ID` bigint(20) NOT NULL,
  `Temp` float NOT NULL,
  `Time` datetime NOT NULL,
  `tripStart` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Gps`
--
ALTER TABLE `Gps`
  ADD UNIQUE KEY `ID_2` (`ID`),
  ADD KEY `ID` (`ID`);

--
-- Indexes for table `Memory`
--
ALTER TABLE `Memory`
  ADD PRIMARY KEY (`Id`),
  ADD UNIQUE KEY `Id_2` (`Id`),
  ADD KEY `Id` (`Id`),
  ADD KEY `Id_3` (`Id`);

--
-- Indexes for table `Temp`
--
ALTER TABLE `Temp`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ID` (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Gps`
--
ALTER TABLE `Gps`
  MODIFY `ID` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35981;
--
-- AUTO_INCREMENT for table `Memory`
--
ALTER TABLE `Memory`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Temp`
--
ALTER TABLE `Temp`
  MODIFY `ID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
