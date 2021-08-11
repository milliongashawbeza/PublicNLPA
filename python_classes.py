class Dog:
    attr1= "dog"
    attr2="cat"

    def fun(self):
        print("I am a ",self.attr1)
        print("I am the second",self.attr2)
Rodger = Dog()
print(Rodger.attr1)
print(Rodger.attr2)
Rodger.fun()

class P:
    def __init__(self,name,age):
        self.name= name
        self.age= age
        print("The name of the p is",self.name)
        print("The age of the p is",self.age)
D = P("milli",2)

