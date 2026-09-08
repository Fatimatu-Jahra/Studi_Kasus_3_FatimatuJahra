daftar_buku = (
    "Kambing Jantan",
    "Cinta Brontosaurus", 
    "Marmut Merah Jambu",
    "Manusia Setengah Salmon",
    "Koala Kumal")
pinjaman = []

print("Daftar Buku Karya Raditya Dika: ")
for i in daftar_buku:
    print(i)

while True:
    print("1. Pinjam Buku")
    print("2. Kembalikan Buku")
    print("3. Lihat Daftar Pinjaman")
    print("4. Keluar")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        judul = input("Masukkan judul buku yang ingin anda pinjam: ")
        if judul in daftar_buku:
            pinjaman.append(judul)
            print("Buku berhasil dipinjam.")
        else:
            print("Buku tidak tersedia.")
    elif pilihan == "2":
        if pinjaman:
            judul = input("Masukkan judul buku yang ingin anda kembalikan: ")
            if judul in pinjaman:
                pinjaman.remove(judul)
                print("Buku berhasil dikembalikan.")
            else:
                print("Buku tidak ada dalam daftar.")
        else:
            print("Tidak ada buku yang dipinjam.")
    elif pilihan == "3":
        if pinjaman:
            print("Daftar Buku yang Dipinjam: ", pinjaman)
        else:
            print("Tidak ada buku yang dipinjam.")
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan perpustakaan.")     
        break