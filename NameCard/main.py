from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    """
    In the below html (angela.html),
        there is an image of angela. However, the
                    Flask is not able to load the image.
                            As a result, we need to serve Static Files.
    """
    """
    In Flask application, 9 out of 10 times,
                          you need to create those
                                   static & templates files. 
    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug = True)