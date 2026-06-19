p=input("enter the password:")
p=p.strip()
if len(p)<8:
    print("enter atleast 8 characters")
elif p.isalpha():
    print("password must have atleast one number")
elif p.islower():
    print("atleast one uppercase letter is required")
elif p.isupper():
    print("atleast one lowercase letter is required")
elif p.isalnum():
    print("atleast one special character is required")
else:
    print(f" {p} is a valid password")
