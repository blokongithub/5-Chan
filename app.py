from flask import Flask, request, render_template
import backend

app = Flask(__name__)


@app.route("/makepost", methods=['POST'])
def makepost():
    title = request.form.get("title")
    body = request.form.get("body")
    chan = request.form.get("chan")
    
    backend.makepost(chan=chan, title=title, body=body)
    
    return 'post has been made'

@app.route("/makechan")
def makechan():
    link = request.form.get("link")
    name = request.form.get("name")
    private = request.form.get("private")
    code = request.form.get("password")
    
    backend.makechan(link=link, name=name, private=private, code=code)
    
    return "chan has been made"

@app.route("/chan")
def fetchchan():
    
    data = backend.getposts("test")
    return render_template("chan.html", posts=data)

if __name__ == '__main__':
    backend.start()
    app.run(debug=True)
