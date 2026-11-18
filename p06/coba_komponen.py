from komponen import Mikrofon, Servo

print("--- UJI MIKROFON ---")
m = Mikrofon("Mic 1")
m.baca(60.0)
m.baca(70.5)
m.baca(55.0)
print(m.data)
print("Rata-rata:", m.proses())

try:
    m.baca(25.0) # Harus error karena di bawah 30.0
except ValueError as e:
    print("Error:", e)

m2 = Mikrofon("Mic 2")
try:
    print(m2.proses()) # Harus error karena belum ada data
except ValueError as e:
    print("Error:", e)

print("\n--- UJI SERVO ---")
s = Servo("Servo 1")
s.gerak_ke(90)
print("Posisi:", s.proses())
s.gerak_ke(180)
print("Posisi:", s.proses())

try:
    s.gerak_ke(-10) # Harus error karena di luar 0-180
except ValueError as e:
    print("Error:", e)