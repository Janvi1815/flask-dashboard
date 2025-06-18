# dash.py
from flask import Flask, render_template, request
import threading
import os
import subprocess

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

ports = {
    "calculator":"https://calculator-a6be.onrender.com",
    "currency_converter":  "https://currency-converter-9oju.onrender.com",
    "form": 5003,
    "guessing_game": 5004,
    "rps": 5005,
    "quote": 5006,
    "flight": 5007
}

paths = {
    "calculator": "../calculator/calculator.py",
    "currency_converter": "https://currency-converter-9oju.onrender.com/",
    "form": "../form/app.py",
    "guessing_game": "../GUESSIN-GAME/guess.py",
    "rps": "../RPS/rps.py",
    "quote": "../random-quote-generator/quote_app/app.py",
    "flight": "../Flight Tacker/app.py"
}

working_dirs = {
    "calculator": "../calculator",
    "currency_converter": "../currency_converter",
    "form": "../form",
    "guessing_game": "../GUESSIN-GAME",
    "rps": "../RPS",
    "quote": "../random-quote-generator/quote_app",
    "flight": "../Flight Tacker"
}

@app.route("/")
def dashboard():
    app_name = request.args.get("app")
    url = None
    if app_name in ports:
        threading.Thread(target=lambda: subprocess.Popen(
            ["python", os.path.basename(paths[app_name])],
            cwd=working_dirs[app_name],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        ), daemon=True).start()
        url = f"http://127.0.0.1:{ports[app_name]}"
    return render_template("dash.html", iframe_url=url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ this makes it work on Render
    app.run(debug=True, host="0.0.0.0", port=port)
