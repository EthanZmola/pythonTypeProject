file = open("day1.txt")

first = 0
firstFound = False
last = 0
sum =0


for line in file:
    first
    firstFound = False
    last

    for letter in line:
        if letter.isdigit():
            last = letter
            if not firstFound:
                first=letter
                firstFound = True
    sum = sum + int(first + last)