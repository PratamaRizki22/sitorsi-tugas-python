from typing import Optional

TypeDataBarang = list[list[int]]

TypePenjualanPerorang = list[str | TypeDataBarang | int]

TypeAllPenjualan = list[TypePenjualanPerorang]


def transaksi(
    data: TypeAllPenjualan, input_sku: int, inp_jumlah: int
) -> Optional[list[list[int]]]:
    for index, _ in enumerate(data):
        for index2, _ in enumerate(data[index][1]):
            if input_sku != data[index][1][index2][0]:
                return data[index][1].append([input_sku, inp_jumlah])

            else:
                data[index][1][index2][1] += inp_jumlah
                data[index][2] += my_tree.root.harga_satuan * inp_jumlah


def print_data_transaksi(index: int, list_subtotal: list[int], data: TypeAllPenjualan):
    for index2, _ in enumerate(data):
        print(15 * "=")
        if list_subtotal[index] == data[index2][2]:
            print("nama: ", data[index2][0])
            for index3, _ in enumerate(data[index2][1]):
                print(f"sku {index3+1}: ", data[index2][1][index3][0])
                print(f"jumlah barang {index3+1}: ", data[index2][1][index3][1])
            print("subtotal: ", data[index2][2])
        print(15 * "=")


def create_new_sku() -> bool:
    from menu1 import my_tree

    no_sku = int(input("Masukkan no sku: "))
    cek_sku = my_tree.contains(no_sku)

    if cek_sku is False:
        nama_barang = input("Masukkan nama barang: ")
        harga_satuan = int(input("Masukkan harga satuan: "))
        jumlah_stok = int(input("Masukkan jumlah stok: "))
        my_tree.insert(no_sku, nama_barang, harga_satuan, jumlah_stok)
        return True

    print("SKU sudah terdaftar => berhasil restock")
    return False
