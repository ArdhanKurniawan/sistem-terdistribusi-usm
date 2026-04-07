from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "User Service Running"


@app.route("/users")
def users():
    return {"users": ["Admin", "User1", "User2"]}


if __name__ == "__main__":
    app.run(port=5001)