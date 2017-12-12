"""
http://www.codeabbey.com/index/task_view/yacht-or-dice-poker
---------------------------------------------------------------
Dice game of Yacht is played with 5 standard dice (having from 1 to 6 points on their sides).
The player's goal is to gather some beautiful combination of points. Suppose, the following combinations are respected:

: two of dice have the same points, like 3 6 5 6 1 - called pair;
: three of dice have the same points, like 2 4 5 4 4 - called three;
: four of dice have the same points, like 1 4 1 1 1 - called four;
: all five dice have the same points, like 2 2 2 2 2 - called yacht;
: two pairs at once, like 3 6 5 3 5 - called two-pairs;
: pair and three at once, like 1 6 6 1 6 - called full-house;
: sequence from 1 to 5, like 2 4 3 5 1 - called small-straight;
: sequence from 2 to 6, like 6 3 4 2 5 - called big-straight.

>>Our goal is to write a program which for given combination of dice will determine its type.

Example:

input data: (error handling: should be number and 5 dice)
3
3 6 5 6 1
1 6 6 1 6
2 4 3 5 1

answer:
pair full-house small-straight

還差two pair and full house
"""

def dice_poker():
    play_times = int(input("Please input what times you played dice."))
    result_list = []
    for times in range(play_times):
        dice_list = input("Please input dice number sequentially separate by space").split()
        if len(dice_list) != 5:
            raise Exception
        for point in dice_list:
            if dice_list.count(point) == 2:
                result_list.append("Pair")
                break
            elif dice_list.count(point) == 3:
                result_list.append("Three")
                break
            elif dice_list.count(point) == 4:
                result_list.append("Four")
                break
            elif dice_list.count(point) == 5:
                result_list.append("Yacht")
                break
            elif sorted(dice_list) == [1, 2, 3, 4, 5]:
                result_list.append("Small-straight")
            elif sorted(dice_list) == [2, 3, 4, 5, 6]:
                result_list.append("Big-straight")

    print(' '.join(result_list))



dice_poker()


