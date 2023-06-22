-- Création de la table Coor-Mic
CREATE TABLE `Coord-Mic` (
  `Num_case` INT PRIMARY KEY,
  `x` DECIMAL(4,2),
  `y` DECIMAL(4,2),
  `Dmic1BG` DECIMAL(4,2),
  `Dmic2HG` DECIMAL(4,2),
  `Dmic3HD` DECIMAL(4,2),
  `AMic1BG` DECIMAL(6,2),
  `AMic2HG` DECIMAL(6,2),
  `AMic3HD` DECIMAL(6,2)
);

CREATE TABLE `Ampli-mic` (
  `Num_case` INT PRIMARY KEY,
  `cdMic1BG` VARCHAR(8),
  `cdMic2HG` VARCHAR(8),
  `cdMic3HD` VARCHAR(8),
  FOREIGN KEY (`Num_case`) REFERENCES `Coord-Mic` (`Num_case`)
);

CREATE TABLE `Code-binaire`(
  `Amplitude` DECIMAL(6,2),
  `cd_binaire` INT
  );

INSERT INTO `Code-binaire` (`Amplitude`, `cd_binaire`) VALUES
('885,41', 0),
('0,08', 1),
('0.09', 10),
('0,10', 11),
('0.11', 100),
('0,12', 101),
('0.13', 110),
('0,14', 111),
('0.15', 1000),
('0,16', 1001),
('0.17', 1010),
('0,18', 1011),
('0.19', 1100),
('0,20', 1101),
('0,21', 1110),
('0.22', 1111),
('0,23', 10000),
('0.24', 10001),
('0,25', 10010),
('0,26', 10011),
('0.27', 10100),
('0,28', 10101),
('0.29', 10110),
('0,30', 10111),
('0,31', 11000),
('0,32', 11001),
('0.33', 11010),
('0,34', 11011),
('0.35', 11100),
('0,36', 11101),
('0,32', 11001),
('0.33', 11010),
('0,34', 11011),
('0.35', 11100),
('0,36', 11101),
('0,37', 11110),
('0,39', 11111),
('0,40', 100000),
('0.42', 100001),
('0,43', 100010),
('0.44', 100011),
('0,48', 100100),
('0,49', 100101),
('0.52', 100110),
('0,54', 100110),
('0.58', 101001),
('0,61', 101010),
('0.67', 101011),
('0,68', 101100),
('0.71', 101101),
('0,72', 101110),
('0.79', 101111),
('0,86', 110000),
('0.89', 110001),
('0,96', 110010),
('0.98', 110011),
('1;04', 110100),
('1,11', 110101),
('1,22', 110110),
('1;36', 110111),
('1,42', 111000),
('1,77', 111001),
('17,71', 111010),
('1,97', 111011),
('2,08', 111100),
('2,21', 111101),
('2,72', 111110),
('3,54', 111111),
('35,42', 1000000),
('3,94', 1000001),
('4,43', 1000010),
('7,08', 1000011),
('8.85', 1000100);


CREATE TABLE `For-ws` (
  `ID_donne` INT AUTO_INCREMENT PRIMARY KEY,
  `Num_case` INT,
  `cdMic1BG` INT,
  `cdMic2HG` INT,
  `cdMic3HD` INT,
  `date_heure` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`Num_case`) REFERENCES `Coord-Mic` (`Num_case`)
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
