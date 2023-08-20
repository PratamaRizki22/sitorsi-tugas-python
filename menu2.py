from typing import Optional
from menu1 import my_tree, create_new_sku

from sorting_algorithm import bubble_sort


TypeDataBarang = list[list[int]]

TypePenjualanPerorang = list[str | TypeDataBarang | int]

TypeAllPenjualan = list[TypePenjualanPerorang]

data: TypeAllPenjualan = []  # list data menu 2


def transaction(data: TypeAllPenjualan,input_sku: int, inp_jumlah: int):
    for index, _ in enumerate(data):
        for index2, _ in enumerate(data[index][1]):
            if input_sku !=  data[index][1][index2][0]:
                data[index][1].append([inp_sku, inp_jumlah])

            else:
                data[index][1][index2][1] += inp_jumlah
                data[index][2] += my_tree.root.harga_satuan * inp_jumlah



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

                            transaction(data, inp_sku, inp_jumlah)

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

            if lanjut == "N":
                print("Transaksi dibatalkan")
                exit()
            elif lanjut == "Y":
                create_new_sku()
                print("data sudah ditambahkan, silahkan input ulang")
                input_data_transaksi()  # input ulang

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
    list_subtotal = []
    for penjualan, _ in enumerate(data):
        get_sub_total = data[penjualan][2]
        list_subtotal.append(get_sub_total)

    bubble_sort(list_subtotal)

    if len(list_subtotal) == 0:
        print("Data transaksi masih kosong")
    else:
        print("Data transaksi berdasarkan subtotal: ")
        for index, _ in enumerate(list_subtotal):
            print_data_transaksi(index, list_subtotal)

def print_data_transaksi(index: int, list_subtotal: list[int]):
    for index2, _ in enumerate(data):
                print(15*"=")
                if list_subtotal[index] == data[index2][2]:
                    print("nama: ", data[index2][0])
                    for index3, _ in enumerate(data[index2][1]):
                        print(f"sku {index3+1}: ", data[index2][1][index3][0])
                        print(f"jumlah barang {index3+1}: ", data[index2][1][index3][1])
                    print("subtotal: ", data[index2][2])
                print(15*"=")
