class myPet:
  name = 'unknown'
  species = 'unknown'
  age = 'unknown'

nick = myPet()
nick.name = "Nick"
nick.species = "dog"
nick.age = 10

simba = myPet()
simba.name = "Simba"
simba.species = "cat"
simba.age = 5

print(f"{nick.name} is my pet, he is a {nick.species} and is {nick.age} years old!\n{simba.name} is my pet, he is a {simba.species} and is {simba.age} years old!")

class myName:
    name = "unknow"
    def speak(self):
        print(f"Hello World! My name is {self.name}.")

alex = myName()
alex.name = "Alexandre"
alex.speak()

class myFriend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My friend's name is {self.name} and he is {self.age} years old!"

yuri = myFriend("Yuri", 30)
print(yuri)