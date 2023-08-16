from typing import Optional

from BST import BinarySearchTree


my_tree = BinarySearchTree()
TypeDataBarang = list[list[int]]

TypePenjualanPerorang = list[str | TypeDataBarang | int]

TypeAllPenjualan = list[TypePenjualanPerorang]
data: TypeAllPenjualan = []  # list data menu 3


def input_data_transaksi():  # menu 2.1 input data transaksi baru
    databarang: TypeDataBarang = []  # data barang dibeli (sku dan jumlah)
    nama_konsumen = str(input("Masukkan nama konsumen: "))
    no_sku_barang_dibeli: int = int(input("Masukkan no sku barang yang dibeli: "))
    cek_sku: Optional[bool] = my_tree.contains(no_sku_barang_dibeli)
    while True:
        print(data)
        if cek_sku:
            print("SKU sudah terdaftar")

            jumlah_barang_dibeli: int = int(
                input("Masukkan jumlah barang yang dibeli: ")
            )
            if (
                jumlah_barang_dibeli
                <= my_tree.search(my_tree.root, no_sku_barang_dibeli).jumlah_stok
            ):
                print("Transaksi berhasil")
                databarang.append([no_sku_barang_dibeli, jumlah_barang_dibeli])
                my_tree.kurang_stok(no_sku_barang_dibeli, jumlah_barang_dibeli)

                sub_total = my_tree.root.harga_satuan * jumlah_barang_dibeli

                data.append([nama_konsumen, databarang, sub_total])
                print("Transaksi berhasil")
                while True:
                    tambah_data = input(
                        "Apakah ada sku barang lain yang akan dibeli? (Y/N): "
                    )
                    if tambah_data == "Y":
                        inp_sku = int(input("Masukkan no sku: "))
                        inp_jumlah = int(input("Masukkan jumlah: "))
                        if my_tree.root.jumlah_stok > jumlah_barang_dibeli:
                            my_tree.kurang_stok(inp_sku, inp_jumlah)
                            print("Transaksi berhasil")
                            for index, _ in enumerate(data):
                                for index2, _ in enumerate(data[index][1]):
                                    if data[index][1][index2][0] == inp_sku:
                                        data[index][1][index2][1] += inp_jumlah
                                        data[index][2] += (
                                            my_tree.root.harga_satuan * inp_jumlah
                                        )

                                    else:
                                        data[index][1].append([inp_sku, inp_jumlah])

                        elif (
                            my_tree.search(my_tree.root, inp_sku).jumlah_stok
                            < jumlah_barang_dibeli
                        ):
                            print(
                                "Transaksi gagal karena barang tak mencukupi=>silahkan input ulang"
                            )
                            return True

                    elif tambah_data == "N":
                        print("Transaksi selesai")
                        return False

            elif jumlah_barang_dibeli > my_tree.root.jumlah_stok:
                print("barang tak mencukupi")
                lanjut = input("Apakah anda ingin melanjutkan transaksi? (Y/N): ")
                if lanjut == "Y":
                    return True
                elif lanjut == "N":
                    print("Transaksi dibatalkan")
                    return False

        elif cek_sku == None:
            print("No. SKU yang diinputkan blm terdaftar")
            lanjut = input("Apakah anda ingin melanjutkan transaksi? (Y/N): ")
            if lanjut == "Y":
                print("Masukkan No. SKU ")
                no_sku_baru = int(input("Masukkan no sku: "))
                nama_barang_baru = input("Masukkan nama barang: ")
                harga_satuan_baru = int(input("Masukkan harga satuan: "))
                jumlah_stok_baru = int(input("Masukkan jumlah stok: "))

                my_tree.insert(
                    no_sku_baru, nama_barang_baru, harga_satuan_baru, jumlah_stok_baru
                )
                print("data sudah ditambahkan, silahkan input ulang")
                input_data_transaksi()  # input ulang
            elif lanjut == "N":
                print("Transaksi dibatalkan")
                exit()


def lihat_transaksi_konsumen():  # menu 2.2
    if len(data) == 0:
        print("Data transaksi masih kosong")
    else:
        print("Seluruh data transaksi konsumen: ")
        for index, _ in enumerate(data):
            a = 1
            print("nama: ", data[index][0])
            for index2, _ in enumerate(data[index][1]):
                print(f"sku barang {a}: ", data[index][1][index2][0])
                print(f"jumlah barang {a}: ", data[index][1][index2][1])
                a += 1
                print("\n")
            print("subtotal: ", data[index][2], "\n")


def lihat_data_transaksi_subtotal():  # menggunakan bubble short #menu 2.3
    list_subtotal: TypePenjualanPerorang = []
    for penjualan, _ in enumerate(data):
        get_sub_total = data[penjualan][2]
        list_subtotal.append(get_sub_total)

    def bubble_sort(my_list: list[int]) -> list[int]:
        for i in range(len(my_list) - 1, 0, -1):
            for j in range(i):
                if my_list[j] < my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
        return my_list

    bubble_sort(list_subtotal)

    if len(list_subtotal) == 0:
        print("Data transaksi masih kosong")
    else:
        print("Data transaksi berdasarkan subtotal: ")
        for index, _ in enumerate(list_subtotal):
            for index2, _ in enumerate(data):
                print("====================================")
                if list_subtotal[index] == data[index2][2]:
                    print("nama: ", data[index2][0])
                    for index3, _ in enumerate(data[index2][1]):
                        print(f"sku {index3+1}: ", data[index2][1][index3][0])
                        print(f"jumlah barang {index3+1}: ", data[index2][1][index3][1])
                    print("subtotal: ", data[index2][2])
                print("====================================")


def input_stok_barang():  # menu 1.1
    no_sku = int(input("Masukkan no sku: "))
    if len(str(no_sku)) != 4:
        print("SKU harus 4 digit angka")
        return False
    elif len(str(no_sku)) == 4:
        a = my_tree.contains(no_sku)
        if a:
            print("SKU sudah terdaftar=>anda tidak bisa menambahkan data yang sama")
            # return False
        else:
            nama_barang = input("Silahkan Masukkan nama barang: ")
            harga_satuan = int(input("Masukkan harga satuan: "))
            jumlah_stok = int(input("Masukkan jumlah stok: "))
            my_tree.insert(no_sku, nama_barang, harga_satuan, jumlah_stok)

        lagi = input("Apakah anda ingin menambahkan data lagi? (Y/N): ")
        if lagi == "Y":
            input_stok_barang()
        elif lagi == "N":
            print("Anda tidak menambahkan data lagi")
            print("Data stok barang: ")
            my_tree.print_BST(my_tree.root)
            return True


def restock_barang():  # menu 1.2
    no_sku = int(input("Masukkan no sku: "))
    a = my_tree.contains(no_sku)
    if a:
        print("SKU sudah terdaftar")
        restock = int(input("Masukkan jumlah barang yang di restock: "))
        my_tree.tambah_stok(no_sku, restock)
    else:
        print("SKU belum terdaftar => buat sku data stok barang terlebih dahulu")
        create_new_sku()


def create_new_sku() -> bool:
    no_sku = int(input("Masukkan no sku: "))
    node = my_tree.contains(no_sku)

    if node is None:
        nama_barang = input("Masukkan nama barang: ")
        harga_satuan = int(input("Masukkan harga satuan: "))
        jumlah_stok = int(input("Masukkan jumlah stok: "))
        my_tree.insert(no_sku, nama_barang, harga_satuan, jumlah_stok)
        return True

    print("SKU sudah terdaftar => berhasil restock")
    return False


def cari_stok_barang():  # menu 1.4
    no_sku: int = int(input("Masukkan nomor SKU barang yang ingin ditampilkan: "))
    node = my_tree.search(my_tree.root, no_sku)
    if node is None:
        print("Barang dengan nomor SKU tersebut tidak ditemukan.")

    else:
        print("No SKU:", node.no_sku)
        print("Nama Barang:", node.nama_barang)
        print("Harga Satuan:", node.harga_satuan)
        print("Jumlah Stok:", node.jumlah_stok)


def tampilkan_stok_barang():  # menu 1.3
    if my_tree.root is None:
        print("Data stok barang masih kosong")
    else:
        my_tree.print_BST(my_tree.root)
