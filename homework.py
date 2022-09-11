#!/usr/bin/python
# -*- coding: cp1251 -*-

import datetime as dt


def convert_time(time):
    date_format = '%d.%m.%Y'
    moment = dt.datetime.strptime(time, date_format)
    return moment.date()


class Record():
    today = dt.datetime.now().date()
    def __init__(self, amount=0, date='1.01.1970', comment=''):
        self.amount = amount
        self.comment = comment
        if date == '1.01.1970':
            self.date = dt.datetime.now().date()
        else:
            self.date = convert_time(date)


class Calculator():
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, rec):
        self.records.append(rec)


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def add_record(self, rec):
        return super().add_record(rec)

    def get_today_stats(self):
        current = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if record.date == today:
                current += record.amount
        print(f'Сегодня съедено {current} кКал')

    def get_calories_remained(self):
        cal = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if record.date == today:
                cal += record.amount
        if cal < self.limit:
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью \
            не более {self.limit - cal} кКал')
        else:
            print('Хватит есть!')

    def get_week_stats(self):
        cal = 0
        today = dt.datetime.now().date()
        start_wk = (dt.datetime.now() - dt.timedelta(days=7)).date()

        for record in self.records:
            if start_wk < record.date <= today:
                cal += record.amount
        print(f'Калорий получено за последние 7 дней: {cal} кКал')


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def add_record(self, rec):
        return super().add_record(rec)

    def get_today_stats(self, cur):
        current = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if record.date == today:
                current += record.amount
        print(f'Сегодня потрачено {current} {cur}')

    def get_today_cash_remained(self, cur):
        cash_spent = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if record.date == today:
                cash_spent += record.amount
        if cash_spent < self.limit:
            print(f'На сегодня осталось {self.limit - cash_spent} {cur}')
        elif cash_spent == self.limit:
            print('Денег нет, держись')
        else:
            print(f'Денег нет, держись: твой долг - {cash_spent - self.limit} {cur}')

    def get_week_stats(self, cur):
        cash_spent = 0
        today = dt.datetime.now().date()
        start_wk = (dt.datetime.now() - dt.timedelta(days=7)).date()

        for record in self.records:
            if start_wk < record.date <= today:
                cash_spent += record.amount
        print(f'Денег портачено за последние 7 дней {cash_spent} {cur}')


today = '11.09.2022'  # format day.month.year

r1 = Record(100, today, 'Candies')
r2 = Record(20000, today, 'Meat')
r3 = Record(400, '08.09.2022', 'Cake')

cash = CashCalculator(500)

cash.add_record(r1)
cash.add_record(r2)
cash.add_record(r3)

cash.get_today_stats('$')
cash.get_today_cash_remained('$')
cash.get_week_stats('$')

cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="cofee"))
cash_calculator.add_record(Record(amount=300, comment="launch for friend"))
cash_calculator.add_record(Record(amount=3000, comment="Pub in Tanya\'s birthday", date="08.11.2019"))

cash_calculator.get_today_cash_remained('rub')

print("==========================")

calories = CaloriesCalculator(500)

calories.add_record(r1)
calories.add_record(r2)
calories.add_record(r3)

calories.get_today_stats()
calories.get_calories_remained()
calories.get_week_stats()