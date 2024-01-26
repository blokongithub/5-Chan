import time

def makepost(title, body, chan):
    post = {
        "Title": title,
        "Body": body,
        "Date": round(time.time())
    }
    
def makechan(id, name, private=False, code=None):
    print("todo")