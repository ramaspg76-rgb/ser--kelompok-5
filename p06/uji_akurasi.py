from galat import hitung_galat, cek_status

print("--- PENGUJIAN AKURASI ---")
# Anggap ini data hasil pengolahan kita
hasil_program = [59.8, 60.2, 75.0, 81.5]
# Anggap ini nilai acuan dari dosen (spreadsheet)
nilai_acuan = [60.0, 60.0, 75.0, 80.0]

for i in range(len(hasil_program)):
    hasil = hasil_program[i]
    acuan = nilai_acuan[i]
    _, g_rel = hitung_galat(hasil, acuan)
    status = cek_status(g_rel)
    print(f"Data ke-{i+1}: Hasil={hasil}, Acuan={acuan} | Galat Relatif={g_rel:.2f}% | Status={status}")