class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def play_with_dog(self, dog):
        if dog.friendly:
            self.happiness += 10
            print(f"{self.name} грається з собакою {dog.name}. Котик щасливий! ")
        else:
            self.happiness -= 10
            print(f"{self.name} намагається гратись з собакою {dog.name}, але та бурчить... ")

    def status(self):
        print(f"{self.name} — Щастя: {self.happiness}")


class Dog:
    def __init__(self, name, friendly=True):
        self.name = name
        self.friendly = friendly
        self.happiness = 50

    def play_with_cat(self, cat):
        self.happiness += 10
        print(f"{self.name} грається з котиком {cat.name}. Собака щасливий! ")

    def status(self):
        print(f"{self.name} — Щастя: {self.happiness}")


murko = Cat("Мурко")
rex = Dog("Рекс", friendly=True)

murko.status()
rex.status()

murko.play_with_dog(rex)
rex.play_with_cat(murko)


murko.status()
rex.status()