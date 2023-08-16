from typing import Optional
from dataclasses import dataclass

@dataclass
class Node:
        no_sku:int
        nama_barang:str
        harga_satuan:int
        jumlah_stok:int
        left:Optional['Node'] = None
        right:Optional['Node'] = None

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, no_sku:int, nama_barang:str, harga_satuan:int, jumlah_stok:int):  # menu 1.1
        new_node:Node = Node(no_sku, nama_barang, harga_satuan, jumlah_stok)
        if self.root is None:
            self.root = new_node
            print("SKU berhasil ditambahkan")
            return True

        temp: Node = self.root
        while True:
            if new_node.no_sku == temp.no_sku:
                return False
            if new_node.no_sku < temp.no_sku:
                if temp.left is None:
                    temp.left = new_node
                    print("SKU berhasil ditambahkan")
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    print("SKU berhasil ditambahkan")
                    return True
                temp = temp.right

    def contains(self, no_sku:int):
        temp = self.root
        while temp is not None:
            if no_sku < temp.no_sku:
                temp = temp.left
            elif no_sku > temp.no_sku:
                temp = temp.right
            else:
                return True

    def search(self,root:Optional[Node], no_sku:int)->Optional[Node]:
        if root is None or root.no_sku == no_sku:
            return root
        if no_sku < root.no_sku:
            return self.search(root.left, no_sku)
        return self.search(root.right, no_sku)

    def tambah_stok(self,no_sku:int, stok_tambah:int):
        temp=self.root
        node:Optional[Node] = self.search(temp,no_sku)
        if node is not None:
            node.jumlah_stok +=stok_tambah
            print("Stok berhasil ditambah.")
        else:
            print("Nomor sku tidak ditemukan.")

    def kurang_stok(self,no_sku:int, stok_kurang:int):
        temp = self.root
        node:Optional[Node] = self.search(temp,no_sku)
        if node is not None:
            node.jumlah_stok -=stok_kurang
            print("Stok berhasil dikurangan.")
        else:
            print("Nomor sku tidak ditemukan.")

    def print_BST(self, temp:Optional[Node]):
        if temp is not None:
            self.print_BST(temp.left)
            print("No SKU:", temp.no_sku)
            print("Nama Barang:", temp.nama_barang)
            print("Harga Satuan:", temp.harga_satuan)
            print("Jumlah Stok:", temp.jumlah_stok)
            print()
            self.print_BST(temp.right)