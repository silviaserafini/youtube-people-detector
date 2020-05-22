import sqlalchemy as db
import getpass
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


password= os.getenv('PASSWORD')

db_name = "faces_book"
connection_data = f"mysql+pymysql://root:{password}@localhost/{db_name}"
engine = db.create_engine(connection_data)
connection = engine.connect()
print("Connected to server!")

def add_face(face_id1,face_path1,age1,gender1,time1):
    query = """INSERT INTO faces (face_id,face_path, age, gender,time) 
        VALUES (%s,%s,%s,%s,%s);"""
    val = (face_id1,face_path1,age1,gender1,time1)
    connection.execute(query,val) 
    return "Ok!"

def get_face_data(face_id):
    query = """
        SELECT face_id, age, gender,time FROM faces WHERE face_id='{}'
    """.format(face_id)
    df= pd.read_sql_query(query, engine)
    return df

def get_all_data():
    query = """
        SELECT * FROM faces 
    """
    df= pd.read_sql_query(query, engine)
    return df


