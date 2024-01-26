import time
import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yeet1234!",
    auth_plugin='mysql_native_password',
    database="chanclone"
)
mycursor = mydb.cursor()

def makepost(title, body, chan):
    mycursor.execute("INSERT INTO `chanclone`.`posts` (`id`, `boardID`, `title`, `body`, `timestamp`) VALUES ('" + str(random.randint(1,1000000000000000)) + "', '" + str(chan) + "', '" + title + "', '" + body +"', '"+ str(time.time()) + "');")
    mydb.commit()
def makechan(link, name, private="0", code="0"):
    mycursor.execute("INSERT INTO `chanclone`.`chans` (`id`, `hlink`, `name`, `isPrivate`, `password`) VALUES ('" + str(random.randint(1,1000000000000000)) + "', '" + link + "', '" + name + "', '" + private +"', '"+ code + "');")
    mydb.commit()
    