from galat import hitung_galat, cek_status

print("--- UJI GALAT ---")
# Pasangan 1: Hasil 52.5, Acuan 50.0
g_abs1, g_rel1 = hitung_galat(52.5, 50.0)
status1 = cek_status(g_rel1)
print(f"Hasil: 52.5, Acuan: 50.0 -> Galat Absolut: {g_abs1}, Galat Relatif: {g_rel1}%, Status: {status1}")

# Pasangan 2: Hasil 61.0, Acuan 60.0
g_abs2, g_rel2 = hitung_galat(61.0, 60.0)
status2 = cek_status(g_rel2)
print(f"Hasil: 61.0, Acuan: 60.0 -> Galat Absolut: {g_abs2}, Galat Relatif: {g_rel2}%, Status: {status2}")

# Pasangan 3: Hasil 40.0, Acuan 42.0
g_abs3, g_rel3 = hitung_galat(40.0, 42.0)
status3 = cek_status(g_rel3)
print(f"Hasil: 40.0, Acuan: 42.0 -> Galat Absolut: {g_abs3}, Galat Relatif: {g_rel3}%, Status: {status3}")
print("\n--- UJI PESAN ERROR ---")
g_abs4, g_rel4 = hitung_galat("61.8", 60.0) # Sengaja pakai teks (pakai tanda kutip)
print(g_abs4)