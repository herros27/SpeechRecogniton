# Proyek Pengenalan Suara Sederhana

Proyek ini adalah contoh sederhana penggunaan pustaka `speech_recognition` di Python untuk mengubah suara dari mikrofon menjadi teks. Ini menggunakan **Google Web Speech API**, yang memerlukan koneksi internet aktif.

---

## Fitur Utama

* **Deteksi Mikrofon Otomatis:** Menampilkan daftar mikrofon yang terhubung dan memungkinkan Anda memilihnya.
* **Penyesuaian Kebisingan Lingkungan:** Membantu meningkatkan akurasi pengenalan dengan menyesuaikan ambang batas kebisingan.
* **Pengenalan Suara Online:** Menggunakan API canggih dari Google untuk konversi suara ke teks.
* **Dukungan Multi-Bahasa:** Kode ini sudah diatur untuk Bahasa Indonesia (`id-ID`), tetapi mudah diubah ke bahasa lain seperti Inggris (`en-US`).

---

## Persyaratan Sistem

Sebelum memulai, pastikan sistem Anda memenuhi persyaratan berikut:

* **Sistem Operasi:** Windows, macOS, atau Linux.
* **Python:** Versi 3.x terinstal.
* **Koneksi Internet:** Diperlukan koneksi internet yang stabil untuk menggunakan Google Web Speech API.
* **Mikrofon:** Mikrofon yang berfungsi dan terdeteksi oleh sistem Anda.

---

## Instalasi

Ikuti langkah-langkah di bawah ini untuk menyiapkan proyek Anda:

1.  **Buat Lingkungan Virtual (Opsional, tapi Direkomendasikan):**
    Lingkungan virtual akan membantu mengelola dependensi proyek Anda secara terisolasi.

    ```bash
    python -m venv .venv
    ```

2.  **Aktifkan Lingkungan Virtual Anda:**

    * **Untuk Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **Untuk macOS / Linux:**
        ```bash
        source ./.venv/bin/activate
        ```

3.  **Instal Pustaka yang Diperlukan:**
    Instal pustaka `SpeechRecognition`, `PyAudio` (untuk akses mikrofon), dan `requests` (untuk pengecekan koneksi internet).

    ```bash
    pip install SpeechRecognition PyAudio requests
    ```

    **Penting: Masalah Instalasi PyAudio**
    * Jika Anda mengalami masalah saat menginstal `PyAudio` (terutama di Windows), ini seringkali karena kurangnya *build tools*. Anda mungkin perlu mengunduh file `.whl` (wheel file) yang sudah dikompilasi dari [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) yang sesuai dengan versi Python dan arsitektur sistem Anda (misalnya, `PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl` untuk Python 3.10 64-bit). Setelah diunduh, instal dengan `pip install path\to\your\PyAudio‑*.whl`.
    * **Untuk Debian/Ubuntu Linux:** Anda mungkin perlu menginstal dependensi sistem:
        ```bash
        sudo apt-get install portaudio19-dev python3-pyaudio
        ```

---

## Cara Menjalankan Aplikasi

1.  **Simpan Kode:**
    Pastikan semua kode Python Anda tersimpan dalam file bernama `main.py` di direktori utama proyek Anda.

2.  **Buka Terminal atau Command Prompt:**
    Navigasikan ke direktori tempat file `main.py` Anda berada.

    ```bash
    cd D:\Voice Asistent\SpeechRecogniton
    ```

3.  **Aktifkan Lingkungan Virtual (jika belum aktif):**

    * **Untuk Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **Untuk macOS / Linux:**
        ```bash
        source ./.venv/bin/activate
        ```

4.  **Jalankan Skrip Python:**

    ```bash
    python main.py
    ```

5.  **Ikuti Instruksi di Terminal:**
    * Skrip akan menampilkan daftar mikrofon yang tersedia di sistem Anda dengan nomor indeksnya.
    * Anda akan diminta untuk **memasukkan nomor indeks** mikrofon yang ingin Anda gunakan. Pilih mikrofon yang Anda yakini aktif dan berfungsi dengan baik.
    * Setelah itu, ikuti instruksi yang muncul di layar, seperti "Silakan ucapkan sesuatu...". Bicara dengan jelas ke mikrofon Anda.

---

## Pemecahan Masalah Umum

Berikut adalah beberapa masalah umum yang mungkin Anda temui dan solusinya:

* **`Timeout`**:
    * **Penyebab:** Skrip tidak mendeteksi ucapan dalam waktu yang ditentukan (7 detik).
    * **Solusi:** Mulai berbicara segera setelah pesan "Silakan ucapkan sesuatu...". Pastikan mikrofon aktif dan level inputnya cukup tinggi di pengaturan suara sistem Anda.

* **`AssertionError` atau `AttributeError: 'NoneType' object has no attribute 'close'`**:
    * **Penyebab:** Python gagal membuka atau menginisialisasi mikrofon yang dipilih.
    * **Solusi:**
        1.  **Tutup semua aplikasi lain** yang mungkin menggunakan mikrofon (misalnya, Zoom, Discord, aplikasi perekam suara, tab browser dengan panggilan video).
        2.  **Periksa izin mikrofon** di pengaturan privasi sistem operasi Anda. Pastikan aplikasi desktop (Python) memiliki izin untuk mengakses mikrofon.
        3.  **Coba indeks mikrofon lain** dari daftar yang ditampilkan. Kadang, ada beberapa entri serupa dan salah satunya berfungsi lebih baik.
        4.  **Restart komputer** Anda.

* **`Tidak Dapat Memahami` (dari Google Web Speech API)**:
    * **Penyebab:** Google tidak dapat menginterpretasikan audio yang dikirim.
    * **Solusi:**
        1.  **Pastikan koneksi internet Anda stabil** saat skrip memproses audio. Meskipun cek awal berhasil, koneksi bisa saja terputus atau melambat di tengah jalan.
        2.  **Tingkatkan kualitas audio:** Bicara lebih jelas dan lebih dekat ke mikrofon. Pastikan volume mikrofon Anda optimal di pengaturan suara sistem (tidak terlalu pelan, tidak terlalu keras hingga distorsi). Kurangi kebisingan latar belakang di lingkungan Anda.
        3.  **Periksa pengaturan bahasa di kode:** Pastikan `language="id-ID"` jika Anda berbicara Bahasa Indonesia, atau `language="en-US"` jika Anda berbicara Bahasa Inggris. Kesalahan ini sangat umum!

* **`sr.RequestError` (dari Google Web Speech API)**:
    * **Penyebab:** Masalah pada koneksi ke server Google atau koneksi terblokir.
    * **Solusi:**
        1.  **Periksa koneksi internet Anda** lagi.
        2.  **Periksa Firewall atau Antivirus Anda.** Coba nonaktifkan sementara untuk pengujian (ingat untuk mengaktifkannya kembali setelah selesai!). Terkadang mereka memblokir aplikasi untuk mengakses jaringan eksternal.
        3.  Jika Anda menggunakan **Proxy atau VPN**, coba nonaktifkan sementara.

---
