from flask import Flask, request
import backend

app = Flask(__name__)

@app.route("/makepost", methods=['POST'])
def makepost():
    title = request.form.get("title")
    body = request.form.get("body")
    chan = request.form.get("chan")

    backend.makepost(chan=chan, title=title, body=body)
    
    return 'POST request received!'

@app.route("/")
def x():
    import requests

    # Specify the URL of your Flask server with the full address
    url = "http://localhost:5000/makepost"  # Change the port if your Fs lask server is running on a different port

    # Specify the data to be sent in the POST request
    data = {
        "title": "Sample Title",
        "body": "Sample Body",
        "chan": "2"  # Assuming chan is expected as a string in the backend
    }

    # Send the POST request
    response = requests.post(url, data=data)

    # Print the response from the server
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
