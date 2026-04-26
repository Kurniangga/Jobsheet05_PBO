import math

class Bentuk:
    def nama_bentuk(self):
        return "Bentuk Generik"
    def hitung_luas(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius
    def nama_bentuk(self):
        return "Lingkaran"
    def hitung_luas(self):
        return math.pi * (self.radius ** 2)

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    def nama_bentuk(self):
        return "Persegi"
    def hitung_luas(self):
        return self.sisi * self.sisi

class TaplakMeja:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def hitung_luas(self):
        return self.panjang * self.lebar
    def deskripsi(self):
        return f"Taplak Meja {self.panjang}x{self.lebar}"

def tampilkan_info_luas(objek_dengan_luas):
    print("-" * 20)
    try:
        luas = objek_dengan_luas.hitung_luas()
        try:
            nama = objek_dengan_luas.nama_bentuk()
        except AttributeError:
            nama = type(objek_dengan_luas).__name__

        print(f"Objek: {nama}")
        print(f"Luas : {luas:.2f}") 

    except AttributeError:
        print(f"Objek {type(objek_dengan_luas).__name__} tidak dapat dihitung luasnya (metode tidak ditemukan).")
    except NotImplementedError:
         print(f"Metode 'hitung_luas' belum diimplementasi untuk {type(objek_dengan_luas).__name__}.")

if __name__ == "__main__":
    lingkaran1 = Lingkaran(7)
    persegi1 = Persegi(5)
    taplak1 = TaplakMeja(1.5, 0.8)
    bentuk_dasar = Bentuk() 
    string_biasa = "Ini string" 

    daftar_item = [lingkaran1, persegi1, taplak1, bentuk_dasar, string_biasa]

    print("Menampilkan Info Luas (Polimorfisme Campuran):")
    for item in daftar_item:
        tampilkan_info_luas(item)