from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/upcoming")
def upcoming():
    return render_template("upcoming.html")

if __name__ == "__main__":
    app.run(debug =True)
