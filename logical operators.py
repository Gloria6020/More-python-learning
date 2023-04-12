# logical operators(and, or,not)= used to check if two or more conditional statements is true

temp = int(input("what is the temperature outside?:"))

if not(temp>=0 and temp <= 30):
    print("the temp is good today")
    print("go outside")
elif  not(temp < 0 or temp >30):
    print("the temp is bad today")
    print("stay inside!")
