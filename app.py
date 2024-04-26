from flask import Flask, request, render_template
import backend
import hashlib

app = Flask(__name__)


@app.route("/makepost", methods=['POST'])
def makepost():
    title = request.form.get("title")
    body = request.form.get("body")
    chan = request.form.get("chan")
    chans = backend.getchansid()
    print(chans)
    if chan not in chans:
        return render_template("invalid_chan.html")
        print(chans)
    else:
        backend.makepost(chan=chan, title=title, body=body)
        return render_template("posted.html", chan=chan)

@app.route("/makepost")
def postget():
    return render_template("makepost.html")


@app.route("/makechan", methods=["POST"])
def makechan():
    link = request.form.get("link")
    name = request.form.get("name")
    private = request.form.get("private")
    code = request.form.get("password")
    
    devpassword = request.form.get("secret")
    
    if devpassword == "5chanclone1234!":
        backend.makechan(link=link, name=name, private=private, code=code)
        ret = "chan has been made"
    else:
        ret = "back off hacker"
        
    return ret

@app.route("/delchan", methods=["POST"])
def delchan():
    chan = request.form.get("chan")
    
    devpassword = request.form.get("secret")
    
    if devpassword == "5chanclone1234!":
        backend.delchan(chan=chan)
        ret = "chan has been deleted"
    else:
        ret = "back off hacker"
        
    return ret

@app.route("/chan/<chan>")
def fetchchan(chan):
    
    data = backend.getposts(chan=chan)
    chans = backend.getchansid()
    if chan in chans:
        return render_template("chan.html", posts=data, chan=chan)
    else:
        return "Chan does not exist"

@app.route("/")
def indexy():
    data = backend.getchans()
    return render_template("index.html", chans=data)

@app.route("/index")
def indexy2():
    data = backend.getchans()
    return render_template("index.html", chans=data)


if __name__ == '__main__':
    backend.start()
    app.run(debug=True)
