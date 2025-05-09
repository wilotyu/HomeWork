class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 50  
        self.hunger = 50  
        self.happiness = 50  

    def eat(self):
        print(f"{self.name} їсть.")
        self.hunger = max(0, self.hunger - 30)
        self.energy = min(100, self.energy + 10)

    def sleep(self):
        print(f"{self.name} спить.")
        self.energy = min(100, self.energy + 40)
        self.hunger = min(100, self.hunger + 20)

    def play(self):
        print(f"{self.name} грається.")
        if self.energy >= 20:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 20
            self.hunger += 10
        else:
            print(f"{self.name} занадто втомлений, щоб гратись.")

    def status(self):
        print(f"\nСтан котика {self.name}:")
        print(f"  Енергія: {self.energy}")
        print(f"  Голод: {self.hunger}")
        print(f"  Щастя: {self.happiness}")


murko = Cat("Мурко")
murko.status()
murko.eat()
murko.play()
murko.sleep()
murko.status()