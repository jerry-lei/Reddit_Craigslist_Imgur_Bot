import sqlite3

def intoDB(sub_id, album_id):
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("INSERT INTO cl_log VALUES(?, ?)", [sub_id,album_id])
    conn.commit()
    conn.close()

def intoDB2(sub_id):
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("INSERT INTO sub_log VALUES(?)", [sub_id])
    conn.commit()
    conn.close()

def intoDB3(com_id):
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("INSERT INTO com_log VALUES(?)", [com_id])
    conn.commit()
    conn.close()

def checkDB(sub_id, table):
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    if table == "sub_log":
        c.execute('SELECT * FROM sub_log WHERE submission_id=?', [sub_id])
    elif table == "cl_log":
        c.execute('SELECT * FROM cl_log WHERE submission_id=?', [sub_id])
    elif table == "com_log":
        c.execute('SELECT * FROM com_log WHERE comment_id=?', [sub_id])
    if c.fetchone() == None:
        conn.close()
        return True
    else:
        conn.close
        return False
