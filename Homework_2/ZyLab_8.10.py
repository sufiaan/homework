"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 8.10
"""

name = input()

forward = ""
backward = ""

for letter in name:
    if letter != " ":
        forward += letter
        backward = letter + backward

if forward == backward:
    print(name, "is a palindrome")

else:
    print(name, "is not a palindrome")
