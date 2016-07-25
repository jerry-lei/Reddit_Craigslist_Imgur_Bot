import sqlite3

def intoDB(sub_id, album_id):
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("INSERT INTO cl_log VALUES(?, ?)", [sub_id,album_id])
    conn.commit()
    conn.close()

def checkDB(sub_id):
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    t = (sub_id,)
    c.execute('SELECT * FROM cl_log WHERE submission_id=?',t)
    if c.fetchone() == None:
        conn.close()
        return True
    else:
        conn.close
        return False
