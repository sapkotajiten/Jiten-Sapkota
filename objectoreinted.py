class dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

obj1=dog("domchu","golden",2)
obj2=dog("kitu","white",1)
obj3=dog("puppy","black",5)

print(f"{obj1.name} is {obj1.color} in color and is {obj1.age} years old!")
print(f"{obj2.name} is {obj2.color} in color and is {obj2.age} years old!")
print(f"{obj3.name} is {obj3.color} in color and is {obj3.age} years old!")