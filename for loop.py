# for loop= a statement that will execute its block of codes a limited amount of time
            #while loop= is unlimited that until the statement is false then it will continue with the programm
            #for loop= limited
            
# `for i in range(10):` is creating a for loop that will iterate 10 times. During each iteration, the
# variable `i` will take on a value from 0 to 9 (inclusive), and the code block below the loop will be
# executed. In this case, the code block is simply printing the value of `i+1` during each iteration.
"""for i in range(10):
    print(i+1)"""
    
"""for int in range(50,100+1,2):
   print (int)"""
   
"""for i in "gloria cherop":
    print(i)"""
    
    
# `import time` is importing the built-in Python module `time`, which provides various time-related
# functions. In this specific code, it is used to pause the execution of the program for one second
# between each iteration of the for loop.
import time


for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)  
print("happy new year")  
