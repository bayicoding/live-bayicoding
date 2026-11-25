// Nested loop + fungsi berparameter ala Bayi Coding
function tabelPerkalian(jumlahBaris, jumlahKolom) {
    console.log("Tabel " + jumlahBaris + " x " + jumlahKolom);

    for (let i = 1; i <= jumlahBaris; i++) {
        let baris = "";
        for (let j = 1; j <= jumlahKolom; j++) {
            baris += (i * j) + "\t";
        }
        console.log(baris);
    }
}

tabelPerkalian(5, 5);
