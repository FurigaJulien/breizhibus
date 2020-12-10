-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 10, 2020 at 10:17 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `breizhibus`
--

-- --------------------------------------------------------

--
-- Table structure for table `arrets`
--

CREATE TABLE `arrets` (
  `id_arret` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets`
--

INSERT INTO `arrets` (`id_arret`, `nom`, `adresse`) VALUES
(1, 'Korrigan', '1 impasse du korrigan'),
(2, 'Morgana', '2 place Morgana'),
(3, 'L\'Ankou', '3 place de la morgue'),
(7, 'Ys', '4 rue de l\'ile d\'Ys'),
(8, 'Viviane', '5 avenue de Viviane'),
(9, 'Guénolé', '6 rue de Saint Guénolé'),
(10, 'Lancelot', 'Adresse'),
(11, 'Guenievre', 'Adresse'),
(12, 'Arthur', 'Adresse'),
(13, 'Burgonde', 'Adresse'),
(14, 'Karadoc', 'Adresse'),
(15, 'Perceval', 'Adresse'),
(16, 'Yvain', 'Adresse'),
(17, 'Gauvain', 'Adresse'),
(18, 'Loth', 'Adresse'),
(19, 'Arielle', 'Adresse');

-- --------------------------------------------------------

--
-- Table structure for table `arrets_lignes`
--

CREATE TABLE `arrets_lignes` (
  `id_ligne` int(11) NOT NULL,
  `id_arret` int(11) NOT NULL,
  `sens` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets_lignes`
--

INSERT INTO `arrets_lignes` (`id_ligne`, `id_arret`, `sens`) VALUES
(3, 1, 0),
(3, 2, 1),
(3, 3, 2),
(3, 7, 4),
(4, 8, 0),
(4, 9, 1),
(4, 10, 3),
(4, 11, 2),
(1, 11, 1),
(1, 12, 0),
(1, 13, 2),
(1, 14, 3),
(2, 15, 0),
(2, 16, 1),
(2, 17, 2),
(2, 18, 3),
(2, 19, 4),
(3, 11, 3),
(2, 12, 5);

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `id_bus` int(11) NOT NULL,
  `numero` varchar(4) NOT NULL,
  `immatriculation` varchar(7) NOT NULL,
  `nombre_place` int(11) NOT NULL,
  `id_ligne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`id_bus`, `numero`, `immatriculation`, `nombre_place`, `id_ligne`) VALUES
(1, 'BB01', 'CA123EL', 20, 1),
(3, 'BB03', 'JE123UX', 20, 3),
(4, 'BB04', 'RE123PA', 30, 1),
(12, 'BB06', 'BZ356EZ', 55, 3),
(21, 'BB07', 'AA000AA', 15, 3);

-- --------------------------------------------------------

--
-- Table structure for table `lignes`
--

CREATE TABLE `lignes` (
  `id_ligne` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lignes`
--

INSERT INTO `lignes` (`id_ligne`, `nom`) VALUES
(1, 'Rouge'),
(2, 'Vert'),
(3, 'Bleu'),
(4, 'Noir');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arrets`
--
ALTER TABLE `arrets`
  ADD PRIMARY KEY (`id_arret`);

--
-- Indexes for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD KEY `id_arret` (`id_arret`),
  ADD KEY `id_ligne` (`id_ligne`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`id_bus`),
  ADD KEY `id_ligne` (`id_ligne`);

--
-- Indexes for table `lignes`
--
ALTER TABLE `lignes`
  ADD PRIMARY KEY (`id_ligne`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arrets`
--
ALTER TABLE `arrets`
  MODIFY `id_arret` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `bus`
--
ALTER TABLE `bus`
  MODIFY `id_bus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `lignes`
--
ALTER TABLE `lignes`
  MODIFY `id_ligne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD CONSTRAINT `arrets_lignes_ibfk_1` FOREIGN KEY (`id_arret`) REFERENCES `arrets` (`id_arret`),
  ADD CONSTRAINT `arrets_lignes_ibfk_2` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`);

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
