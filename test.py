from flask import Flask
from config import config

print config
app = Flask(__name__)

@app.route("/")
def hello():
    return "helloworld"

if __name__ == "__main__":
    app.run()
