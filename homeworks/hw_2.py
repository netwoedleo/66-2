import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, мой уровень: {self.level}.")

    def attack(self):
        print(f"{self.name} наносит базовый удар!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдохнул. Текущее здоровье: {self.health}")



class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} (Воин) атакует мечом!")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} (Маг) кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} (Ассасин) атакует исподтишка!")

warrior_obj = Warrior("Артур", 10, 150, 20, 100)
mage_obj = Mage("Гэндальф", 12, 80, 5, 200)
assassin_obj = Assassin("Эцио", 11, 100, 15, 80)

heroes_dict = {
    "Warrior": warrior_obj,
    "Mage": mage_obj,
    "Assassin": assassin_obj
}

print("--- Добро пожаловать в битву героев! ---")
user_choice = input("Выберите героя (Warrior / Mage / Assassin): ").capitalize()

if user_choice in heroes_dict:
    available_enemies = ["Warrior", "Mage", "Assassin"]
    ai_choice = random.choice(available_enemies)

    player = heroes_dict[user_choice]
    enemy = heroes_dict[ai_choice]

    print(f"\nВы выбрали: {user_choice}")
    print(f"Противник: {ai_choice}")

    player.attack()
    enemy.attack()
    print("-" * 30)

    if user_choice == ai_choice:
        print("Ничья! Герои разошлись миром.")
    elif (user_choice == "Warrior" and ai_choice == "Assassin") or \
            (user_choice == "Assassin" and ai_choice == "Mage") or \
            (user_choice == "Mage" and ai_choice == "Warrior"):
        print(f"Результат: {user_choice} победил!")
    else:
        print(f"Результат: {ai_choice} победил!")
else:
    print("Ошибка: такого героя не существует.")