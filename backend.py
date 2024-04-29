import sqlite3

def get_db_connection():
    return sqlite3.connect("database.db")

def start():
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("CREATE TABLE IF NOT EXISTS chans(id INTEGER PRIMARY KEY AUTOINCREMENT, link TEXT UNIQUE, name TEXT)")
    mydb.execute("CREATE TABLE IF NOT EXISTS requests(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, link TEXT, reason TEXT)")
    #mydb.execute("CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT, chan TEXT, title TEXT, body TEXT)")
    dbcon.commit()
    dbcon.close()

def makepost(chan, title, body):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute(f"INSERT INTO posts_{chan}(title, body) VALUES(?, ?)", (title, body))
    dbcon.commit()
    dbcon.close()

def makechan(link, name):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute(f"CREATE TABLE IF NOT EXISTS posts_{link}(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, body TEXT)")
    mydb.execute("INSERT INTO chans(link, name) VALUES (?, ?)", (link, name))
    dbcon.commit()
    dbcon.close()

def delchan(chan):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("DELETE FROM chans WHERE link = ?", (chan,))
    mydb.execute(f"DROP TABLE posts_{chan}")
    dbcon.commit()
    dbcon.close()

def delpost(chan, id):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute(f"DELETE FROM posts_{chan} WHERE id = ?", (id,))
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
    res = mydb.execute(f"SELECT * FROM posts_{chan}")
    posts = res.fetchall()
    dbcon.close()
    return reversed(posts)

def requestchan(name, link, reason):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    mydb.execute("INSERT INTO requests(name, link, reason) VALUES(?, ?, ?)", (name, link, reason))
    dbcon.commit()
    dbcon.close()
    
def getreq():
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    res = mydb.execute("SELECT * FROM requests")
    req = res.fetchall()
    dbcon.close()
    return req

def makeformchan(id):
    dbcon = get_db_connection()
    mydb = dbcon.cursor()
    res = mydb.execute("SELECT * FROM requests WHERE id = ?", (id,))
    req = res.fetchall()
    dbcon.close()
    info = list(req[0])
    makechan(link=info[2], name=info[1])