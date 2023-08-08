def main():
    my_string = "12345678994809"
    # print the above string at stepof 2
    print("Step indexing", my_string[::2])
    # print the above string starting from  index 1 at step size of 2
    print("Start stop and step ", my_string[1::2])
#   print the above string from index 1 at step size 3 till index 8
    print("Satrt stop step ", my_string[1:8:3])


if __name__ == '__main__':
    main()
