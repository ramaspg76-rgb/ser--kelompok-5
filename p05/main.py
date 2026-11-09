
from komponen import Mikrofon, SensorSuhu, Servo, LampuIndikator

mik = Mikrofon("mik-1")
suhu = SensorSuhu("suhu-servo")
alis = Servo("alis", 90)
led = LampuIndikator("led") # Tambahan Job 3

mik.baca(40.0)
mik.baca(55.0)
mik.baca(70.0)
suhu.baca(31.5)
suhu.baca(36.0)
suhu.baca(33.2)
alis.gerak_ke(120)
led.atur(80) # Kita set awal 80

daftar = [mik, suhu, alis, led] # led dimasukkan ke daftar
for p in daftar:
    p.nyalakan()
    hasil = p.proses()
    print(p, "->", hasil)

# --- Kode uji LampuIndikator (Butir 6) ---
print("=== Uji LampuIndikator ===")
for nilai in [80, 150, -5]:
    led.atur(nilai)
    print(f"atur({nilai}) -> proses() = {led.proses()}")