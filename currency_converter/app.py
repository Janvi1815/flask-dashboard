from flask import Flask, render_template, request

app = Flask(__name__)

conversion_rates = {
    'USD': {'INR': 83.2, 'EUR': 0.93, 'GBP': 0.79, 'JPY': 155.2, 'CAD': 1.36, 'AUD': 1.51, 'CHF': 0.91},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095, 'JPY': 1.87, 'CAD': 0.016, 'AUD': 0.015, 'CHF': 0.011},
    'EUR': {'USD': 1.07, 'INR': 89.5, 'GBP': 0.85, 'JPY': 166.5, 'CAD': 1.46, 'AUD': 1.62, 'CHF': 0.98},
    'GBP': {'USD': 1.26, 'INR': 105.2},
    'JPY': {'USD': 0.0064, 'INR': 0.53},
    'CAD': {'USD': 0.74, 'INR': 61.2},
    'AUD': {'USD': 0.66, 'INR': 55.1},
    'CHF': {'USD': 1.1, 'INR': 93.8},
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        if from_currency == to_currency:
            result = amount
        else:
            rate = conversion_rates.get(from_currency, {}).get(to_currency, 1)
            result = round(amount * rate, 2)

    return render_template('currency.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,port=5002)
