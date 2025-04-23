from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "welcom to home page"

@app.route("/product")
def product():
    return "all products are here btw"


if __name__=="__main__":
    app.run(debug=True)