import string
import random
import time
import sys


letters = string.ascii_letters
digits = string.digits
characters = string.punctuation


while True:
    generator = letters + digits + characters
    ok = False
    esc = 0

    try:
        question_1 = int(input(
            '~~~~Choose the length of your password~~~~ \n'
            'Type: \n'
            '[1] for 6 characters\n'
            '[2] for 8 characters\n'
            '[3] for 10 characters\n'
            '[4] for 12 characters\n'
            '[5] to set a custom number\n'
        ))
    except ValueError as error:
        print('Error, try again')
        continue

    if question_1 == 1:
        esc = 6

    elif question_1 == 2:
        esc = 8

    elif question_1 == 3:
        esc = 10

    elif question_1 == 4:
        esc = 12

    elif question_1 == 5:
        try:
            question_2 = int(input('How many characters do you want?\n'))
            password = "".join(random.choices(generator, k=question_2))
            print(password)
        except ValueError as error2:
            print('Only numbers are allowed.')
            ok = True
            continue

    else:
        print('This is not a valid option, try again.')
        time.sleep(1)
        continue

    password = "".join(random.choices(generator, k=esc))
    print(password)

    time.sleep(1)

    while True:
        if not ok:
            question_3 = input(
                'Create a new password?\n'
                '[y] Yes\n'
                '[n] No\n'
            )

            if question_3 == 'n':
                sys.exit()
            elif question_3 == 'y':
                break
            else:
                print('That is an invalid answer, type only "s" or "n"')
                time.sleep(1)
                continue
        else:
            break
