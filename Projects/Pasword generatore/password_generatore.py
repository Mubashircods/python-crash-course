from random import choice

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '12234567890'
symbols = '*&^%$#@!><~`'

chose_random = choice(upper)+choice(lower)+choice(numbers)+ \
                choice(symbols)+choice(symbols)
OTP_random = choice(upper)+choice(numbers)+choice(numbers)+ \
            choice(upper)+choice(numbers)

type = input("Which type of password you want to generate." \
            "\nChose one (OTP/Privicy): ")
if type == 'otp' or type == 'OTP':
    generate_otp =  choice(OTP_random)+choice(OTP_random)+ \
                    choice(OTP_random)+choice(OTP_random)+ \
                    choice(OTP_random)+choice(OTP_random)
    print(generate_otp)
elif type == 'privicy' or type == 'Privicy':
    password = choice(chose_random)+choice(chose_random)+choice(chose_random)+ \
                    choice(chose_random)+choice(chose_random)+choice(chose_random)+ \
                    choice(chose_random)+choice(chose_random)
    print(password)
else:
    print("Sorry, Invalid choice.")

    