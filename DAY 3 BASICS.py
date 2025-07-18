# Control Flow with if / else and Conditional Operators

# Note : with else we did not write condition it is just blank 

# Logical Operators

# A and B , C or D , not E
# and it returns TRUE if both condition true
# or it returns TRUE if one condition true
# not It is used to reverse the result of a condition

'''
if condition:
    do this
else:
    do this
'''

# if condition & condition2 & condition3:
#     do this
# else:
#     do this

print("Welcome to the rollercoaster")
height= int(input("What is your height in cm ? "))
if height > 120:
    print("You cant ride the rollercoaster")
else:
    print("Sorry you have to grow taller")

# Introducing the Modulo (Operator)

# Modulo Operator give us remainder after divison
# 10 % 5 = 0

# Excercise to Check odd and even number
a = int(input("Enter the value to check \n it is odd or even"))
b = a % 2
if b == 0 :
    print("it is even number")
else:
    print("it is odd number")


#  Nested if statements and elif statements

#  Nested if statements and elif statements

'''
if condition:
   if another condition:
      do this
   else:
     do this
else:
    do this
'''
#  if/elif/else

# if condition 1:
#    do A
# elif condition 2:
#     do B
# else:
#     do this


print("Welcome to the rollercoaster")
height= int(input("What is your height in cm ? "))
if height > 120:
    print("You cant ride the rollercoaster")
    age = int(input("What is your age"))
    if age<= 12:
        print("Please pay $5")
    elif age <= 18 :
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller")

# Multiple If Statements in Succession
# Fun Fact : we use it in same indentation as our if/elif/else statements
# Indentation is very very important always keep in mind

# if condition1:
#    do A
# if condition2:
#    do B
# if condition3:
#    do C

print("Welcome to the rollercoaster")
height= int(input("What is your height in cm ? "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age"))
    if age<= 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18 :
        bill = 7
        print("Youth ticket is $7.")
    else:
        bill = 12
        print("Adult ticket is $12")

    want_photo = input("Do you want to have a photo take? Type y for yes and n for No.")
    if want_photo == "y" :
        # Add 3$ to the bill
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry you have to grow taller")




