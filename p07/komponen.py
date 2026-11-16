from gpiozero import AngularServo
from perangkat import Sensor, Aktuator
from statistik import rata_rata, tertinggi
from validasi import dalam_rentang, BATAS_BAWAH, BATAS_ATAS

class Mikrofon(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "dB")

    def baca(self, nilai):
        if not dalam_rentang(nilai, BATAS_BAWAH, BATAS_ATAS):
            raise ValueError("level di luar rentang mikrofon")
        super().baca(nilai)
        
    def proses(self):
        if len(self.data) == 0:
            raise ValueError("Mikrofon belum memiliki data")
        return rata_rata(self.data)


class SensorSuhu(Sensor):
    def __init__(self, nama):
        super().__init__(nama, "C")

    def proses(self):
        return tertinggi(self.data)


class Servo(Aktuator):
    def __init__(self, nama, nilai_awal=0, pin=None):
        super().__init__(nama, nilai_awal)
        self.perangkat = None
        if pin is not None:
            self.perangkat = AngularServo(
                pin,
                initial_angle=nilai_awal,
                min_angle=0,
                max_angle=180
            )

    def gerak_ke(self, sudut):
        if not dalam_rentang(sudut, 0, 180):
            raise ValueError("sudut harus 0 sampai 180")
        self.nilai = sudut
        if self.perangkat is not None:
            self.perangkat.angle = sudut

    def lebar_pulsa(self):
        if self.perangkat is None:
            return None
        return round(self.perangkat.pulse_width * 1000, 3)

    def proses(self):
        return self.nilai
    


class LampuIndikator(Aktuator):
    def atur(self, persen):
        if persen < 0:
            persen = 0
        if persen > 100:
            persen = 100
        self.nilai = persen

    def proses(self):
        return self.nilai / 100.0
    
    

def tertinggi(data):
    if not data:
        return 0.0
    return max(data)


if __name__ == "__main__":
    m = Mikrofon("mik-test")
    m.baca(40.0)
    m.baca(60.0)
    print(f"Hasil proses Mikrofon: {m.proses()}")

    sv = Servo("servo-test")
    sv.gerak_ke(150)
    print(f"Hasil proses Servo: {sv.proses()}")