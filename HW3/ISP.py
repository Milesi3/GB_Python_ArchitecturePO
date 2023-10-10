from abc import ABC, abstractmethod


# Определение отдельных интерфейсов для различных действий

class FlyingAnimal(ABC):
    @abstractmethod
    def fly(self):
        pass


class SwimmingAnimal(ABC):
    @abstractmethod
    def swim(self):
        pass


# Реализация классов на основе определенных интерфейсов

class Bird(FlyingAnimal):
    def fly(self):
        print("A bird can fly")


class Fish(SwimmingAnimal):
    def swim(self):
        print("A fish can swim")


class Penguin(FlyingAnimal, SwimmingAnimal):
    def fly(self):
        print("A penguin can't fly")


if __name__ == '__main__':
    bird = Bird()
    bird.fly()

    fish = Fish()
    fish.swim()

    penguin = Penguin()
    penguin.fly()
    penguin.swim()
