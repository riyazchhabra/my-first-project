print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0
if height>120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age? "))
    if age<=12:
        bill=5
        print("Child tickets are $5")
    elif age<=18:
        bill=7
        print("Youth tickets are $7")
    else:
        bill=10
        print("Adult tickets are $10")
    want_photo=input("Do you want to have photos while rollercoaster? Type 'y' for yes and 'n' for no.")
    if want_photo=='y':
        bill+=3
    elif want_photo=="n":
        bill=bill
    else:
        print("You typed wrong input")
    print(f"Your final bill is ${bill}")
        
else:
    print("You cannot ride the rollercoaster!")

input(print(" -------------------------------------------------------------------------"))

print("Welcome to Python Pizza Deliveries!")
bill=0
size=input("Which size of pizza would you prefer? 'S' for small 'M' for mediun 'L' for large: ")
pepperoni=input("Would you like pepperoni on your pizza? 'Yes' or 'No': ")
if size=="S":
    bill=15
    if pepperoni=="Yes":
        bill=+2
elif size=="M":
    bill=20
    if pepperoni=="Yes":
        bill+=4
elif size=="L":
    bill=25
    if pepperoni=="Yes":
        bill+=4
else:
    print("You typed wrong inputs")
cheese=input("Would you like extra cheese on your pizza? 'Yes' or 'No': ")
if cheese=="Yes":
    bill+=1
total_bill=print(f"Your total bill is ${bill}")
