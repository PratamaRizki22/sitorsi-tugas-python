from menu1 import (
    cari_stok_barang,
    input_stok_barang,
    restock_barang,
    tampilkan_stok_barang
)
from menu2 import (
    input_data_transaksi,
    lihat_data_transaksi_subtotal,
    lihat_transaksi_konsumen
) 


def menu():
    while True:
        print("============SITORSI==============")
        print("1) Kelola Stok Barang")
        print("2) Kelola transaksi konsumen")
        print("0) Keluar dari program")
        pilih = int(input("Pilih menu: "))
        if pilih == 1:  # kelola stok barang
            print("============Kelola Stok Barang===================")
            print("1) Input data stok barang")
            print("2) Restok Barang")
            print("3) Tampilkan Stok Barang")
            print("4) cari data stok barang")
            print("0) Kembali Ke menu utama")
            pilihmenu1 = int(input("Silahkan pilih menu anda: "))
            if pilihmenu1 == 0:
                print("Anda Keluar dari menu 1")
                continue
            elif pilihmenu1 == 1:
                print("Anda memlih menu 1.1(input stok barang)")
                input_stok_barang()
            elif pilihmenu1 == 2:
                print("Anda memilih menu 1.2(restock barang)")
                restock_barang()
            elif pilihmenu1 == 3:
                print("Anda memilih menu 1.3(tampilkan stok barang)")
                tampilkan_stok_barang()
            elif pilihmenu1 == 4:
                print("Anda memilih menu 1.4(cari stok barang)")
                cari_stok_barang()
        elif pilih == 2:  # kelola transaksi konsumen
            print("============Kelola Transaksi Konsumen=================")
            print("1) Input data transaksi baru")
            print("2) Lihat Seluruh Transaksi Konsumen")
            print("3) Lihat Data Transaksi berdasarkan Subtotal")
            print("0)kembali ke menu utama")
            pilihmenu2 = int(input("Silahkan pilih menu anda: "))
            if pilihmenu2 == 0:
                print("Anda Keluar dari menu 2")
                continue
            elif pilihmenu2 == 1:
                print("Anda memilih menu 2.1(input data transaksi baru)")
                input_data_transaksi()
            elif pilihmenu2 == 2:
                print("Anda memilih menu 2.2(lihat seluruh transaksi konsumen)")
                lihat_transaksi_konsumen()
            elif pilihmenu2 == 3:
                print("Anda memilih menu 2.3(lihat data transaksi berdasarkan subtotal)")
                lihat_data_transaksi_subtotal()
        elif pilih == 0:
            print("Anda Keluar dari program,Terima kasih telah menggunakan program ini")
            return False
        else:
            print("Menu tidak tersedia")
            continue