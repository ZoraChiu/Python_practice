def bubble_sort(b_list):
    for i in range(len(b_list)-1):
        for j in range(len(b_list)-1):
            if b_list[j] > b_list[j+1]:
                b_list[j], b_list[j+1] = b_list[j+1], b_list[j]
    print(b_list)

# reason for out of range:loop till the final element, there's no b_list[i+1], so that range must be (len(b_list)-1)
# why the if statement index is j?



a = [-2, -8, 20, 8, 3, -20, 100, 2]


bubble_sort(a)

