# Fungsi untuk penambahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y == 0:
        return "gak bisa di bagi sama nol, mohon di perbaiki"
    else:
        return x / y

print("Pilih operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    # Meminta input dari pengguna
    pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

    # Memeriksa apakah input adalah angka
    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            print("Hasil:", tambah(angka1, angka2))
        elif pilihan == '2':
            print("Hasil:", kurang(angka1, angka2))
        elif pilihan == '3':
            print("Hasil:", kali(angka1, angka2))
        elif pilihan == '4':
            print("Hasil:", bagi(angka1, angka2))
        
        break
    else:
        print("Input tidak valid")
