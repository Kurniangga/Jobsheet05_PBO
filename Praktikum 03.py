class KalkulatorSederhana:
    def __init__(self, nama="Kalkulator"):
        self.nama = nama
        print(f"{self.nama} siap digunakan.")

    def tambah(self, *args):
        print(f"\nMemanggil metode tambah dengan argumen: {args}")
        if not args:
            print("Tidak ada angka untuk dijumlahkan.")
            return 0 

        total = 0
        valid_input = True
        for angka in args:
            if isinstance(angka, (int, float)):
                total += angka
            else:
                print(f"Peringatan: Argumen '{angka}' bukan angka dan akan diabaikan.")
                valid_input = False

        if valid_input:
            print(f"Hasil penjumlahan: {total}")
        else:
             print(f"Hasil penjumlahan (dengan beberapa input diabaikan): {total}")
        return total

if __name__ == "__main__":
    calc = KalkulatorSederhana("Calc-01")

    print("\n--- Percobaan Penjumlahan ---")
    calc.tambah(5, 10)
    calc.tambah(2, 3, 5, 10)
    calc.tambah(100)
    calc.tambah() 
    calc.tambah(1, 2, "tiga", 4, 5.5)