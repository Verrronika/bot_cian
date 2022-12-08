from user_data import UserData
import math


def count_credit(user_data: UserData):
    rest_payment = user_data.max_price - user_data.first_payment
    month = math.ceil(rest_payment / user_data.salary)
    return [month // 12, month % 12]
