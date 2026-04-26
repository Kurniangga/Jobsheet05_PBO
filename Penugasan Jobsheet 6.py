class Komputer:
    def __init__(self, merk, processor, ram_gb):
        self.merk = merk
        self.processor = processor
        self.ram_gb = ram_gb

    def info_spesifikasi(self):
        print(f"Merk: {self.merk}")
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram_gb} GB")

    def jalankan_aplikasi(self, nama_aplikasi):
        print(f"{self.merk} menjalankan aplikasi: {nama_aplikasi}...")

    def install_software(self, *args):
        if not args:
            print(f"{self.merk}: Tidak ada software yang diberikan untuk diinstal.")
        else:
            for software in args:
                print(f"Menginstall {software} di {self.merk}...")

class Laptop(Komputer):
    def __init__(self, merk, processor, ram_gb, ukuran_layar_inch, berat_kg):
        super().__init__(merk, processor, ram_gb)
        self.ukuran_layar_inch = ukuran_layar_inch
        self.berat_kg = berat_kg

    def info_spesifikasi(self):
        super().info_spesifikasi() 
        print(f"Ukuran Layar: {self.ukuran_layar_inch} inch")
        print(f"Berat: {self.berat_kg} Kg")

class Desktop(Komputer):
    def __init__(self, merk, processor, ram_gb, jenis_casing, monitor_external):
        super().__init__(merk, processor, ram_gb)
        self.jenis_casing = jenis_casing
        self.monitor_external = monitor_external

    def info_spesifikasi(self):
        super().info_spesifikasi() 
        status_monitor = "Ya" if self.monitor_external else "Tidak"
        print(f"Jenis Casing: {self.jenis_casing}")
        print(f"Monitor External: {status_monitor}")

def cetak_semua_spesifikasi(daftar_komputer):
    print("\n=== DAFTAR SPESIFIKASI KOMPUTER ===")
    for komputer in daftar_komputer:
        komputer.info_spesifikasi()
        print("-" * 30)

if __name__ == "__main__":
    laptop_gaming = Laptop("ASUS ROG", "Intel Core i7", 16, 15.6, 2.3)
    desktop_kantor = Desktop("Lenovo ThinkCentre", "Intel Core i5", 8, "Mini-PC", True)

    koleksi_komputer = [laptop_gaming, desktop_kantor]

    cetak_semua_spesifikasi(koleksi_komputer)

    print("\n=== DEMONSTRASI SIMULASI OVERLOADING ===")

    print("-> Instalasi pada Laptop:")
    laptop_gaming.install_software("Visual Studio Code")
    
    print("\n-> Instalasi pada Desktop:")
    desktop_kantor.install_software("Microsoft Office", "Google Chrome", "Cisco Packet Tracer")