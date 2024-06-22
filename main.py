import requests


def convert_currency(amount, from_currency, to_currency):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    data = response.json()


    if "error" not in data:
        exchange_rate = data["rates"][to_currency]

        converted_amount = amount * exchange_rate

        return converted_amount
    else:
        raise Exception("Ошибка при получении курса обмена валют")


amount = int(input('Введите сумму: '))
from_currency = input('Из какой валюты: ')
to_currency = input('В какую валюту: ')

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")