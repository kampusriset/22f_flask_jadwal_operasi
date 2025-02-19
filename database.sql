Buat database baru dengan nama "surgery_scheduling"
CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
);
CREATE TABLE surgeries (
id INT AUTO_INCREMENT PRIMARY KEY,
nama_pasien VARCHAR(255) NOT NULL,
level_urgensi ENUM('Tinggi', 'Sedang', 'Rendah') NOT NULL,
alamat TEXT NOT NULL,
tanggal_operasi DATE NOT NULL
);
