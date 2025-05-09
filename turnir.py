import random
import time

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(60, 100)
        self.strength = random.randint(10, 30)

    def attack(self, opponent):
        damage = random.randint(5, self.strength)
        opponent.health -= damage
        print(f"{self.name} б'є {opponent.name} на {damage} урону! (здоров’я {opponent.name}: {max(0, opponent.health)})")



def tournament(warrior1, warrior2):
    print(f"⚔️ Починається турнір між {warrior1.name} і {warrior2.name}!")
    print(f"{warrior1.name}: {warrior1.health} HP, сила: {warrior1.strength}")
    print(f"{warrior2.name}: {warrior2.health} HP, сила: {warrior2.strength}\n")

    round_num = 1
    while warrior1.health > 0 and warrior2.health > 0:
        print(f"\n Раунд {round_num}")
        warrior1.attack(warrior2)
        if warrior2.health <= 0:
            print(f"\n {warrior1.name} переміг!")
            break
        warrior2.attack(warrior1)
        if warrior1.health <= 0:
            print(f"\n {warrior2.name} переміг!")
            break
        round_num += 1
        time.sleep(1)  

warrior1 = Warrior("Аня")
warrior2 = Warrior("Оксана")
tournament(warrior1, warrior2)
