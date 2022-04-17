import mysql.connector as mysql

# enter your server IP address/domain name
HOST = "cpanel.insaid.co" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "Capstone1"
# this is the user you create
USER = "student"
# user password
PASSWORD = "student"
# connect to MySQL server
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())
mycursor = db_connection.cursor()

mycursor.execute("select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='phone_brand_device_model'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)