<?php
// proses.php: menerima data dari form-php.html
// name="nama" di HTML jadi $_POST["nama"] di PHP
$nama = $_POST["nama"] ?? "";
$jurusan = $_POST["jurusan"] ?? "";

// htmlspecialchars biar input aneh tidak merusak halaman
$nama = htmlspecialchars($nama);
$jurusan = htmlspecialchars($jurusan);

if ($nama == "") {
    echo "<h1>Eh, namanya belum diisi!</h1>";
} else {
    echo "<h1>Halo $nama!</h1>";
    echo "<p>Semangat kuliah di jurusan $jurusan ya!</p>";
}
echo '<a href="form-php.html">Kembali ke form</a>';
