# 1. What is the difference between 
# a parameter and an argument in a python function
'parameter is a place holder'

# 2. In your own words, describe what 
# a conditional statement (if/else) is 

"Use if to specify a block of code to be executed, if a specified condition is true"
"Use else to specify a block of code to be executed, if the same condition is false"

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )

if - "executes a specific block of code if a condition is met"


# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

def put_food_in_the_refridgerator(food_in_refridgerator):
    if  food_in_refridgerator==True:
        print('time to cook')
    else:
        print('time to shop')

put_food_in_the_refridgerator(True)

# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

def cereal_inventory(cereal):
    current_cereal_inventory= 10
    if cereal >= current_cereal_inventory:
        print("inventroy is full")
    else:
        print("need to order more cereal")