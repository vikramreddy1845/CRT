'''for i in range(1,11):
    if i == 5:
        continue
    print(i)
    
   
count = 0
i = input("Enter password: ")
while i != "secret":
    print("Wrong password, try again.")
    i = input("Enter password: ")
    if i == "secret":
        print("Access granted.")
        print("You have successfully logged in.")
    count += 1
    if count == 3:
        print("Too many failed attempts. Access denied.")
        break
'''
p1 = "kohli"
for i in range(3):
    p2 = input("Enter password: ")
    if p2 == p1:
        print("Access granted.")
        break
    else:
        print("Access denied.")  