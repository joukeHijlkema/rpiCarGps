-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 15, 2019 at 04:16 PM
-- Server version: 10.1.38-MariaDB-0+deb9u1
-- PHP Version: 5.6.38-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `busGps`
--

-- --------------------------------------------------------

--
-- Table structure for table `Gps`
--

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
  MODIFY `ID` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=114620;
--
-- AUTO_INCREMENT for table `Memory`
--
ALTER TABLE `Memory`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `Temp`
--
ALTER TABLE `Temp`
  MODIFY `ID` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
