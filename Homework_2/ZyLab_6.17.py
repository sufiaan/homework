"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 6.17
"""
password = input()
strong_password = ''

for item in password:
    if item == "i":
        item = item.replace("i", "!")
        strong_password += item
    elif item == "a":
        item = item.replace("a", "@")
        strong_password += item
    elif item == "m":
        item = item.replace("m", "M")
        strong_password += item
    elif item == "B":
        item = item.replace("B", "8")
        strong_password += item
    elif item == "o":
        item = item.replace("o", ".")
        strong_password += item
    else:
        strong_password += item

strong_password += "q*s"
print(strong_password)
