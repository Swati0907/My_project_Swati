def my_list():
    first_list = [1, 2, 3, 4, 5]
    print(first_list[2])  # printing the element at second index of list
    second_list = [10, 20, 30, 40]
    print(first_list + second_list)  # printing adding two list
    first_list[0] = 50  # replacing the value at 0th index of list
    print(first_list[0:])
    first_list.append('90')  # appending one more value to the first list
    print(first_list + second_list)
    print(first_list)
    first_list.pop() # removing value from end of the list
    print(first_list)
    popped_list= first_list.pop(2)# removing value from 2nd index  of the list
    print(popped_list)
    print(first_list)




if __name__ == '__main__':
    my_list()
