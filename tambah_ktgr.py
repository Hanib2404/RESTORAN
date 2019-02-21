import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_phyton',
)

print("=====INPUT DATA FOOD KATEGORI=====")
kd_kategori = input ("Kd Kategori : ")
kategori = input ("Kategori : ")

try:
    with connection.cursor () as cursor:
        sql = "INSERT INTO kategori VALUES (%s, %s)"

        try:
            cursor.execute (sql, (kd_kategori, kategori))
            print ("Berhasil Kawan Kamu Hebat")
        except:
            print ("Gagal Kawan Kamu Harus Mengulang Ini")

    connection.commit ()
finally:
    connection.close ()