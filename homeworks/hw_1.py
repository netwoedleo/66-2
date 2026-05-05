class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


hero1 = Hero("Алихан", 5, 10, 7)
hero2 = Hero("Эмир", 3, 8, 6)

hero1.greet()
hero1.attack()
hero1.rest()
print("После действий:", hero1.health, hero1.strength)

print("-----")

hero2.greet()
hero2.attack()
hero2.rest()
print("После действий:", hero2.health, hero2.strength)