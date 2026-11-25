// Kalkulator JavaScript ala Bayi Coding
let angka1 = 100;
let angka2 = 4;
let operator = "-";

function hitung(a, b, op) {
    if (op === "+") {
        return a + b;
    } else if (op === "-") {
        return a - b;
    } else if (op === "*") {
        return a * b;
    } else if (op === "/") {
        return a / b;
    }
    return "Operator tidak dikenal";
}

console.log("Hasilnya:", hitung(angka1, angka2, operator));

// Bonus: perulangan, coba semua operator sekaligus
let semuaOperator = ["+", "-", "*", "/"];
for (let i = 0; i < semuaOperator.length; i++) {
    let op = semuaOperator[i];
    console.log(angka1, op, angka2, "=", hitung(angka1, angka2, op));
}
