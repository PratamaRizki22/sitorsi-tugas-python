from typing import Optional

from BST import BinarySearchTree

from sorting_algorithm import bubble_sort


my_tree = BinarySearchTree()
TypeDataBarang = list[list[int]]

TypePenjualanPerorang = list[str | TypeDataBarang | int]

TypeAllPenjualan = list[TypePenjualanPerorang]

data: TypeAllPenjualan = []  # list data menu 2


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
            for index2, _ in enumerate(data):
                print("====================================")
                if list_subtotal[index] == data[index2][2]:
                    print("nama: ", data[index2][0])
                    for index3, _ in enumerate(data[index2][1]):
                        print(f"sku {index3+1}: ", data[index2][1][index3][0])
                        print(f"jumlah barang {index3+1}: ", data[index2][1][index3][1])
                    print("subtotal: ", data[index2][2])
                print("====================================")




