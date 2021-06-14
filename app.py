from flask import Flask

app = Flask("Test")


@app.route("/")
def ping():
    return "pong"


# adding a new comment
# build one more time

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
