

sun_is_out = False

if sun_is_out is True:
    print("do not turn on street lamps")
else:
    print("turn on street lamps")

#
    money_in_account = 10.00
    price_of_phone = 700.00

    if money_in_account > price_of_phone:
        print('congrats, you got the new phone')
    else:
        print("sorry, insufficient funds")

#write a function for a user password

user_password = 'password'


def login_password(user_password):
    user_password = input('please enter password')
    if user_password == 'password':
        print('welcome you are logged in')
    else:
        print('incorrect password')


# login_password()