import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_phyton',
)

try:
    with connection.cursor () as cursor:
        sql = "SELECT kd_kategori, kategori, 'desc' FROM kategori"
        try:
            cursor.execute (sql)
            result = cursor.fetchall ()

            print ("Kode Kategori\t\t\tKategori")
            print ("----------------------------------------------------------")
            for row in result:
                print (str (row[0]) + "\t\t\t\t" + row[1] )

        except:
            print ("Whoops! Something wrong")

    connection.commit ()
finally:
    connection.close ()