"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 6.22
"""

# ax + by == c formula
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

solution = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            solution = True
            print(x, y)
if not solution:
    print("No solution")
