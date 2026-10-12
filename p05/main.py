from komponen import Mikrofon, SensorSuhu, Servo, LampuIndikator

# 1. Instansiasi objek
mik = Mikrofon("mik-1")
suhu = SensorSuhu("suhu-1")
alis = Servo("alis", 90)
led = LampuIndikator("led-1")

# 2. Pengisian data / aksi
mik.baca(40.0)
mik.baca(55.0)
mik.baca(70.0)

suhu.baca(31.5)
suhu.baca(36.0)
suhu.baca(33.2)

alis.gerak_ke(120)
led.atur(-5)

# 3. Pengujian Polimorfisme (perulangan seragam pada daftar perangkat)
daftar_perangkat = [mik, suhu, alis, led]

print("=== Pengujian Polimorfisme (Job 3) ===")
for p in daftar_perangkat:
    p.nyalakan()
    hasil = p.proses()  # Memanggil proses() sesuai class masing-masing
    print(f"{p} -> Hasil Proses: {hasil}")
    
