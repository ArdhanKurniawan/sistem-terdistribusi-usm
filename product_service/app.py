from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Product Service Running"


@app.route("/products")
def products():
    return {"products": ["Laptop", "Mouse", "Keyboard"]}


if __name__ == "__main__":
    app.run(port=5002)