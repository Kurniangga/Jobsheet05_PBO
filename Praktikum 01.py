# Kelas Induk
class Burung:
    def __init__(self, nama):
        self.nama = nama
    def terbang(self):
        print(f"{self.nama} terbang dengan cara umum.")
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara burung.")

# Kelas Anak 1
class Elang(Burung):
    def __init__(self, nama, rentang_sayap):
        super().__init__(nama)
        self.rentang_sayap = rentang_sayap
    # Override
    def terbang(self):
        print(f"{self.nama} terbang tinggi melayang di angkasa.")
    # Override
    def bersuara(self):
        print(f"{self.nama} berteriak nyaring!")

# Kelas Anak 2
class Pipit(Burung):
    def __init__(self, nama, warna_bulu):
        super().__init__(nama)
        self.warna_bulu = warna_bulu
    # Override
    def terbang(self):
        print(f"{self.nama} terbang cepat di antara pepohonan.")
    # Override
    def bersuara(self):
        print(f"{self.nama} berkicau merdu: Cit cit!")

# Fungsi Polimorfik
def demonstrasi_aksi_burung(daftar_burung):
    print("\nAksi Burung:")
    for burung in daftar_burung:
        print(f"-- Aksi untuk {burung.nama} --")
        burung.terbang()
        burung.bersuara()
        print("-" * 15)

if __name__ == "__main__":
    elang_jawa = Elang("Elang Jawa", 1.5)
    pipit_gereja = Pipit("Pipit Gereja", "Coklat")
    burung_aneh = Burung("Burung Misterius") 

    koleksi_burung = [elang_jawa, pipit_gereja, burung_aneh]
    demonstrasi_aksi_burung(koleksi_burung)