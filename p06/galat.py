def galat_absolut(hasil, acuan):
    """Mengembalikan selisih tanpa tanda minus antara hasil dan acuan."""
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    """Mengembalikan galat relatif dalam persen terhadap nilai acuan.

    Memunculkan ValueError bila acuan sama dengan 0.
    """
    if acuan == 0:
        raise ValueError("acuan 0, galat relatif tidak dapat dihitung")
    return (galat_absolut(hasil, acuan) / abs(acuan)) * 100


TOLERANSI = 0.5

def status(galat_persen):
    if galat_persen <= TOLERANSI:
        return "LULUS"
    return "TIDAK LULUS"