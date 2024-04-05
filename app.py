from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Bonjour ! Je suis Lynda BENKERROU"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
