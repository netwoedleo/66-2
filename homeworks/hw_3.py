from abc import ABC, abstractmethod

# 🔹 Абстрактный родительский класс
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1
        print(f"Здоровье восстановлено. Текущее здоровье: {self.__health}")

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"{self.name}: Воин атакует мечом")

class Mage(Hero):
    def attack(self):
        print(f"{self.name}: Маг использует магию")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка")

warrior = Warrior("Артур", 5, 100, 15)
mage = Mage("Мерлин", 7, 60, 20)
assassin = Assassin("Эцио", 6, 80, 12)

heroes = [warrior, mage, assassin]

for hero in heroes:
    hero.greet()
    hero.attack()
    hero.rest()
    print("-" * 30)