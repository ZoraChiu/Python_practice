"""
http://www.codeabbey.com/index/task_view/weighted-sum-of-digits
wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60

:不知如何將amount印在同一行不以list表示

Error Handling: type error, 數量不符, 輸入數字時錯誤或打成英文
"""


def wsd():
    try:
        times = int(input("Please input how many numbers do you want to calculate"))
        if times <= 0:
            raise Exception
        user_number = input("Please input all numbers sequentially and separate by space")
        user_number_list = user_number.split()
        if len(user_number_list) != times:
            raise Exception
        each_amount = 0
        amount_list = []
        position = 1
        for j in user_number_list:
            for k in j:
                each_amount += int(k) * position
                position += 1
            amount_list.append(each_amount)
            each_amount = 0  # reset
            position = 1  # reset
        print(amount_list)
    except TypeError:
        print("Please input integers")
    except Exception:
        print("Please check your input, there may be something wrong.")



wsd()



