def hitung_galat(hasil, acuan):
    galat_absolut = abs(hasil - acuan)
    galat_relatif = (galat_absolut / abs(acuan)) * 100
    return galat_absolut, galat_relatif

def cek_status(galat_relatif, toleransi=0.5):
    if galat_relatif <= toleransi:
        return "LULUS"
    else:
        return "TIDAK LULUS"