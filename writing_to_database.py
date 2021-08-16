import pymysql 
import os 
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

mydb = pymysql.connect(
host,
user,
password,
database,
)

cursor = mydb.cursor()


# cursor.execute("CREATE TABLE store (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO store (name, address) VALUES (%s)(%s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)
mydb.commit()
cursor.close()
mydb.close()

print(cursor.rowcount, "record inserted.")
