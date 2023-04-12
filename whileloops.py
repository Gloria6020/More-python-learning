# while loop= a statement  that will execute its block of code, as long as its condition remains true
# This code is asking the user to input their name and storing it in the variable `name`. The `while`
# loop is checking if the length of `name` is equal to 0 (meaning the user has not entered anything
# yet). If the length is 0, the loop will continue to prompt the user to enter their name until they
# do so. Once the user enters their name, the loop will exit and the program will print a greeting
# message with the user's name.
# This code is asking the user to input their name and storing it in the variable `name`. The `while`
# loop is checking if the length of `name` is equal to 0 (meaning the user has not entered anything
# yet). If the length is 0, the loop will continue to prompt the user to enter their name until they
# do so. Once the user enters their name, the loop will exit and the program will print a greeting
# message with the user's name.
name =""

while len(name)==0:
    name  = input("enter your name")  
    
print("hello "+name)

