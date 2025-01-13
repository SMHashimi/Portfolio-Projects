import random
from flask import Flask
app = Flask(__name__)
@app.route("/")
def higher_lower_game():
    return '<h1><b>Guess a number between 0 and 9</b></h1>' \
    '<img src = "https://cdn.pixabay.com/animation/2024/12/30/03/48/03-48-22-605_512.gif" width = 450 height = 340>'
"""
    Project: Create random integers from 0 to 9.
                        A user will guess a number,
                                   and the app will check 
                                               if the user choice is higher than the random,
                                                                            or not. 
"""
from_0_to_9 = random.randint(0, 9)
print(from_0_to_9)
@app.route("/<int:number>")
def play_game(number):
    if number == from_0_to_9:
        return '<h1><b>You found me!</b></h1>' \
        '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width = 450 height = 340>'
    elif number > from_0_to_9:
        return '<h1><b>Too high, try again!</b></h1>' \
        '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width = 450 height = 340>'
    else:
        return '<h1><b>Too low, try again!</b></h1>'\
        '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width = 450 height = 340>'
if __name__ == "__main__":
    app.run(debug = True)

