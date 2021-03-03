"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 9.10
"""

import csv

csv_file = input()
my_dict = {}

with open(csv_file) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # print(row)
        for content in row:
            # print(content)

            if content in my_dict:
                my_dict[content] = my_dict[content] + 1

            else:
                my_dict[content] = 1

# print(my_dict)

for keys,values in my_dict.items():
    print(keys, values)
