import numpy as np
import audio


def main():
    print("== Uji input buatan ==")
    print("konstan 0.1 -> dBFS", round(float(audio.hitung_dbfs(np.full(100, 0.1))), 3))
    print("konstan 0.5 -> dBFS", round(float(audio.hitung_dbfs(np.full(100, 0.5))), 3))
    print("konstan 1.0 -> dBFS", round(float(audio.hitung_dbfs(np.full(100, 1.0))), 3))

    print("level_db konstan 0.1 =", audio.ke_level_db(np.full(100, 0.1)))
    print("level_db konstan 1.0 =", audio.ke_level_db(np.full(100, 1.0)))

    try:
        audio.hitung_dbfs(np.zeros(100))
    except ValueError as e:
        print("ditolak:", e)

    print("== Daftar perangkat input ==")
    for no, nama in audio.daftar_masukan():
        print(no, "|", nama)

    print("== Rekam 0.5 detik (diam) ==")
    diam = audio.rekam(0.5)
    print("jumlah sampel:", len(diam))
    print("level_db diam  :", audio.ke_level_db(diam))

    input("Tekan Enter lalu bicara/tepuk pelan... ")
    print("== Rekam 0.5 detik (suara) ==")
    suara = audio.rekam(0.5)
    print("jumlah sampel:", len(suara))
    print("level_db suara :", audio.ke_level_db(suara))


if __name__ == "__main__":
    main()