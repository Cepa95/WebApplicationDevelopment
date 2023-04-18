-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2023 at 02:52 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `upisni_list`
--

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session_id` int(11) NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`session_id`, `data`) VALUES
(39, '{\"user_id\": 1, \"username\": \"josip\", \"button\": \"Upisni list\", \"ds\": \"not\", \"la\": \"not\", \"fur\": \"not\", \"uup\": \"not\", \"oiws\": \"not\", \"oop\": \"not\", \"os\": \"not\", \"spa\": \"not\", \"pinm\": \"not\", \"bp\": \"not\", \"zr\": \"not\", \"puj\": \"not\", \"puc\": \"not\", \"pr\": \"not\", \"mu\": \"not\"}');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `ects` int(11) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subject_id`, `code`, `name`, `ects`, `year`) VALUES
(1, 'uup', 'uvod u programiranje', 7, 1),
(2, 'oiws', 'Osnove izrade web stranice', 6, 1),
(3, 'ds', 'Digitalni sustavi', 6, 1),
(4, 'fur', 'Fizika u racunarstvu', 5, 1),
(5, 'la', 'Linearna algerbra', 6, 1),
(6, 'os', 'Operativni sustavi', 5, 2),
(7, 'bp', 'Baze podataka', 6, 2),
(8, 'spa', 'Strukture podataka i algoritmi', 6, 2),
(9, 'oop', 'Objektno programiranje', 7, 2),
(10, 'pinm', 'Primijenjena i numericka matematika', 6, 2),
(11, 'puc', 'Programiranje u C#', 6, 3),
(12, 'puj', 'Programiranje u javi', 6, 3),
(13, 'mu', 'Mrezne usluge', 6, 3),
(14, 'zr', 'Zavrsni rad', 8, 3),
(15, 'pr', 'Prakticni rad', 12, 3);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varbinary(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `password`) VALUES
(1, 'josip', 'josip@gmail.com', 0x98cef995db82270dade46ea146e98957c617f7c2d1f9cb560306bbd75652de09a55b4548ee39c41c92ca31c4e28f6b32a42bc39ddfbf4e7d44f1c7c82aa2892d),
(2, 'ivana', 'ivana@gmail.com', 0x3c54b4fca6b614695c3db9f47834f679d9e1a5fbdcebc7929b9136372dcd81b9b0097fa9cd2bccda12802a0f9bf4c1dfa04a1eeca0ba85eb47e85c98717fcf5c),
(3, 'josipa', 'josipa@gmail.com', 0x0043262745a5fe9087429f0e553d6e985bd7b4c0ef8b9c97a0799370be2536ac92ae09e0e57a9d48c6de3d635eeac039b5439477f5b0cb7af6892c677957a7e8),
(4, 'ivica', 'ivica@gmail.com', 0xbc163aa0f44cd031624096474ce1c6d518218ed141fafa03fdb355ad376f122ed4fba23a8ecf3ce26856516691cf13b0d11cdb5a733061793943253d4db92c41),
(5, 'matko', 'matko@gmail.com', 0x68c01b13ae62d70c13817b2a6c466af326adb2fecf1224aa7cf69ae351f3bb1571b35dd666ca967131e1e6fcd6f2a067fcc1729d44abada801a0736f306fb3e9),
(12, 'nikola', 'nikola@gmail.com', 0xe0fb97251862a9403aa5e0bab441c2e0b15d3e581f2eea1a17c0e1bc1f1c2328ce5357dca57512f2ecef13e8994a9b87f199dd9a930baaad6c975f46d827b2d9),
(13, 'zvonko', 'zvonko@gmail.com', 0x4dd3521c4ea0f4946818fef636b5742e5ed5faf1351370c5d7181ece8867f69934c67676db8c9d37ee2369f0c8a60184ec9d8f9802119bbad283e4f3ed3aef02);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subject_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
