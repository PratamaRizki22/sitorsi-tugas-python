from BST import BinarySearchTree
from help_func import create_new_sku

my_tree = BinarySearchTree()


def input_stok_barang():  #* menu 1.1
        create_new_sku()
        lagi = input("Apakah anda ingin menambahkan data barang lagi? (Y/N): ")
        if lagi == "Y":
            input_stok_barang()
        elif lagi == "N":
            print("Anda tidak menambahkan data lagi")
            print("Data stok barang: ")
            my_tree.print_BST(my_tree.root)
            return True


def restock_barang():  #* menu 1.2
    no_sku = int(input("Masukkan no sku: "))
    cek_sku = my_tree.contains(no_sku)
    if cek_sku == True:
        print("SKU sudah terdaftar")
        jumlah_restock = int(input("Masukkan jumlah barang yang di restock: "))
        my_tree.add(no_sku, jumlah_restock)
    else:
        print("SKU belum terdaftar => buat sku data stok barang terlebih dahulu")
        create_new_sku()


def tampilkan_stok_barang():  #* menu 1.3
    if my_tree.root is None:
        print("Data stok barang masih kosong")
    else:
        my_tree.print_BST(my_tree.root)


def cari_stok_barang():  #* menu 1.4
    no_sku: int = int(input("Masukkan nomor SKU barang yang ingin ditampilkan: "))
    get_data = my_tree.search(my_tree.root, no_sku)
    if get_data is None:
        print("Barang dengan nomor SKU tersebut tidak ditemukan.")

    else:
        print("No SKU:", get_data.no_sku)
        print("Nama Barang:", get_data.nama_barang)
        print("Harga Satuan:", get_data.harga_satuan)
        print("Jumlah Stok:", get_data.jumlah_stok)
