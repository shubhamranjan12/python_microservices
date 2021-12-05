from flask import Flask
from producer import publish

app = Flask(__name__)

@app.route("/")
def hello_world():
    publish({'hello': 'world'})
    return "<p>Service-1: Hello, World!</p>"

#app.run(debug=True, port=8081)