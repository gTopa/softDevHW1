from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "No Hablo queso"
@app.route("/hi")
def hello_world():
    return "Welcome"
@app.route("/bye")
def hello_world():
    return "Goodbye"

if __name__ == "__main__":
    app.run()
