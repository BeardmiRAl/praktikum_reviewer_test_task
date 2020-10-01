import datetime as dt
"""неиспользуемый элемент импорта"""
import json

"""Должно быть 2 отступа, произведен только 1."""
class Record:
    def __init__(self, amount, comment, date=''):
        """Отсутствует пробел до и после знака равенства."""
        self.amount=amount
        """Длина строки превышает 79 символов."""
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        """Отсутствует пробел до и после знака равенства."""
        self.comment=comment
"""Отсутствуют отступы между объявлениями классов."""
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        """Отсутствует пробел до и после знака равенства."""
        self.records=[]
    """Отсутствуют отступы между объявлениями методов классов."""
    def add_record(self, record):
        self.records.append(record)
    """Отсутствуют отступы между объявлениями методов классов."""
    def get_today_stats(self):
        """Отсутствует пробел до и после знака равенства."""
        today_stats=0
        """Переменная Record объявлена с заглавной буквы"""
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                """Неоднородное исполнение кода. В методе описанном ниже использована
                конструкция +=."""
                today_stats = today_stats+Record.amount
        return today_stats
    """Отсутствуют отступы между объявлениями методов классов."""
    def get_week_stats(self):
        """Отсутствует пробел до и после знака равенства."""
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            """Логическое выражение может быть записано в виде двойного неравенства"""
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                """Отсутствует пробел до и после знака равенства."""
                week_stats +=record.amount
        return week_stats
"""Отсутствуют отступы между объявлениями классов."""
class CaloriesCalculator(Calculator):
    """Закомментированный код не в формате docstring"""
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        """Отсутствует пробел до и после знака равенства."""
        x=self.limit-self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
"""Отсутствуют отступы между объявлениями классов."""
class CashCalculator(Calculator):
    """Закомментированный код не в формате docstring"""
    USD_RATE=float(60) # Курс доллар США.
    """Закомментированный код не в формате docstring"""
    EURO_RATE=float(70) #Курс Евро.
    """Отсутствует отступ между атрибутами класса и объявлением методов классов.
    Переменные объявлены заглавными буквами"""
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        """Отсутствует пробел до и после знака равенства."""
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        """Отсутствует пробел до и после оператора сравнения."""
        if currency=='usd':
            cash_remained /= USD_RATE
            """Отсутствует пробел до и после знака равенства."""
            currency_type ='USD'
            """Отсутствует пробел до и после оператора сравнения."""
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            """Отсутствует пробел до и после знака равенства."""
            currency_type ='Euro'
            """Отсутствует пробел до и после оператора сравнения."""
        elif currency_type=='rub':
            """Лишняя строка, не оказывающая эффекта на выполнение кода."""
            cash_remained == 1.00
            """Отсутствует пробел до и после знака равенства."""
            currency_type ='руб'
        if cash_remained > 0:
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)
    """Отсутствует необходимость в методе. Полностью копирует метод родительского класса."""
    def get_week_stats(self):
        super().get_week_stats()
