# 22f_flask_jadwal_operasi

Nama Aplikasi : Website Penjadwalan Operasi Berdasarkan Tingkat Urgensi

Kegunaan Aplikasi : Pengaturan penjadwalan operasi berdasarkan tingkat urgensi, yang dapat mengelola data dan jadwal operasi pasien

Flowchart alur kerja aplikasi : ![alt text](Flowchart.png)

Alur Otentikasi :
Proses login dengan verifikasi kredensial
Pendaftaran untuk pengguna baru
Fungsionalitas perubahan kata sandi

Operasi Dasbor :
Melihat operasi terjadwal
Mencari pasien
Menambahkan jadwal operasi baru
Mengedit jadwal yang ada
Menghapus jadwal operasi

Manajemen Data :
Validasi input
Operasi database
Langkah-langkah konfirmasi untuk tindakan penting

Manajemen Sesi :
Fungsionalitas login/logout
Validasi sesi untuk rute yang dilindungi

Warna yang berbeda dalam diagram alur mewakili :
Biru : Titik awal
Hijau : Dasbor utama
Kuning : Halaman autentikasi
Merah : Poin keputusan/konfirmasi

Anggota : Muhammad Ferdiharvan (2213010374) (muhammadferdi90@gmail.com) mengerjakan halaman penjadwalan

          Muh Rafly Fatchurrohman (2213010375) (muh.10375@mhs.amikomsolo.ac.id) mengerjakan halaman login, change password, register

          Honggo Negoro Seno Sri Satrio (2213010376) (honggo.10376@mhs.amikomsolo.ac.id) mengerjakan halaman login, , change password, register

Link vidio dokumentasi lihat melalui link berikut : https://youtu.be/deYlJQOE_3U

Cara Instalasi :

Persiapan Database
o Install MySQL Server
o Buat database baru dengan nama "surgery_scheduling"
o Buat dua tabel yang diperlukan :
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

Instalasi Dependencies :
• Pastikan Python sudah terinstall
• Buat virtual environment : python -m venv venv
• Aktifkan virtual environment:
o Windows : venv\Scripts\activate
o Linux/Mac : source venv/bin/activate
• Install dependencies : pip install -r requirements.txt

Konfigurasi Database :
• Buka file app.py
• Sesuaikan konfigurasi database pada variabel db_config:
db_config = {
'host': 'localhost',
'user': 'your_username',
'password': 'your_password',
'database': 'surgery_scheduling'
}

Menjalankan Aplikasi :
• Jalankan dengan perintah : python app.py
• Akses aplikasi melalui browser : http://localhost:5000

Fitur-fitur Aplikasi :

1. Manajemen Pengguna :
   o Register : Pembuatan akun baru
   o Login : Autentikasi pengguna
   o Change Password : Mengubah password
   o Logout : Keluar dari sistem

2. Manajemen Jadwal Operasi :
   o Tambah jadwal operasi baru
   o Lihat daftar jadwal operasi
   o Edit jadwal operasi
   o Hapus jadwal operasi
   o Pencarian pasien berdasarkan nama
   o Pengelompokan berdasarkan level urgensi (Tinggi, Sedang, Rendah)

3. Interface :
   o Responsive design
   o Color-coded urgency levels
   o Modal forms untuk tambah/edit data
   o Search dengan highlight hasil pencarian
   o Konfirmasi sebelum penghapusan data

Alur Kerja (Workflow) :

1. Alur Autentikasi :
   o User mengakses aplikasi → diarahkan ke halaman login
   o User baru dapat mendaftar melalui halaman register
   o Setelah login berhasil → diarahkan ke dashboard
   o Session digunakan untuk menjaga status login
   o Logout akan menghapus session

2. Alur Pengelolaan Jadwal Operasi :
   o User harus login untuk mengakses dashboard
   o Di dashboard, user dapat: Melihat daftar semua jadwal operasi, Menambah jadwal baru melalui modal form, Mengedit jadwal existing, Menghapus jadwal dengan konfirmasi, Mencari jadwal berdasarkan nama pasien

3. Alur Pencarian :
   o User memasukkan nama pasien di search box
   o Sistem akan memfilter daftar berdasarkan input
   o Hasil yang cocok akan di-highlight
   o Jika tidak ditemukan, muncul alert

4. Alur Pengelolaan Data :
   o Semua data disimpan dalam database MySQL
   o Setiap operasi CRUD memperbarui data secara real-time
   o Level urgensi ditampilkan dengan warna berbeda untuk memudahkan identifikasi
   o Validasi input diterapkan di sisi client dan server
