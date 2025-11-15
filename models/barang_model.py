# models/barang_model.py
from database.connection import get_connection

class BarangModel:
    def __init__(self):
        self.koneksi = get_connection()

    # ===================== TAMPIL DATA =====================
    def dataBarang(self):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM data_barang ORDER BY id_barang ASC"
        aksiCur.execute(sql)
        data = aksiCur.fetchall()
        aksiCur.close()
        return data

    # ===================== FILTER BERDASARKAN NAMA =====================
    def filterBarang(self, cari):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM data_barang WHERE nama LIKE %s OR kode LIKE %s"
        like = "%" + cari + "%"
        aksiCur.execute(sql, (like, like))
        data = aksiCur.fetchall()
        aksiCur.close()
        return data

    # ===================== CARI BY ID =====================
    def getById(self, id_barang):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM data_barang WHERE id_barang=%s"
        aksiCur.execute(sql, (id_barang,))
        data = aksiCur.fetchone()
        aksiCur.close()
        return data

    # ===================== SIMPAN =====================
    def simpanDataBarang(self, kode, nama, harga, stok):
        aksiCur = self.koneksi.cursor()
        sql = "INSERT INTO data_barang (kode, nama, harga, stok) VALUES (%s, %s, %s, %s)"
        aksiCur.execute(sql, (kode, nama, harga, stok))
        self.koneksi.commit()
        aksiCur.close()

    # ===================== UBAH =====================
    def ubahDataBarang(self, kode, nama, harga, stok, id_barang):
        aksiCur = self.koneksi.cursor()
        sql = "UPDATE data_barang SET kode=%s, nama=%s, harga=%s, stok=%s WHERE id_barang=%s"
        aksiCur.execute(sql, (kode, nama, harga, stok, id_barang))
        self.koneksi.commit()
        aksiCur.close()

    # ===================== HAPUS =====================
    def hapusDataBarang(self, id_barang):
        aksiCur = self.koneksi.cursor()
        sql = "DELETE FROM data_barang WHERE id_barang=%s"
        aksiCur.execute(sql, (id_barang,))
        self.koneksi.commit()
        aksiCur.close()

    # ===================== CEK KODE (UNTUK VALIDASI) =====================
    def cekKodeBarang(self, kode):
        aksiCur = self.koneksi.cursor()
        sql = "SELECT COUNT(*) FROM data_barang WHERE kode=%s"
        aksiCur.execute(sql, (kode,))
        jumlah = aksiCur.fetchone()[0]
        aksiCur.close()
        return jumlah

    # ===================== CEK KODE BARANG SAAT EDIT =====================
    def cekKodeBarangLain(self, kode, id_barang):
        aksiCur = self.koneksi.cursor()
        sql = "SELECT COUNT(*) FROM data_barang WHERE kode=%s AND id_barang<>%s"
        aksiCur.execute(sql, (kode, id_barang))
        jumlah = aksiCur.fetchone()[0]
        aksiCur.close()
        return jumlah

    # ===================== CEK APAKAH BARANG DI TABEL LAIN =====================
    def cekBarangDipakai(self, id_barang):
        aksiCur = self.koneksi.cursor()

        sql_masuk = "SELECT COUNT(*) FROM barang_masuk WHERE id_barang=%s"
        aksiCur.execute(sql_masuk, (id_barang,))
        jumlah_masuk = aksiCur.fetchone()[0]

        sql_keluar = "SELECT COUNT(*) FROM barang_keluar WHERE id_barang=%s"
        aksiCur.execute(sql_keluar, (id_barang,))
        jumlah_keluar = aksiCur.fetchone()[0]

        aksiCur.close()
        return jumlah_masuk + jumlah_keluar

