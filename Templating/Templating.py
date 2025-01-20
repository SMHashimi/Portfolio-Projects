from flask import Flask, render_template
from requests import *
app = Flask(__name__)
NPOINT_API = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route("/")
def home():
    blogs_npoint = get(url = NPOINT_API).json()
    return render_template("index.html", blogs = blogs_npoint)

@app.route("/post/<num>")
def get_post(num):
    blogs_npoint = get(url = NPOINT_API).json()
    return render_template("post.html", blogs = blogs_npoint, Number = int(num))
if __name__ == "__main__":
    app.run(debug=True)