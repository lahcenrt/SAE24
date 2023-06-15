
CREATE TABLE `Ampli-mic` (
  `Num_case` INT PRIMARY KEY,
  `Mic1HG` VARCHAR(255),
  `Mic2HD` VARCHAR(255),
  `Mic3BG` VARCHAR(255)
);
CREATE TABLE `For-ws` (
  `Num_case` INT PRIMARY KEY,
  `Mic1HG` VARCHAR(255),
  `Mic2HD` VARCHAR(255),
  `Mic3BG` VARCHAR(255)
);

-- Création de la table Coor-Mic
CREATE TABLE `Coord-Mic` (
  `Num_case` INT PRIMARY KEY,
  `x` FLOAT,
  `y` FLOAT,
  `Dmic1HG` FLOAT,
  `Dmic2HD` FLOAT,
  `Dmic3BG` FLOAT,
  FOREIGN KEY (`Num_case`) REFERENCES `Ampli-mic` (`Num_case`)
);

-- Création de la table admin
CREATE TABLE `Admin` (
  `login` VARCHAR(255) PRIMARY KEY,
  `mdp` VARCHAR(255)
);
CREATE TABLE `User` (
  `login` VARCHAR(255) PRIMARY KEY,
  `mdp` VARCHAR(255)
);