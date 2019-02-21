import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_phyton',
)


kd_menu = input ("Kode Menu : ")
menu = input ("Menu : ")
jenis = input ("Jenis : ")
harga = input ("Harga : ")
status = input ("Status : ")
foto = input ("Foto : ")
kd_kategori = input ("Kode Kategori : ")

try:
    with connection.cursor () as cursor:
        sql = "INSERT INTO menu VALUES (%s, %s, %s, %s, %s, %s, %s)"

        try:
            cursor.execute (sql, (kd_menu, menu, jenis, harga, status, foto, kd_kategori))
            print ("Berhasil Kawan Kawan")
        except:
            print ("Gagal Kawan Coba Lagi Sampai Berhasil :)")

    connection.commit ()
finally:
    connection.close ()