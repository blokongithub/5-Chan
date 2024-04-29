from flask import Flask, request, render_template
import backend
import hashlib

app = Flask(__name__)

@app.route("/makepost", methods=['GET', 'POST'])
def makepost():
    if request.method == "POST":
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
    else:
        return render_template("makepost.html")


@app.route("/makechan", methods=["GET","POST"])
def makechan():
    if request.method == "POST":
        link = request.form.get("link")
        name = request.form.get("name")
        
        devpassword = request.form.get("secret")
        password = hashlib.md5(devpassword.encode())
        password = password.hexdigest()
        if password == "e0d1e169daaa03df020a8aa6172becd0":
            backend.makechan(link=link, name=name)
            return "chan has been made"
        else:
            return "back off hacker"
    else:
        return render_template("create_chan.html")
    
@app.route("/delchan", methods=["GET", "POST"])
def delchan():
    if request.method == "POST":
        chan = request.form.get("chan")
        
        devpassword = request.form.get("secret")
        password = hashlib.md5(str(devpassword).encode())
        password = password.hexdigest()
        if password == "e0d1e169daaa03df020a8aa6172becd0":
            backend.delchan(chan=chan)
            return "chan has been deleted"
        else:
            return str(password)
    else:
        return render_template("delete_chan.html")

@app.route("/chan/<chan>")
def fetchchan(chan):
    
    data = backend.getposts(chan=chan)
    chans = backend.getchansid()
    print(chan, chans)
    if chan in chans:
        return render_template("chan.html", posts=data, chan=backend.chanidtoname(chan))
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

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/requestchan", methods=["GET", "POST"])
def requestchan():
    if request.method == "GET":
        return render_template("requestchan.html")
    else:
        name = request.form.get("name")
        link = request.form.get("link")
        reason = request.form.get("reason")
        backend.requestchan(name, link, reason)
        return ("chan requested")

@app.route("/acceptchan", methods=["GET", "POST"])
def acceptchan():
    if request.method == "GET":
        res=backend.getreq()
        return render_template("requestsubmissions.html", req=res)
    else:
        devpassword = request.form.get("password")
        password = hashlib.md5(devpassword.encode())
        password = password.hexdigest()
        if password == "e0d1e169daaa03df020a8aa6172becd0":
            id = request.form.get("id")
            backend.makeformchan(id)
            return "made chan"
        else:
            return "back off hacker"
    
if __name__ == '__main__':
    backend.start()
    app.run(debug=True)
