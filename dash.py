from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")

# Direct Render app links
render_urls = {
    "calculator": "https://calculator-a6be.onrender.com",
    "currency_converter": "https://currency-converter-9oju.onrender.com/",  # ⛔ update later
    "form": "https://form-3mxn.onrender.com/",
    "guessing_game": "https://your-guess-url.onrender.com",
    "rps": "https://rps-tyi7.onrender.com/",
    "quote": "https://your-quote-url.onrender.com",
    "flight": "https://your-flight-url.onrender.com"
}

@app.route("/")
def dashboard():
    app_name = request.args.get("app")
    iframe_url = render_urls.get(app_name, "")
    return render_template("dash.html", iframe_url=iframe_url)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
