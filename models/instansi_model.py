from database.connection import get_connection

class InstansiModel:
    def __init__(self):
        self.koneksi = get_connection()

    # ===================== TAMPIL DATA =====================
    def dataInstansi(self):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT i.*, u.nama AS nama_admin FROM instansi i LEFT JOIN users u ON i.id_admin = u.id_user ORDER BY id_instansi ASC"
        aksiCur.execute(sql)
        data = aksiCur.fetchall()
        aksiCur.close()
        return data

    # ===================== FILTER BERDASARKAN NAMA =====================
    def filterInstansi(self, cari):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT i.*, u.nama AS nama_admin FROM instansi i LEFT JOIN users u ON i.id_admin = u.id_user WHERE i.nama_instansi LIKE %s"
        like = "%" + cari + "%"
        aksiCur.execute(sql, (like,))
        data = aksiCur.fetchall()
        aksiCur.close()
        return data

    # ===================== CARI BY ID =====================
    def getById(self, id_instansi):
        aksiCur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM instansi WHERE id_instansi=%s"
        aksiCur.execute(sql, (id_instansi,))
        data = aksiCur.fetchone()
        aksiCur.close()
        return data

    # ===================== SIMPAN =====================
    def simpanDataInstansi(self, nama_instansi, alamat, kontak, id_admin):
        aksiCur = self.koneksi.cursor()
        sql = "INSERT INTO instansi (nama_instansi, alamat, kontak, id_admin) VALUES (%s, %s, %s, %s)"
        aksiCur.execute(sql, (nama_instansi, alamat, kontak, id_admin))
        self.koneksi.commit()
        aksiCur.close()

    # ===================== UBAH =====================
    def ubahDataInstansi(self, nama_instansi, alamat, kontak, id_admin, id_instansi):
        aksiCur = self.koneksi.cursor()
        sql = "UPDATE instansi SET nama_instansi=%s, alamat=%s, kontak=%s, id_admin=%s WHERE id_instansi=%s"
        aksiCur.execute(sql, (nama_instansi, alamat, kontak, id_admin, id_instansi))
        self.koneksi.commit()
        aksiCur.close()

    # ===================== HAPUS =====================
    def hapusDataInstansi(self, id_instansi):
        aksiCur = self.koneksi.cursor()
        sql = "DELETE FROM instansi WHERE id_instansi=%s"
        aksiCur.execute(sql, (id_instansi,))
        self.koneksi.commit()
        aksiCur.close()
