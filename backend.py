import random
import sqlite3
import os

dbcon = sqlite3.connect("database.db")
mydb = dbcon.cursor()

def start():
    mydb.execute("CREATE TABLE IF NOT EXISTS chans(id INTEGER PRIMARY KEY AUTOINCREMENT, link TEXT, name TEXT, isprivate INTEGER, password TEXT)")
    mydb.execute("CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT, chan INTEGER, title TEXT, body TEXT)")
    dbcon.commit()
    
def deldb(filename):
    os.remove(filename)
    

def makepost(chan, title, body):
    mydb.execute("INSERT INTO posts(chan, title, body) VALUES(?, ?, ?)", (chan, title, body))
    dbcon.commit()

def makechan(link, name, private="0", code="0"):
    mydb.execute("INSERT INTO chans(link, name, isprivate, password) VALUES (?, ?, ?, ?)", (link, name, private, code))
    dbcon.commit()
    
def delchan(id):
    mydb.execute("DELETE FROM chans WHERE id = ?", (id,))
    dbcon.commit()
    
def delchan(id):
    mydb.execute("DELETE FROM posts WHERE id = ?", (id,))
    dbcon.commit()
    
def panicattack():
    mydb.execute("DROP TABLE chans")
    mydb.execute("DROP TABLE posts")
    dbcon.commit()