'''try:
    contact=int(input("Enter your contact number: \t"))
except ValueError:
    print("Enter contact number in integer. Your input is invalid!!")
else:
    print(f"We will contact you on : {contact}")
finally:
    print("Algo ended")'''

try:
    a=int(input("Enter the first number: \n"))
    b=int(input("Enter the secind number: \n"))
except ValueError:
    print("Invalid input!!")
except ZeroDivisionError:
    print("b cannot be 0")
else:
    print(f"Your answer is {a/b}")
    
                