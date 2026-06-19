p=input("enter the password:").strip()
score=0
if len(p)>=8:
    score+=1
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False
    for char in p:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif char not isalnum():
            has_special=True 
    if has_upper == True:
        score+=1
    if has_lower == True:
        score+=1
    if has_digit == True:
        score+=1
    if has_special == True:
        score+=1
    if score<5:
        print("password is weak")
    else:
        print("password is strong")