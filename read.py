import pymysql.cursors

SERVER_URL = "localhost"
DB = "concessionaria_db"
USER_NAME = "app_conc_user"
PASSWORD = "123"

SQL_CONNECTION = pymysql.connect(host=SERVER_URL,
    user=USER_NAME,
    passwd=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True)

SQL = """SELECT * 
         FROM carro"""

with SQL_CONNECTION.cursor() as cursor:
    try:
        sql_exec = cursor.execute(SQL)
        if sql_exec:
            print(sql_exec)
            print(cursor.fetchall())
        else:
            print(sql_exec)
            print("No Record")
    except (pymysql.Error, pymysql.Warning) as e:
        print('error! {e}')
    finally:
        SQL_CONNECTION.close()