def Max():
    my_list=[4,6,27,15,31,22,30,29,8,16]
    max_value = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
    print(f'Maximum no is: {max_value}')

Max()
