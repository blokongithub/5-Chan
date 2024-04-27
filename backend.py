import sqlite3

def get_db_connection():
    return sqlite3.connect("database.db")

def start():
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("CREATE TABLE IF NOT EXISTS chans(id INTEGER PRIMARY KEY AUTOINCREMENT, link TEXT UNIQUE, name TEXT)")
    mydb.execute("CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT, chan TEXT, title TEXT, body TEXT)")
    dbcon.commit()
    dbcon.close()

def makepost(chan, title, body):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("INSERT INTO posts(chan, title, body) VALUES(?, ?, ?)", (chan, title, body))
    dbcon.commit()
    dbcon.close()

def makechan(link, name, private="0", code="0"):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("INSERT INTO chans(link, name) VALUES (?, ?)", (link, name))
    dbcon.commit()
    dbcon.close()

def delchan(chan):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("DELETE FROM chans WHERE link = ?", (chan,))
    mydb.execute("DELETE FROM posts WHERE chan = ?", (chan,))
    dbcon.commit()
    dbcon.close()

def delpost(id):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("DELETE FROM posts WHERE id = ?", (id,))
    dbcon.commit()
    dbcon.close()

def panicattack():
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("DROP TABLE IF EXISTS chans")
    mydb.execute("DROP TABLE IF EXISTS posts")
    dbcon.commit()
    dbcon.close()

def getchans():
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    res = mydb.execute("SELECT * FROM chans")
    chans = res.fetchall()
    dbcon.close()
    return chans

def getchansid():
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    res = mydb.execute("SELECT link FROM chans")
    chans = res.fetchall()
    dbcon.close()
    result = [item[0] for item in chans]
    return result

def chanidtoname(link):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    res = mydb.execute("SELECT name FROM chans WHERE link = ?", (link,))
    chans = res.fetchall()
    dbcon.close()
    result = chans[0][0]
    print(chans)
    return result

def getposts(chan):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    res = mydb.execute("SELECT * FROM posts WHERE chan = ?", (chan,))
    posts = res.fetchall()
    dbcon.close()
    return posts