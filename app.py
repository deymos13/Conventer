from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# функция для получения курса валют с помощью API-запроса
def get_exchange_rates(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    rates = data['rates']
    return rates

# это главная страница для ввода данных, можно добавить разные валюты, помимо тех что используются здесь
@app.route('/')
def index():
    currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'RUB']
    return render_template('index.html', currencies=currencies)

# здесь происходит обработка формы с конвертацией
@app.route('/convert', methods=['POST'])
def convert():
    base_currency = request.form['base-currency']
    target_currency = request.form['target-currency']
    amount = float(request.form['amount'])

    rates = get_exchange_rates(base_currency) # тут мы получаем курсы валют

    if target_currency in rates:
        rate = rates[target_currency]
        converted_amount = amount * rate
        return render_template('result.html', base_currency=base_currency, target_currency=target_currency, amount=amount, converted_amount=converted_amount)
    else:
        return "Конверсия валюты невозможна."

if __name__ == '__main__':
    app.run(debug=True)