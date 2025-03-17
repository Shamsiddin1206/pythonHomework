from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes a {self.sound} sound."

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    @abstractmethod
    def unique_behavior(self):
        pass


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "moo")

    def unique_behavior(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "cluck")

    def unique_behavior(self):
        return f"{self.name} is laying eggs."


class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "baa")

    def unique_behavior(self):
        return f"{self.name} is providing wool."


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the farm!")

    def farm_activities(self):
        for animal in self.animals:
            print(animal.make_sound())
            print(animal.eat())
            print(animal.sleep())
            print(animal.unique_behavior())
            print("-")


if __name__ == "__main__":
    my_farm = Farm()

    cow = Cow("AAA", 5)
    chicken = Chicken("BBB", 2)
    sheep = Sheep("SSS", 3)

    my_farm.add_animal(cow)
    my_farm.add_animal(chicken)
    my_farm.add_animal(sheep)

    print("\nFarm Activities:")
    my_farm.farm_activities()
