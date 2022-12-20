import pandas as pd
from user_data import UserData


def month_payment(percentage, sum, term):
    r = percentage / 1200.0
    ak = (r * (1 + r) ** term) / (((1 + r) ** term) - 1)
    mp = sum * ak
    total = mp * term
    return round(mp, 2)


def count_credits(user_data: UserData):
    result = []
    data = pd.read_csv('bank.csv')
    for index, item in data.iterrows():
        credit_size = user_data.max_price - user_data.first_payment
        if item['term'] == user_data.years and 0 <= item['sum'] - credit_size < 1000000:
            percentage = float(item['pecentage'][3:-1].replace(',', '.'))
            sum = int(item['sum'])
            payment = month_payment(percentage, sum, item['term'])
            print(sum, payment)
            result.append([item['name'], item['pecentage'], f'Месячный платеж: {payment} рублей'])
    return result
