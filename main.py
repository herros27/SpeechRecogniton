

import speech_recognition as sr
import os
import time # Import modul time untuk jeda jika diperlukan

r = sr.Recognizer()

print("Daftar Mikrofon yang Tersedia:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"[{index}] {name}")

try:
    selected_index = int(input("Masukkan nomor indeks mikrofon yang ingin Anda gunakan: "))
    if selected_index < 0 or selected_index >= len(sr.Microphone.list_microphone_names()):
        print("Indeks tidak valid. Menggunakan mikrofon default (indeks 0).")
        microphone_index = 0
    else:
        microphone_index = selected_index
except ValueError:
    print("Input tidak valid. Menggunakan mikrofon default (indeks 0).")
    microphone_index = 0

print(f"\nMemilih mikrofon: {sr.Microphone.list_microphone_names()[microphone_index]} (Indeks: {microphone_index})\n")

with sr.Microphone(device_index=microphone_index) as source:
    print("--- Mohon Tenang Sebentar ---")
    print("Menyesuaikan dengan kebisingan lingkungan Anda. Ini membantu pengenalan lebih akurat.")

    # Meningkatkan durasi penyesuaian kebisingan untuk hasil yang lebih baik
    # Jika lingkungan Anda cukup stabil, 1 detik sudah cukup, tapi 2 detik bisa lebih baik.
    r.adjust_for_ambient_noise(source, duration=2) 
    print("Penyesuaian kebisingan selesai.")
    time.sleep(0.5) # Memberi sedikit jeda agar tidak terlalu cepat

    print("--- Siap Mendengarkan! ---")
    print("Silakan ucapkan sesuatu...")

    try:
        # Meningkatkan timeout untuk memberi lebih banyak waktu bagi ucapan untuk dimulai
        # dan phrase_time_limit untuk memberi waktu lebih lama untuk satu frasa.
        audio = r.listen(source, timeout=7, phrase_time_limit=15)

        print("--- Sedang Memproses Ucapan Anda (Online dengan Google Web Speech API)... ---")
        
        # --- PERHATIAN PENTING DI SINI: PILIH BAHASA YANG TEPAT! ---
        # Jika Anda berbicara Bahasa Inggris, gunakan "en-US".
        # Jika Anda berbicara Bahasa Indonesia, **WAJIB** ganti menjadi "id-ID".
        # Contoh jika ingin Bahasa Indonesia:
        # text = r.recognize_google(audio, language="id-ID")
        
        # Saat ini masih diset "en-US" sesuai kode terakhir Anda. Sesuaikan jika Anda bicara bahasa Indonesia.
        text = r.recognize_google(audio, language="id-ID") 

        print("\n--- Hasil Pengenalan Suara ---")
        print(f"Anda Mengatakan: {text}")

    except sr.WaitTimeoutError:
        print("\n--- Timeout ---")
        print("Tidak ada ucapan yang terdeteksi dalam waktu yang ditentukan (7 detik). Coba bicara segera setelah 'Siap Mendengarkan!'.")
    except sr.UnknownValueError:
        print("\n--- Tidak Dapat Memahami ---")
        print("Maaf, Google Web Speech API tidak dapat memahami ucapan Anda.")
        print("Penyebab umum:")
        print("  1. Tidak ada **koneksi internet stabil** saat pengenalan berlangsung.")
        print("  2. Kualitas audio buruk: terlalu pelan, terlalu banyak kebisingan latar belakang, atau distorsi.")
        print("  3. Anda berbicara dalam bahasa yang berbeda dari yang diatur di kode (misal: bicara Indonesia tapi `language='en-US'`).")
        print("Mohon periksa poin-poin di atas dan coba bicara lebih jelas.")
    except sr.RequestError as e:
        print(f"\n--- Kesalahan Layanan Online (Koneksi/API) ---")
        print(f"Terjadi kesalahan saat meminta hasil dari Google Web Speech API: {e}")
        print("Penyebab:")
        print("  1. Koneksi internet terputus atau tidak stabil.")
        print("  2. Ada masalah dengan server Google (jarang terjadi).")
        print("  3. Firewall atau proxy memblokir akses internet Python.")
        print("Mohon periksa koneksi internet Anda.")
    except Exception as e:
        print(f"\n--- Kesalahan Tak Terduga ---")
        print(f"Terjadi kesalahan yang tidak terduga: {e}")