from flask import Flask

app = Flask("Test")


@app.route("/")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
