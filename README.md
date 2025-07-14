# 🎤 Proyek Pengenalan Suara Sederhana Anda 📝

Selamat datang di proyek pengenalan suara sederhana! Aplikasi ini memungkinkan Anda mengubah ucapan dari mikrofon menjadi teks secara *real-time* menggunakan kecanggihan Google Web Speech API. Ucapkan selamat tinggal pada keyboard dan sambut era kontrol suara yang mudah!

---

## ✨ Fitur Unggulan

* **Pilihan Mikrofon Otomatis:** Tak perlu pusing mencari-cari. Aplikasi akan menampilkan semua mikrofon yang terhubung dan Anda bisa memilih yang paling pas.
* **Adaptasi Kebisingan Cerdas:** Lingkungan Anda bising? Tidak masalah! Aplikasi ini akan menyesuaikan diri dengan kebisingan latar belakang untuk memastikan pengenalan suara tetap akurat.
* **Ditenagai Google Web Speech API:** Dapatkan akurasi pengenalan suara yang superior berkat teknologi canggih dari Google. Cukup bicara, dan biarkan Google yang melakukan sisanya!
* **Siap Bahasa Indonesia:** Kode sudah diatur untuk memahami Bahasa Indonesia (`id-ID`). Mau beralih ke Inggris (`en-US`) atau bahasa lain? Mudah sekali!

---

## 🚀 Persiapan Cepat

Sebelum kita mulai, pastikan Anda memiliki ini:

* **Sistem Operasi:** Windows, macOS, atau Linux.
* **Python:** Versi 3.x terinstal.
* **Koneksi Internet:** Ini penting! Google Web Speech API butuh internet yang stabil untuk bekerja.
* **Mikrofon:** Tentu saja, siapkan mikrofon yang berfungsi dengan baik.
* **Git:** Terinstal di sistem Anda (untuk mengunduh proyek).

---

## ⬇️ Mengunduh Proyek (Git Clone)

Untuk mendapatkan salinan lokal dari repositori ini, ikuti langkah-langkah berikut:

1.  **Buka Terminal atau Command Prompt.**
2.  **Pindah ke direktori tempat Anda ingin menyimpan proyek.** Contoh:
    ```bash
    cd Documents/GitHub
    ```
3.  **Lakukan `git clone`** dengan URL repositori Anda. Ganti `[URL_REPOSITORI_ANDA]` dengan URL sebenarnya dari repositori GitHub Anda (misalnya `https://github.com/namauser/nama-repo.git`).
    ```bash
    git clone [URL_REPOSITORI_ANDA]
    ```
4.  **Masuk ke direktori proyek yang baru di-clone:**
    ```bash
    cd nama-folder-proyek-yang-di-clone # Sesuaikan dengan nama folder repositori Anda
    ```
    (Biasanya nama folder akan sama dengan nama repositori.)

---

## 🛠️ Instalasi (Anti Pusing)

Ikuti langkah-langkah mudah ini untuk menyiapkan proyek Anda:

1.  **Buat Lingkungan Virtual (Sangat Disarankan!):**
    Ini seperti "ruang kerja" khusus agar proyek Anda rapi dan tidak bentrok dengan proyek Python lain.

    ```bash
    python -m venv .venv
    ```

2.  **Masuk ke Lingkungan Virtual Anda:**
    Ini penting agar semua instalasi pustaka masuk ke "ruang kerja" khusus tadi.

    * **Untuk Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **Untuk macOS / Linux:**
        ```bash
        source ./.venv/bin/activate
        ```

3.  **Instal Pustaka Ajaib Kita:**
    Kita butuh `SpeechRecognition` (otak utamanya), `PyAudio` (untuk ngobrol sama mikrofon), dan `requests` (untuk cek internet).

    ```bash
    pip install SpeechRecognition PyAudio requests
    ```

    ---

    **🚨 PENTING: Masalah Instalasi PyAudio? Ini Solusinya! 🚨**

    `PyAudio` kadang rewel, terutama di Windows. Jangan panik!

    * **Untuk Windows:**
        Jika `pip install PyAudio` gagal, Anda mungkin perlu mengunduh **file `.whl` (wheel file)** yang sudah dikompilasi. Kunjungi [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio). Cari versi `PyAudio` yang sesuai dengan **versi Python dan arsitektur sistem Anda** (misalnya, `PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl` untuk Python 3.10 64-bit). Setelah diunduh, instal dengan perintah:
        ```bash
        pip install path\to\your\PyAudio‑*.whl
        ```
        (Ganti `path\to\your\` dengan lokasi file yang Anda unduh).

    * **Untuk Debian/Ubuntu Linux:**
        Anda mungkin perlu menginstal beberapa dependensi sistem terlebih dahulu:
        ```bash
        sudo apt-get install portaudio19-dev python3-pyaudio
        ```

    ---

---

## 🏃‍♀️ Cara Menjalankan Aplikasi

Siap untuk mulai berbicara dengan komputer Anda?

1.  **Pastikan Kode Siap:**
    Pastikan semua kode Python Anda tersimpan dalam satu file bernama `main.py` di dalam folder proyek Anda.

2.  **Buka Terminal / Command Prompt:**
    Navigasikan ke direktori tempat `main.py` berada.

    ```bash
    cd D:\Voice Asistent\SpeechRecogniton # Ini adalah contoh, sesuaikan dengan lokasi clone Anda
    ```

3.  **Aktifkan Lingkungan Virtual (Jika Belum Aktif):**
    Ini adalah langkah penting sebelum menjalankan skrip.

    * **Untuk Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **Untuk macOS / Linux:**
        ```bash
        source ./.venv/bin/activate
        ```

4.  **Jalankan Skrip Python Anda:**

    ```bash
    python main.py
    ```

5.  **Ikuti Arahan di Layar:**
    * Aplikasi akan menampilkan daftar mikrofon yang terdeteksi. Pilih nomor indeks yang paling sesuai dengan mikrofon yang ingin Anda gunakan.
    * Setelah itu, tunggu pesan "--- Siap Mendengarkan! ---".
    * Ketika Anda melihat "Silakan ucapkan sesuatu...", **langsung bicara dengan jelas**!

---

## 🚑 Pemecahan Masalah Umum (Jangan Panik!)

Mengalami kendala? Cek bagian ini:

* **`Timeout`**:
    * **Apa artinya:** Aplikasi tidak mendengar suara Anda dalam batas waktu yang ditentukan (7 detik).
    * **Solusi:**
        * **Bicara Cepat:** Mulai berbicara segera setelah "Siap Mendengarkan!".
        * **Cek Mikrofon:** Pastikan mikrofon Anda aktif dan volume inputnya sudah maksimal di pengaturan suara sistem Anda.

* **`AssertionError` atau `AttributeError: 'NoneType' object has no attribute 'close'`**:
    * **Apa artinya:** Python kesulitan membuka atau mengakses mikrofon yang Anda pilih.
    * **Solusi:**
        1.  **Tutup Semua Aplikasi Lain:** Pastikan tidak ada aplikasi lain (Zoom, Discord, game, perekam suara, tab browser dengan panggilan) yang sedang menggunakan mikrofon Anda. Ini penyebab paling umum!
        2.  **Cek Izin Mikrofon:** Di pengaturan privasi sistem operasi Anda, pastikan aplikasi desktop (termasuk Python) diizinkan mengakses mikrofon.
        3.  **Coba Indeks Mikrofon Lain:** Dari daftar yang muncul, coba indeks lain yang punya nama mirip dengan mikrofon Anda.
        4.  **Restart Komputer:** Solusi ajaib untuk banyak masalah teknis!

* **`Tidak Dapat Memahami` (dari Google Web Speech API)**:
    * **Apa artinya:** Google menerima audio, tetapi tidak bisa mengerti apa yang Anda katakan.
    * **Solusi:**
        1.  **Koneksi Internet Stabil:** Pastikan internet Anda benar-benar stabil saat Anda berbicara dan aplikasi memproses suara. Kadang koneksi bisa "putus-nyambung" saat upload data.
        2.  **Kualitas Audio Optimal:**
            * **Bicara Jelas & Dekat:** Dekatkan mulut Anda ke mikrofon dan bicara dengan artikulasi yang jelas.
            * **Volume Ideal:** Sesuaikan volume mikrofon Anda di pengaturan suara sistem (tidak terlalu pelan, tidak terlalu keras hingga distorsi).
            * **Minimalkan Kebisingan:** Carilah tempat yang tenang. Matikan TV, musik, atau kipas angin yang berisik.
        3.  **Pengaturan Bahasa yang Tepat:** Ini *sering sekali* jadi masalah! Pastikan di kode Anda:
            * Jika Anda bicara **Bahasa Indonesia**, gunakan: `text = r.recognize_google(audio, language="id-ID")`
            * Jika Anda bicara **Bahasa Inggris**, gunakan: `text = r.recognize_google(audio, language="en-US")`

* **`sr.RequestError` (dari Google Web Speech API)**:
    * **Apa artinya:** Ada masalah saat aplikasi mencoba menghubungi server Google.
    * **Solusi:**
        1.  **Cek Internet Anda Lagi:** Pastikan koneksi benar-benar aktif dan tidak ada kendala jaringan.
        2.  **Periksa Firewall atau Antivirus Anda.** Coba nonaktifkan sementara untuk pengujian (ingat untuk mengaktifkannya kembali setelah selesai!). Terkadang mereka memblokir aplikasi untuk mengakses jaringan eksternal.
        3.  Jika Anda menggunakan **Proxy atau VPN**, coba nonaktifkan sementara.

---
