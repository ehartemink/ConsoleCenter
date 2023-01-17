from flask import Flask
import config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host=config.HOST, debug=config.DEBUG, port=config.PORT)
