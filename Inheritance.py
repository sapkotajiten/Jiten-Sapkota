class Person:
    def __init__(self, name,age,cid_number):
        self.name=name
        self.age=age
        self.cid_number=cid_number
    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# creating objects
Person1 = Person("Jiten", 20, 11306002058)
Person2 = Person("Passang", 44, 11006001400)

# Accessing behaviors
Person1.walk()
Person2.sleep()

