class student:
    school="SRU"
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def greet(self):
        print(f"Hello,I am {self.name} and I am {self.age} y/o from {self.dept} dept. ")   
s1=student("Anuj",20,"cse")
s2=student("Aryan",21,"ece")
print(s1.name)
print(s1.age)
print(s2.dept)
s1.greet()
s2.greet()
print(s1.school)
print(s2.school)