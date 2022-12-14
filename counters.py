import pandas as pd
from user_data import UserData


def count_credits(user_data: UserData):
    result = []
    data = pd.read_csv('bank.csv')
    for index, item in data.iterrows():
        credit_size = user_data.max_price - user_data.first_payment
        if item['term'] == user_data.years and 0 <= item['sum'] - credit_size < 1000000:
            result.append([item['name'], item['pecentage'], item['image']])
    return result
