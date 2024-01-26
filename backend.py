import time
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="4chan",
  password="Epic4chan"
)

def makepost(title, body, chan):
    post = {
        "Title": title,
        "Body": body,
        "Date": round(time.time())
    }
    
def makechan(id, name, private=False, code=None):
    print("todo")