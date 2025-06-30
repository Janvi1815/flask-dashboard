from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    rating = request.form.get("rating")
    comments = request.form.get("feedback")

    with open("feedback.txt", "a", encoding="utf-8") as file:
        file.write(f"Name: {name}\nRating: {rating}\nComments: {comments}\n{'-'*60}\n")

    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
