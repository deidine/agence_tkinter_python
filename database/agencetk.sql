-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 05 avr. 2023 à 19:54
-- Version du serveur : 10.4.27-MariaDB
-- Version de PHP : 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `agencetk`
--

-- --------------------------------------------------------

--
-- Structure de la table `buss`
--

CREATE TABLE `buss` (
  `id` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `nbre_chaise` int(11) NOT NULL,
  `plaine` varchar(33) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `buss`
--

INSERT INTO `buss` (`id`, `numero`, `nbre_chaise`, `plaine`) VALUES
(1, 1, 12, ''),
(2, 2, 12, ''),
(3, 3, 12, ''),
(4, 4, 12, ''),
(6, 22, 22, ''),
(9, 52, 22, ''),
(10, 23, 22, ''),
(11, 24, 22, ''),
(12, 25, 22, ''),
(13, 72, 22, ''),
(14, 55, 22, ''),
(15, 32, 22, ''),
(16, 27, 22, ''),
(17, 29, 22, ''),
(18, 244, 22, ''),
(19, 12, 92, ''),
(20, 62, 22, ''),
(21, 33, 23, ''),
(22, 133, 15, '');

-- --------------------------------------------------------

--
-- Structure de la table `chauffeur`
--

CREATE TABLE `chauffeur` (
  `id` int(11) NOT NULL,
  `nom` varchar(22) NOT NULL,
  `prenom` varchar(22) NOT NULL,
  `telephone` varchar(11) NOT NULL,
  `salaire` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `id` int(11) NOT NULL,
  `nom` varchar(22) NOT NULL,
  `depart` varchar(22) NOT NULL,
  `numero` int(11) DEFAULT NULL,
  `telephone` int(11) NOT NULL,
  `direction` varchar(22) NOT NULL,
  `prix` int(200) DEFAULT NULL,
  `date` varchar(405) DEFAULT NULL,
  `payer` varchar(11) NOT NULL,
  `emploiyer` varchar(22) NOT NULL,
  `imprimer` varchar(22) NOT NULL,
  `bus_no` varchar(232) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`id`, `nom`, `depart`, `numero`, `telephone`, `direction`, `prix`, `date`, `payer`, `emploiyer`, `imprimer`, `bus_no`) VALUES
(1, 'sidi', 'matin', 7, 1221, 'noikchott', 5000, '2023-01-01', '✅', '0', '✔', 'ABCD'),
(2, 'w', 'matin', 10, 1, 'noikchott', 5000, '0002-01-01', '❌', '0', '✔', 'ABCD'),
(3, '11', 'matin', 13, 1, 'noikchott', 5000, '2023-01-01', '✅', '0', '✔', 'ABCD'),
(4, 'ققللل', 'matin', 11, 1, 'noikchott', 5000, '2023-01-01', '❌', '0', '✔', 'ABCD'),
(5, 'q', 'matin', 8, 1, 'noikchott', 5000, '2023-01-01', '✅', '0', '✔', 'ABCD'),
(6, 'deidien', 'matin', 5, 11, 'noikchott', 5000, '2023-01-01', '✅', '0', '✔', 'ABCD'),
(7, 'qq', 'matin', 14, 1, 'noikchott', 5000, '2023-01-01', '❌', '0', '✔', 'ABCD'),
(8, 'q', 'matin', 2, 1, 'noikchott', 5000, '2023-03-14', '❌', '0', '✔', 'ABCD'),
(9, 'sidi', 'matin', 9, 1, 'noikchott', 5000, '2023-01-01', '✅', '0', '✔', 'ABCD'),
(10, 'deidien', 'matin', 4, 212, 'noikchott', 5000, '2023-03-29', '✅', '0', '✔', 'ABCD'),
(11, 'sidi', 'matin', 7, 11, 'noikchott', 5000, '2023-03-15', '✅', '0', '✔', 'ABCD'),
(12, 'deidien', 'matin', 11, 12344, 'noikchott', 5000, '2023-03-23', '✅', '0', '✔', 'ABCD'),
(13, 'med', 'matin', 14, 1234567, 'noikchott', 5000, '2023-03-04', '✅', '0', '✔', 'ABCD'),
(14, 'سيبلاتنمحخهعتا', 'matin', 3, 111, 'noikchott', 5000, '2023-03-17', '✅', '0', '✔', 'ABCD'),
(15, 'locvoiture updated_at', 'matin', 15, 11, 'noikchott', 5000, '2023-03-31', '✅', '0', '✔', 'ABCD'),
(16, 'après etat', 'matin', 5, 11, 'atar', 4000, '2023-03-03', '✅', '0', '✔', 'sidi'),
(17, 'locvoiture updated_at', 'soir', 2, 221, 'atar', 4000, '2023-04-02', '✅', '0', '✔', '1'),
(18, 'deidine', 'matin', 1, 11, 'noikchott', 5000, '2023-04-02', '✅', 'q', '✔', '1'),
(19, 'Deidine', 'matin', 6, 444, 'atar', 4000, '2023-04-03', '✅', '0', '✔', 'sidi'),
(21, 'q', 'matin', 1, 1234, 'noikchott', 5000, '2023-04-03', '✅', 'q', '✔', '2');

-- --------------------------------------------------------

--
-- Structure de la table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `username` varchar(22) NOT NULL,
  `password` varchar(33) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `login`
--

INSERT INTO `login` (`id`, `username`, `password`) VALUES
(5, 'l;l', 'qqqqqqqqqqqqqqqq'),
(6, '122', '50'),
(8, 'nezih', 'nezih'),
(9, 'rachel', '4666'),
(10, 'rachel', '450000'),
(11, '', ''),
(13, 'q', 'q'),
(14, '', ''),
(15, 'deidine', '1234'),
(16, 'deidine', '3456');

-- --------------------------------------------------------

--
-- Structure de la table `message`
--

CREATE TABLE `message` (
  `id` int(11) NOT NULL,
  `respteur` varchar(45) DEFAULT NULL,
  `telephone` int(11) DEFAULT NULL,
  `typemessage` varchar(55) DEFAULT NULL,
  `prix` int(11) DEFAULT NULL,
  `emploiyer` varchar(22) NOT NULL,
  `date` varchar(405) DEFAULT NULL,
  `direction` varchar(200) DEFAULT NULL,
  `nombre` int(11) NOT NULL,
  `imprimer` varchar(22) NOT NULL,
  `bus_num` int(11) NOT NULL,
  `payer` varchar(33) NOT NULL,
  `depart` varchar(22) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `message`
--

INSERT INTO `message` (`id`, `respteur`, `telephone`, `typemessage`, `prix`, `emploiyer`, `date`, `direction`, `nombre`, `imprimer`, `bus_num`, `payer`, `depart`) VALUES
(2, 'deiden', 4567, 'ss', 5000, 'q', '2023-03-25', 'شنقيط ', 4, '✔', 62, '✅', '');

-- --------------------------------------------------------

--
-- Structure de la table `payer`
--

CREATE TABLE `payer` (
  `id` int(11) NOT NULL,
  `img` varchar(222) NOT NULL,
  `telephone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `payer`
--

INSERT INTO `payer` (`id`, `img`, `telephone`) VALUES
(15, 'mimg.png', 212),
(18, 'bus1.png', 222),
(20, 'b2.jpg', 444);

-- --------------------------------------------------------

--
-- Structure de la table `seats`
--

CREATE TABLE `seats` (
  `id` int(11) NOT NULL,
  `bus_no` varchar(155) NOT NULL,
  `seat_booked` varchar(255) DEFAULT '1',
  `direction` varchar(22) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `seats`
--

INSERT INTO `seats` (`id`, `bus_no`, `seat_booked`, `direction`) VALUES
(2, '1433AC07', '1', 'atar'),
(6, '3321AB08', '1', 'noidibou'),
(7, '1209AB00', '1,7', 'noikchott');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `buss`
--
ALTER TABLE `buss`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero` (`numero`);

--
-- Index pour la table `chauffeur`
--
ALTER TABLE `chauffeur`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bus_num` (`bus_num`);

--
-- Index pour la table `payer`
--
ALTER TABLE `payer`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `seats`
--
ALTER TABLE `seats`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `buss`
--
ALTER TABLE `buss`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT pour la table `chauffeur`
--
ALTER TABLE `chauffeur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `client`
--
ALTER TABLE `client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT pour la table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `message`
--
ALTER TABLE `message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `payer`
--
ALTER TABLE `payer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT pour la table `seats`
--
ALTER TABLE `seats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
