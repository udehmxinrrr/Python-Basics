
class Animal: #"Animal" is called a base,super,or parent class, because attributes are being derived/borrowed from it.
    ismammal=True
    def speak(self):
        print("Animal is speaking")
    def move(self):
        print("Animal is moving")

class cat(Animal):      #This is inheritance; placing the name of another class into brackets in the name of the target class. Here, class cat is known as the child, derived or sub class.
    def sound(self):
        print("cat is meowing")
    def climb(self):
        print("cat is climbing a tree")

class horse:
    hasTail= True
    def neigh(self):
        print("horse is neighing")

a=Animal()
c=cat()
h=horse()