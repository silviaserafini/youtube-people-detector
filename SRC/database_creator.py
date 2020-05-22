import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

password=os.getenv('PASSWORD')
db_connection = mysql.connector.connect(
host="localhost",
user="root",
password=password
)

# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor(buffered=True)

# executing cursor with execute method and pass SQL query
db_cursor.execute("DROP DATABASE IF EXISTS faces_book;")

#creating the database
db_cursor.execute("CREATE DATABASE faces_book;")

#connecting to the database
db_cursor.execute("USE faces_book;")

#deleting existing table faces
sql = "DROP TABLE IF EXISTS faces;"
db_cursor.execute(sql)

# get list of all databases
db_cursor.execute("SHOW DATABASES;")
#for db in db_cursor:
  #print(db)

#Here creating database table faces
db_cursor.execute("""CREATE TABLE IF NOT EXISTS faces_book.faces (
                             face_id VARCHAR(300), 
                             face_path BLOB,
                             age  VARCHAR(200), 
                             gender VARCHAR(200), 
                             time VARCHAR(200)
                             );""")                       

#Get database table
db_cursor.execute("SHOW TABLES")
#for table in db_cursor:
	#print(table)

