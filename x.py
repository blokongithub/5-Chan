import requests

# Specify the URL of your Flask server
url = "http://localhost:5000/makepost"  # Change the port if your Flask server is running on a different port

# Specify the data to be sent in the POST request
data = {
    "title": "Sample Title",
    "body": "Sample Body",
    "chan": 2
}

# Send the POST request
response = requests.post(url, data=data)

# Print the response from the server
print(response.text)
