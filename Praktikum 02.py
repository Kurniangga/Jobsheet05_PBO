class Kucing:
    def bersuara(self):
        print("Kucing: Meow!")

class Anjing:
    def bersuara(self):
        print("Anjing: Guk guk!")

class Bebek:
    def bersuara(self):
        print("Bebek: Kwek kwek!")

class Mobil: # Kelas ini TIDAK punya metode bersuara()
    def jalankan(self):
        print("Mobil: Brummm!")

# Fungsi ini tidak peduli tipe objeknya, asal punya metode .bersuara()
def buat_suara(objek_yang_bisa_bersuara):
    try:
        objek_yang_bisa_bersuara.bersuara()
    except AttributeError:
        print(f"Objek {type(objek_yang_bisa_bersuara).__name__} tidak bisa bersuara.")

if __name__ == "__main__":
    kucing1 = Kucing()
    anjing1 = Anjing()
    bebek1 = Bebek()
    mobil1 = Mobil()

    daftar_objek = [kucing1, anjing1, bebek1, mobil1]

    print("Demonstrasi Duck Typing:")
    for item in daftar_objek:
        buat_suara(item)