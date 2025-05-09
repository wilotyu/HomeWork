class Pet:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_birthday_year(self):
        return self.birth_year



class Dog(Pet):
    def __init__(self, name, birth_year, breed):
        super().__init__(name, birth_year)  
        self.breed = breed

    def get_breed(self):
        return self.breed



my_dog = Dog(name="Sam", birth_year=2020, breed="Golden Retriever")


print(f"Ім'я собаки: {my_dog.name}")
print(f"Рік народження собаки: {my_dog.get_birthday_year()}")
print(f"Порода собаки: {my_dog.get_breed()}")