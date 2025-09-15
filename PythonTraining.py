#Variabel
angka_int = 13
angka_float = 1.3
teks = "Taylor Swift"
list_data = [1,2,3,4]

#TipeData
print("Tipe data angka_int:", type(angka_int))
print("Tipe data angka_float:", type(angka_float))
print("Tipe data teks:", type(teks))
print("Tipe data list_data:", type(list_data))

# a. Buat list belanja
belanja = ["beras", "minyak", "telur"]

# b. Tambahkan item gula dan kopi menggunakan fungsi append()
belanja.append("gula")
belanja.append("kopi")

# c. Tampilkan semua item dengan perulangan
print("Daftar belanja:")
for item in belanja:
    print("-", item)

#Dictionary

# a. Buat dictionary harga belanjaan:
harga = {
     "beras": 12.000,
     "minyak": 17.000,
     "telur": 24.000,
     "gula":15.000,
     "kopi":20.000
}

total = sum(harga.values())
print("Total harga belanjaan: ", total)

print("-"*50)

# Fungsi
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

luas, keliling = persegi_panjang(10, 5)
print("Luas persegi panjang:", luas)
print("Keliling persegi panjang:", keliling)

print("-" * 50)

# Percabangan
usia = int(input("Masukkan usia Anda: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")