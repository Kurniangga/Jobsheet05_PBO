class Burung:
    def __init__(self, nama):
        self.nama = nama
    def terbang(self):
        print(f"{self.nama} terbang dengan cara umum.")
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara burung.")

class Elang(Burung):
    def __init__(self, nama, rentang_sayap):
        super().__init__(nama)
        self.rentang_sayap = rentang_sayap
    def terbang(self):
        print(f"{self.nama} terbang tinggi melayang di angkasa.")
    def bersuara(self):
        print(f"{self.nama} berteriak nyaring!")
    def berburu(self):
        print(f"{self.nama} sedang mencari mangsa dari ketinggian.")

class Pipit(Burung):
    def __init__(self, nama, warna_bulu):
        super().__init__(nama)
        self.warna_bulu = warna_bulu
    def terbang(self):
        print(f"{self.nama} terbang cepat di antara pepohonan.")
    def bersuara(self):
        print(f"{self.nama} berkicau merdu: Cit cit!")
    def membangun_sarang(self):
        print(f"{self.nama} sedang mengumpulkan ranting untuk sarang.")

def interaksi_dengan_burung(burung):
    print(f"\n--- Berinteraksi dengan {type(burung).__name__}: {getattr(burung, 'nama', 'Objek tidak dikenal')} ---")

    if isinstance(burung, Burung):
        burung.terbang()
        burung.bersuara()

        if isinstance(burung, Elang):
            print("-> Ini adalah Elang!")
            burung.berburu() 
        elif isinstance(burung, Pipit):
            print("-> Ini adalah Pipit!")
            burung.membangun_sarang() 
        else:
            print("-> Ini adalah burung jenis umum (bukan Elang/Pipit).")
    else:
        print("-> Objek ini bukan termasuk jenis Burung.")
    print("-" * 25)

if __name__ == "__main__":
    elang_sumatra = Elang("Elang Sumatra", 1.8)
    pipit_rumah = Pipit("Pipit Rumah", "Abu-abu")
    merak = Burung("Merak") 
    kucing_tetangga = "Meong" 

    koleksi_makhluk = [elang_sumatra, pipit_rumah, merak, kucing_tetangga]

    for makhluk in koleksi_makhluk:
        interaksi_dengan_burung(makhluk)