a=input("Please enter the first name:")
b=input("Please enter the last name:")
c=int(input("Please enter the age:"))
d=input("Please enter the date of birth") #just year
print(f"User's information:\n{a}\n{b}\n{c}\n{d}")
UsersInformation=[]
UsersInformation.append(a)
UsersInformation.append(b)
UsersInformation.append(c)
UsersInformation.append(d)
if c < 18:
    print("You can't go out because it's dangerous")
else:
    print("You can go out to the street")