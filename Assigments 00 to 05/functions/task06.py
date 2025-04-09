# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def check_num(num):
    for i in num:
        if i % 2 == 0:
            print(f"{i} even",end = " ")
        else:
            print(f"{i} odd",end = " ")


lst = []

while True:
    usr = input("Enter Number: ")
    if usr.lower() == "stop":
        break
    if usr.isdigit():
        lst.append(int(usr))
    else:
        print("Invalid Input!")

check_num(lst)




