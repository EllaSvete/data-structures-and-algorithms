from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        if isinstance(animal, Cat):
            self.cats.enqueue(animal)


    def dequeue(self, choice):
        if choice == "dog" and self.dogs:
            return self.dogs.dequeue()
        if choice == "cat" and self.cats:
            return self.cats.dequeue()

class Dog:
    pass


class Cat:
    pass
