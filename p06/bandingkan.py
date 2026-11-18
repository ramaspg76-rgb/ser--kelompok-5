print("--- PERBANDINGAN TANPA VALIDASI VS DENGAN VALIDASI ---")
# Tanpa validasi (menganggap -999 itu benar)
galat_tanpa_validasi = abs(-999 - 60.0) / 60.0 * 100
print(f"Galat tanpa validasi: {galat_tanpa_validasi}% (Output wajar? TIDAK)")

# Dengan validasi (membuang -999, pakai rata-rata asli)
galat_dengan_validasi = abs(61.8 - 60.0) / 60.0 * 100
print(f"Galat dengan validasi : {galat_dengan_validasi}% (Output wajar? YA)")