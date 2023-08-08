
def change_and_print_list(val):
    val[1] = 9
    print('Modified:', val)


def change_and_print_string(val):
    val = val + ' extra'
    print('Modified:', val)


def num_list():
    l1 = [0, 1, 2, 3, 4]
    change_and_print_list(l1.copy())
    print('Original:', l1)

    s1 = 'hello'
    change_and_print_string(s1)
    print('Original:', s1)



if __name__ == '__main__':
    num_list()
