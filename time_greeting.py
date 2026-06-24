a=int(input("Enter current hour     "))
b=int(input("Enter current minutes  "))
if a>=5 and a<12:
    print("Good Morning")
elif a>=12 and a<18:
    print("Good Afternoon")
elif a>=18:
    print("Good evening")
    