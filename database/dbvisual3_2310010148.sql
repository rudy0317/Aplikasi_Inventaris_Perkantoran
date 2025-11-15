-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:1111
-- Generation Time: Nov 15, 2025 at 01:34 PM
-- Server version: 8.0.30
-- PHP Version: 8.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbvisual3_2310010148`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang_keluar`
--

CREATE TABLE `barang_keluar` (
  `id_keluar` int NOT NULL,
  `id_barang` int NOT NULL,
  `tanggal` date NOT NULL,
  `jumlah` int NOT NULL,
  `id_user` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `barang_keluar`
--

INSERT INTO `barang_keluar` (`id_keluar`, `id_barang`, `tanggal`, `jumlah`, `id_user`) VALUES
(1, 1, '2025-11-05', 7, 1),
(2, 2, '2025-11-05', 2, 1),
(3, 3, '2025-11-06', 4, 1),
(4, 5, '2025-11-06', 5, 2),
(5, 9, '2025-11-07', 1, 3),
(7, 12, '2025-11-15', 7, 2),
(8, 1, '2025-11-05', 2, 1),
(9, 1, '2025-11-05', 2, 2),
(10, 1, '2025-11-05', 4, 3);

-- --------------------------------------------------------

--
-- Table structure for table `barang_masuk`
--

CREATE TABLE `barang_masuk` (
  `id_masuk` int NOT NULL,
  `id_barang` int NOT NULL,
  `tanggal` date NOT NULL,
  `jumlah` int NOT NULL,
  `id_user` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `barang_masuk`
--

INSERT INTO `barang_masuk` (`id_masuk`, `id_barang`, `tanggal`, `jumlah`, `id_user`) VALUES
(1, 1, '2025-11-01', 3, 2),
(2, 2, '2025-11-02', 5, 1),
(3, 3, '2025-11-02', 10, 2),
(4, 6, '2025-11-03', 4, 3),
(7, 1, '2025-11-01', 3, 1),
(8, 2, '2025-11-02', 5, 1),
(9, 1, '2025-11-01', 3, 1),
(11, 31, '2025-11-15', 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `data_barang`
--

CREATE TABLE `data_barang` (
  `id_barang` int NOT NULL,
  `kode` varchar(16) NOT NULL,
  `nama` varchar(256) NOT NULL,
  `harga` int NOT NULL,
  `stok` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `data_barang`
--

INSERT INTO `data_barang` (`id_barang`, `kode`, `nama`, `harga`, `stok`) VALUES
(1, 'BRG001', 'Printer Epson L3150', 2500000, 5),
(2, 'BRG002', 'Monitor Dell 24 Inch', 1850000, 8),
(3, 'BRG003', 'Keyboard Logitech K120', 90000, 12),
(5, 'BRG005', 'Kabel LAN Cat6 20 Meter', 75000, 20),
(6, 'BRG006', 'Router TP-Link TL-WR840N', 350000, 6),
(7, 'BRG007', 'Switch Cisco 8 Port', 800000, 3),
(8, 'BRG008', 'Access Point Ruijie RG-RAP', 1200000, 2),
(9, 'BRG009', 'Laptop Lenovo ThinkPad E14', 9500000, 4),
(12, 'BRG011', 'Pensil', 3000, 50),
(16, 'BRG002', 'Buku Tulis A5 60 Lembar', 8500, 80),
(18, 'BRG004', 'Spidol Whiteboard Hitam', 7000, 40),
(19, 'BRG005', 'Kertas HVS A4 80gsm (Isi 500)', 55000, 25),
(20, 'BRG006', 'Stapler Besar Kangaro', 28000, 18),
(21, 'BRG007', 'Isian Staples No. 10', 5000, 50),
(22, 'BRG008', 'Lakban Bening 2 inch', 9000, 30),
(23, 'BRG009', 'Flashdisk 16GB Sandisk', 65000, 20),
(25, 'BRG011', 'Mouse Wireless Logitech', 120000, 10),
(26, 'BRG012', 'Keyboard Office Logitech', 160000, 8),
(27, 'BRG013', 'Lampu Meja LED', 45000, 6),
(31, 'BRG014', 'RAM DDR4', 300000, 5);

-- --------------------------------------------------------

--
-- Table structure for table `instansi`
--

CREATE TABLE `instansi` (
  `id_instansi` int NOT NULL,
  `nama_instansi` varchar(256) NOT NULL,
  `alamat` text,
  `kontak` varchar(64) DEFAULT NULL,
  `id_admin` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `instansi`
--

INSERT INTO `instansi` (`id_instansi`, `nama_instansi`, `alamat`, `kontak`, `id_admin`) VALUES
(4, 'PT Maju Jaya', 'Jl. Merdeka No. 10, Banjarmasin', '081234567890', 1),
(5, 'CV Sukses Selalu', 'Jl. Veteran No. 21, Banjarbaru', '082198765432', 2),
(6, 'UNISKA Banjarmasin', 'Jl. Adhyaksa No. 2, Banjarmasin', '0511-1234567', 3),
(7, 'PT Telkom Indonesia', 'JL. Banjarmasin', '081234512345', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id_user` bigint NOT NULL,
  `user` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `nama` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id_user`, `user`, `password`, `nama`) VALUES
(1, 'rudy', 'rudy', 'administrator'),
(2, 'gudang1', 'gudang123', 'Petugas Gudang 1'),
(3, 'gudang2', 'gudang123', 'Petugas Gudang 2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang_keluar`
--
ALTER TABLE `barang_keluar`
  ADD PRIMARY KEY (`id_keluar`),
  ADD KEY `id_barang` (`id_barang`),
  ADD KEY `id_user` (`id_user`);

--
-- Indexes for table `barang_masuk`
--
ALTER TABLE `barang_masuk`
  ADD PRIMARY KEY (`id_masuk`),
  ADD KEY `id_barang` (`id_barang`),
  ADD KEY `id_user` (`id_user`);

--
-- Indexes for table `data_barang`
--
ALTER TABLE `data_barang`
  ADD PRIMARY KEY (`id_barang`);

--
-- Indexes for table `instansi`
--
ALTER TABLE `instansi`
  ADD PRIMARY KEY (`id_instansi`),
  ADD KEY `id_admin` (`id_admin`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `id_user` (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barang_keluar`
--
ALTER TABLE `barang_keluar`
  MODIFY `id_keluar` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `barang_masuk`
--
ALTER TABLE `barang_masuk`
  MODIFY `id_masuk` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `data_barang`
--
ALTER TABLE `data_barang`
  MODIFY `id_barang` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `instansi`
--
ALTER TABLE `instansi`
  MODIFY `id_instansi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id_user` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `barang_keluar`
--
ALTER TABLE `barang_keluar`
  ADD CONSTRAINT `barang_keluar_ibfk_1` FOREIGN KEY (`id_barang`) REFERENCES `data_barang` (`id_barang`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_barang_keluar_users` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `barang_masuk`
--
ALTER TABLE `barang_masuk`
  ADD CONSTRAINT `barang_masuk_ibfk_1` FOREIGN KEY (`id_barang`) REFERENCES `data_barang` (`id_barang`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `barang_masuk_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `instansi`
--
ALTER TABLE `instansi`
  ADD CONSTRAINT `instansi_ibfk_1` FOREIGN KEY (`id_admin`) REFERENCES `users` (`id_user`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
