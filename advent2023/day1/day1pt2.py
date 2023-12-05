file = open("day1.txt")

first = 0
firstFound = False
last = 0
sum =0
nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
intNums = ["0","1","2","3","4","5","6","7","8","9"]
for line in file:
    first
    firstFound = False
    last

    # for letter in line:
    #     if letter.isdigit():
    #         last = letter
    #         if not firstFound:
    #             first=letter
    #             firstFound = True
    #     elif 
    for letter in range(len(line)):
        if line[letter].isdigit():
            last = line[letter]
            if not firstFound:
                first=line[letter]
                firstFound = True

        for words in range(len(nums)):
            if line[letter:letter+ len(nums[words])] == nums[words]:
                last = intNums[words]
                if not firstFound:
                    first = intNums[words]
                    firstFound = True
    print((first + last))
    sum = sum + int(first + last)


print(sum)