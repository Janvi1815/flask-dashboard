from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    result = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        button = request.form.get("button")

        if button == "=":
            try:
                result = str(eval(expression))
            except:
                result = "Error"
        elif button == "AC":
            expression = ""
            result = ""
        else:
            expression += button

    return render_template("calculator.html", expression=expression, result=result)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
