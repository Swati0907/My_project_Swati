"""
Todo: Read about

Using files in python
    - different modes of opening files
    - read, write and append

Syntax: open('<file_path>', '<mode>') as file_handler:
            # use the file handler here

"""

import csv


if __name__ == '__main__':

    with open('./test.csv', 'r') as file_handler:
        reader = csv.reader(file_handler)

        data = []

        for row in reader:
            print(row)
            # create dict
            # append to the list

        

