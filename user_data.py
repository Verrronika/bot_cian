from dataclasses import dataclass


@dataclass
class UserData:
    rooms: int = 0
    max_price: int = 0
    okrug: str = ""
    district: str = ""
    salary: int = 0
    first_payment: int = 0

    def set_rooms(self, num):
        self.rooms = num

    def set_max_price(self, price):
        self.max_price = price

    def set_okrug(self, okrug):
        self.okrug = okrug

    def set_district(self, district):
        self.district = district

    def set_salary(self, salary):
        self.salary = salary

    def set_first_payment(self, payment):
        self.first_payment = payment
