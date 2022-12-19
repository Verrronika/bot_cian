import pandas as pd
from locale import atof

def month_payment(percentage, sum, term):
    r = percentage / 1200.0
    ak = (r * (1 + r) ** term) / (((1 + r) ** term) - 1)
    mp = sum * ak
    total = mp * term
    return round(mp, 2)

result = []
data = pd.read_csv('bank.csv')

for index, item in data.iterrows():
    percentage = float(item['pecentage'][3:-1].replace(',', '.'))
    sum = int(item['sum'])
    payment = month_payment(percentage, sum, item['term'])
    print(sum, payment)
    result.append([item['name'], item['pecentage'], item['image'], payment])