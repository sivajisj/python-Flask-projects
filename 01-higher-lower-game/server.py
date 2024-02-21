import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route("/")
def hello():
    return """
    <div style="text-align: center;">
        <h1>Guess a number between 0 and 9</h1>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' height=300 width=400 />
    </div>
    """

@app.route("/<int:num>")
def check_num(num):
    if num == random_number:
        return """
        <div style="text-align: center;">
            <h1 style='color:green;'>Correct Answer, You found me</h1>
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' height=300 width=400 />
        </div>
        """
    elif num > random_number:
        return """
        <div style="text-align: center;">
            <h1 style='color:orange;'>Number is too high, Try again</h1>
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' height=300 width=400 />
        </div>
        """
    else:
        return """
        <div style="text-align: center;">
            <h1 style='color:red;'>Number is too low, Try again</h1>
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' height=300 width=400 />
        </div>
        """

if __name__ == '__main__':
    app.run(debug=True)
