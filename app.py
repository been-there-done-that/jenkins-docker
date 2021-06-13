from flask import Flask

app = Flask("Test")


@app.route("/")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run()
