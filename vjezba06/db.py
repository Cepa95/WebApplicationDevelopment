#!python
import mysql.connector # "C:\ProgramData\Anaconda3\python.exe" -m pip install mysql-connector 
import json
import password_utils

db_conf = {
    "host":"localhost",
    "db_name": "upisni_list",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def create_user(username, password, email):
    query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    hashed_password = password_utils.hash_password(password)
    values = (username, hashed_password, email)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid
    

def get_user(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username='" + str(username) + "'")
    myresult = cursor.fetchone()
    return myresult

def get_email():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT email FROM users")
    myresult = cursor.fetchone()
    return myresult

def get_subjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM subjects")
    myresult = cursor.fetchall()
    return myresult

def change_user_password(name, password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    hashed_password = password_utils.hash_password(password)
    query = "UPDATE users SET password=%s WHERE username=%s"
    values = (hashed_password, name)
    try:
        cursor.execute(query, values)
        mydb.commit()
        return True
    except:
        return False

def get_upisni_list(student_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT predmet_id, status FROM upisni_list WHERE student_id='" + str(student_id) + "'")
    myresult = cursor.fetchall()
    dict = {}
    for x, y in myresult:   	
        dict[x] = y
    return dict

def get_students():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    #defaultno student, u bazi se moze prominiti na admina
    cursor.execute("SELECT * FROM users WHERE uloga='student'")
    myresult = cursor.fetchall()
    return myresult 

def get_user_role(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT uloga FROM users WHERE user_id='" + str(user_id) + "'")
    myresult = cursor.fetchone()
    return myresult[0]

def add_upisni_list (student_id, predmet_id, status):
    query = '''
    INSERT INTO upisni_list
        (student_id, predmet_id, status)
    VALUES
        (%s, %s, %s)
    ON DUPLICATE KEY UPDATE
        status = VALUES(status);
    '''
    values = (student_id, predmet_id, status)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid