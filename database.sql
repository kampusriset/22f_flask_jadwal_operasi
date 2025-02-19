-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 19 Feb 2025 pada 18.03
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `surgery_scheduling`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `surgeries`
--

CREATE TABLE `surgeries` (
  `id` int(11) NOT NULL,
  `nama_pasien` varchar(100) NOT NULL,
  `level_urgensi` enum('Tinggi','Sedang','Rendah') NOT NULL,
  `alamat` text NOT NULL,
  `tanggal_operasi` date NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `surgeries`
--

INSERT INTO `surgeries` (`id`, `nama_pasien`, `level_urgensi`, `alamat`, `tanggal_operasi`, `created_at`) VALUES
(2, 'ega', 'Tinggi', 'solo', '2025-01-02', '2025-02-17 05:47:56'),
(3, 'cindy', 'Rendah', 'sukoharjo', '2019-02-03', '2025-02-17 05:48:35'),
(4, 'topik', 'Sedang', 'jogja', '2018-03-04', '2025-02-17 05:49:04'),
(5, 'sugeng', 'Tinggi', 'semarang', '2024-12-31', '2025-02-18 14:25:56'),
(6, 'ronaldo', 'Tinggi', 'madrid', '2025-01-31', '2025-02-18 14:26:36');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'ferdi', '1234567890'),
(2, 'rafly', '1234567890'),
(3, 'eko', '123'),
(4, 'budi', '123');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `surgeries`
--
ALTER TABLE `surgeries`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `surgeries`
--
ALTER TABLE `surgeries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
