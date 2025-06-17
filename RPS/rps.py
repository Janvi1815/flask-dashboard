from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user_choice = ""
    computer_choice = ""
    if request.method == "POST":
        choices = ["rock", "paper", "scissors"]
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose!"

    return render_template("rps.html", result=result, user_choice=user_choice, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(port=5005, debug=True)
