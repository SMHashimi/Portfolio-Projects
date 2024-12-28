import random
from flask import Flask
app = Flask(__name__)
print(random.__name__)
# What is the name (__name__)?
@app.route("/")
def hello_world():
    return "Hello, Sayed!"
if __name__ == "__main__":
    app.run()

