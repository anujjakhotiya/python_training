class student:
    def set_info(self,name,age):
        self.name=name
        self.age=age
    def give_info(self):
        print(self.name,":",self.age)
obj1=student()
obj2=student()
print(id(obj1))
print(id(obj2))
obj1.set_info("Alice",20)
obj2.set_info("Isobel",30)
obj1.give_info()
