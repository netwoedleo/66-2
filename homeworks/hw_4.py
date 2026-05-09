rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def __add__(self, other):
        if isinstance(other, Money):
            total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
            return Money(total_kgs, "KGS")
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
            return Money(total_kgs, "KGS")
        return NotImplemented

    def __mul__(self, number):
        if isinstance(number, (int, float)):
            return Money(self.amount * number, self.currency)
        return NotImplemented

    def __truediv__(self, number):
        if isinstance(number, (int, float)):
            if number == 0:
                raise ZeroDivisionError("На ноль делить нельзя!")
            return Money(self.amount / number, self.currency)
        return NotImplemented

    def __str__(self):
        return f"{self.amount} {self.currency}"


money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result_add = money1 + money2
print(f"Сложение: {result_add}")

result_sub = money1 - money2
print(f"Вычитание: {result_sub}")

result_mul = money1 * 3
print(f"Умножение (100 USD * 3): {result_mul}")

result_div = money2 / 2
print(f"Деление (5000 KGS / 2): {result_div}")