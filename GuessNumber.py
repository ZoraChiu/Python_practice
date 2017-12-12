"""
Error Handling: type error, 邊界值
"""


from random import randint

def guess_number():
    ans = randint(1, 100)
    print(ans)# for testing purpose
    interval = [1, 100]
    restart = True
    while restart:
        try:
            user_input = int(input("Please input a number" + str(interval)))
            if user_input < interval[0] or user_input > interval[1]:
                raise ValueError
            elif user_input > ans:
                interval[1] = user_input
                print("Wrong number, please input a number again", interval)
            elif user_input < ans:
                interval[0] = user_input
                print("Wrong number, please input a number again", interval)
            else:
                print("You Won")
                restart = False
        except TypeError:
            print("Please input an integer")
            restart = True
        except ValueError:
            print("Please input a number during", interval)
            restart = True

guess_number()


