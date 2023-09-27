# 1. In your own words, describe what a function is
"a function is a reusable block of code that only runs when its called"

# 2. What is are function parameters and arguments and describe
# the difference between the 2. 
# "function parameter is a place holder - goes in function definition"
# "function argument is the actual data - goes in function call"

# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
def welcome_msg(username):
    print('welcome '+ username + ' to coding class')
    
    welcome_msg('nahjell')

# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)
def calculate(randNumber, randomNumber2, randomNumber3):
    print(randNumber + randomNumber2 + randomNumber3)
    
    calculate(64, 73, 200)
    
    
# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.  

def userMsg(nextClass):
    Classname = input('what is your next class')
    print("you have" + nextClass + "after this")