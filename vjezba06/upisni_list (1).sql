-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2023 at 11:55 PM
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
-- Table structure for table `upisni_list`
--

CREATE TABLE `upisni_list` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `predmet_id` int(11) NOT NULL,
  `status` enum('not','pass','enr') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `upisni_list`
--

INSERT INTO `upisni_list` (`id`, `student_id`, `predmet_id`, `status`) VALUES
(1062, 1, 4, 'pass'),
(1063, 1, 5, 'not'),
(1064, 1, 1, 'enr'),
(1065, 1, 2, 'not'),
(1066, 1, 3, 'pass'),
(1067, 1, 6, 'not'),
(1068, 1, 8, 'enr'),
(1069, 1, 7, 'enr'),
(1070, 1, 10, 'pass'),
(1071, 1, 9, 'enr'),
(1072, 1, 15, 'pass'),
(1073, 1, 13, 'enr'),
(1074, 1, 11, 'not'),
(1075, 1, 14, 'not'),
(1076, 1, 12, 'pass'),
(1077, 2, 4, 'pass'),
(1078, 2, 1, 'not'),
(1079, 2, 3, 'enr'),
(1080, 2, 2, 'not'),
(1081, 2, 5, 'not'),
(1082, 2, 9, 'pass'),
(1083, 2, 10, 'not'),
(1084, 2, 7, 'enr'),
(1085, 2, 8, 'not'),
(1086, 2, 6, 'not'),
(1087, 2, 14, 'enr'),
(1088, 2, 11, 'not'),
(1089, 2, 15, 'not'),
(1090, 2, 12, 'pass'),
(1091, 2, 13, 'enr'),
(1092, 13, 4, 'pass'),
(1093, 13, 3, 'not'),
(1094, 13, 2, 'enr'),
(1095, 13, 1, 'not'),
(1096, 13, 5, 'not'),
(1097, 13, 7, 'enr'),
(1098, 13, 6, 'not'),
(1099, 13, 10, 'not'),
(1100, 13, 9, 'pass'),
(1101, 13, 8, 'not'),
(1102, 13, 12, 'pass'),
(1103, 13, 15, 'not'),
(1104, 13, 11, 'enr'),
(1105, 13, 13, 'not'),
(1106, 13, 14, 'enr'),
(1107, 13, 10, 'not'),
(1108, 13, 9, 'pass'),
(1109, 13, 8, 'not'),
(1110, 13, 6, 'not'),
(1111, 13, 7, 'enr');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varbinary(64) NOT NULL,
  `uloga` enum('student','admin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `password`, `uloga`) VALUES
(1, 'josip', 'josip@gmail.com', 0xa0667b0dd48e03dd7b6d4f0f6c6bc887a5c6a74489b8fda94201e3bafa1b864f4a1f33cf3b4a5e94a734c044f28dd80795d330146ef48912a32e2798dbbc4658, 'admin'),
(2, 'ivana', 'ivana@gmail.com', 0x3c54b4fca6b614695c3db9f47834f679d9e1a5fbdcebc7929b9136372dcd81b9b0097fa9cd2bccda12802a0f9bf4c1dfa04a1eeca0ba85eb47e85c98717fcf5c, 'student'),
(3, 'josipa', 'josipa@gmail.com', 0x0043262745a5fe9087429f0e553d6e985bd7b4c0ef8b9c97a0799370be2536ac92ae09e0e57a9d48c6de3d635eeac039b5439477f5b0cb7af6892c677957a7e8, 'student'),
(4, 'ivica', 'ivica@gmail.com', 0xbc163aa0f44cd031624096474ce1c6d518218ed141fafa03fdb355ad376f122ed4fba23a8ecf3ce26856516691cf13b0d11cdb5a733061793943253d4db92c41, 'student'),
(5, 'matko', 'matko@gmail.com', 0x68c01b13ae62d70c13817b2a6c466af326adb2fecf1224aa7cf69ae351f3bb1571b35dd666ca967131e1e6fcd6f2a067fcc1729d44abada801a0736f306fb3e9, 'student'),
(12, 'nikola', 'nikola@gmail.com', 0xe0fb97251862a9403aa5e0bab441c2e0b15d3e581f2eea1a17c0e1bc1f1c2328ce5357dca57512f2ecef13e8994a9b87f199dd9a930baaad6c975f46d827b2d9, 'student'),
(13, 'zvonko', 'zvonko@gmail.com', 0x4dd3521c4ea0f4946818fef636b5742e5ed5faf1351370c5d7181ece8867f69934c67676db8c9d37ee2369f0c8a60184ec9d8f9802119bbad283e4f3ed3aef02, 'student'),
(14, 'tomislav', 'tomislav@gmail.com', 0x6ce3258335d0ce0cfb2f9c05dbd50046a7729d7f073b86d3ef7a4ec20d1da39e57ace020879023dcf124f8d08c64461eafd5ecaaafec968f1f4bf7369bbc0188, 'student'),
(15, 'tomo', 'tomo@gmail.com', 0x466a589032830392c54c508a9312433dff75e03eaa0170da540eb7877a199ababcd4b77ddf94aa1f4945ddcec0873b05dc735bed1875e714ac634235db1ba42d, 'student'),
(16, 'nikolina', 'nikolina@gmail.com', 0xfc283c6d2b25662ecd32f9ac0e91c2890ad9254d2bccb6da5f46f89410e3e52b311355bee5cc9427bf0bd6b2eaec29d9bb4914ec83c475cd91188cd6414a6a77, 'student');

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
-- Indexes for table `upisni_list`
--
ALTER TABLE `upisni_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Test` (`predmet_id`),
  ADD KEY `student_id` (`student_id`);

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
  MODIFY `session_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `upisni_list`
--
ALTER TABLE `upisni_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1112;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `upisni_list`
--
ALTER TABLE `upisni_list`
  ADD CONSTRAINT `Test` FOREIGN KEY (`predmet_id`) REFERENCES `subjects` (`subject_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `upisni_list_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
