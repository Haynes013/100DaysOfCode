class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


#Fish inherites the attributes of Animal

class Fish(Animal):
    def __init__(self):
        super().__init__() # inherits from super class animal

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("moving in the water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
