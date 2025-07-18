# Control Flow with if / else and Conditional Operators
'''
if condition:
    do this
else:
    do this
'''

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

'''
if condition:
   if another condition:
      do this
   else:
     do this
else:
    do this
'''

print("Welcome to the rollercoaster")
height= int(input("What is your height in cm ? "))
if height > 120:
    print("You cant ride the rollercoaster")
    age = int(input("What is your age"))
    if age <= 18 :
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller")

#  if/elif/else

# if condition 1:
#    do A
# elif condition 2:
#     do B
# else:
#     do this



