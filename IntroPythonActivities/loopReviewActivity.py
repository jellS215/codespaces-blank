# Write a loop that will work for these three scenarios

# Passcode loop - write a program that will check
# if a passcode is correct. While the passscode is not correct
# Ask the user to try again. User gets 4 attempts

passcode = 2156
i= 0
while i <= 4:
    print(1)
    if i==4:
        break
    i+=1

# continue
def continueExample():
    i=0
    while i <= 8:
        i+=1
        if i==5:
            print('skip the number 5.')
            continue
        print(i)
        
