# Cara Cek Kode PHP di Localhost 🍼

Request dari Kak sunshine, makasih ya!

Localhost = komputer kita sendiri berlaku jadi "server", jadi kode PHP bisa dibuka di browser.

---

## 🪟 Windows: pakai XAMPP (paling gampang)

**Yang di-install:**
1. **XAMPP**: unduh di apachefriends.org (sudah berisi PHP + Apache + MySQL)
2. **VS Code**: unduh di code.visualstudio.com (buat nulis kode)
3. **Browser**: Chrome / Edge (sudah ada)

**Langkah:**
1. Install XAMPP, biarkan foldernya di `C:\xampp`
2. Buka **XAMPP Control Panel**
3. Klik **Start** di baris **Apache** (sampai warnanya hijau)
4. Buat folder proyek di `C:\xampp\htdocs\`, misalnya `C:\xampp\htdocs\form-php\`
5. Taruh file kamu di situ (`form-php.html`, `proses.php`)
6. Buka browser, ketik:
   ```
   localhost/form-php/form-php.html
   ```

**Kalau Apache tidak mau Start:** biasanya port 80 dipakai aplikasi lain (Skype, IIS).
Klik **Config** > `httpd.conf`, ganti `Listen 80` jadi `Listen 8080`,
lalu buka `localhost:8080/form-php/form-php.html`.

---

## 🍎 Mac / 🪟 Windows: pakai `php -S` (tanpa XAMPP)

**Yang di-install:**
- **Mac**: `brew install php` (butuh Homebrew dari brew.sh)
- **Windows**: unduh PHP dari windows.php.net, ekstrak ke `C:\php`,
  lalu tambahkan `C:\php` ke **Environment Variables > Path**

**Cek sudah terpasang:**
```
php -v
```

**Langkah:**
1. Buka terminal di folder kode kamu (di VS Code: menu **Terminal > New Terminal**)
2. Ketik:
   ```
   php -S localhost:8000
   ```
3. Buka browser:
   ```
   localhost:8000/form-php.html
   ```
4. Selesai? Tekan **Ctrl + C** di terminal untuk mematikan server

---

## ⚠️ Kesalahan yang sering terjadi

| Masalah | Penyebab | Solusi |
|---|---|---|
| Kode PHP muncul mentah di browser | File dibuka langsung (klik 2x), bukan lewat localhost | Buka lewat `localhost/...` |
| `404 Not Found` | Server jalan di folder yang salah | Jalankan `php -S` di folder yang ada file-nya |
| `php is not recognized` | PHP belum masuk Path (Windows) | Tambahkan folder PHP ke Path, buka ulang terminal |
| Form dikirim tapi data kosong | `name` di `<input>` beda dengan `$_POST["..."]` | Samakan namanya |

Semangat ngoding, Pasukan Dot! 🍼
