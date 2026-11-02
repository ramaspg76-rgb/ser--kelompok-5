from galat import galat_absolut, galat_relatif

TOLERANSI = 0.5

def status(galat_persen):
    if galat_persen <= TOLERANSI:
        return "LULUS"
    return "TIDAK LULUS"

# --- GANTI ANGKA DI BAWAH INI DENGAN TIGA PASANGAN DARI MODUL ANDA ---
tiga_pasangan = [
    (52.5, 50.0),
    (48.0, 50.0),
    (50.2, 50.0)
]

print("=== PENGUJIAN TIGA PASANGAN PERTAMA ===")
for hasil, acuan in tiga_pasangan:
    ga = galat_absolut(hasil, acuan)
    gr = galat_relatif(hasil, acuan)
    st = status(gr)
    
    print(f"Hasil: {hasil}, Acuan: {acuan}")
    print(f"  Galat Absolut : {ga}")
    print(f"  Galat Relatif : {gr}%")
    print(f"  Status        : {st}")
    print("-" * 35)

print("\n=== PENGUJIAN PASANGAN KEEMPAT (7.0, 0) ===")
hasil_4 = 7.0
acuan_4 = 0

# Galat absolut tetap bisa dihitung
ga_4 = galat_absolut(hasil_4, acuan_4)
print(f"Hasil: {hasil_4}, Acuan: {acuan_4}")
print(f"  Galat Absolut : {ga_4}")

# Galat relatif harus ditangkap dengan try-except karena acuan = 0
try:
    gr_4 = galat_relatif(hasil_4, acuan_4)
    st_4 = status(gr_4)
    print(f"  Galat Relatif : {gr_4}%")
    print(f"  Status        : {st_4}")
except ValueError as e:
    print(f"  Galat Relatif : Error!")
    print(f"  Status        : Tidak dapat dihitung")
    print(f"  Pesan Error   : {e}")