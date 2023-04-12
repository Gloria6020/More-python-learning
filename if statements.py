# if statement= ablock of code that will execute if its conditions is true
age=int(input("how old are you?: "))

if age == 100:
    print("you are a century old!")
elif age >= 18:
    print("you are an adult")
elif age < 0:
    print("you havent been born!")
else:
    print("you are a child!")
    