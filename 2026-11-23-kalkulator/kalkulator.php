<?php
// Kalkulator sederhana ala Bayi Coding
$angka1 = 100;
$angka2 = 4;
$operator = "/";

if ($operator == "+") {
    $hasil = $angka1 + $angka2;
} elseif ($operator == "-") {
    $hasil = $angka1 - $angka2;
} elseif ($operator == "*") {
    $hasil = $angka1 * $angka2;
} else {
    $hasil = $angka1 / $angka2;
}

echo "Hasilnya: " . $hasil . "\n";
