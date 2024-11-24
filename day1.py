from common import *

def Day1():
    lines = getDayInput(1, False)
    total = 0

    for line in lines:
        lineOnlyNumbers = []
        for char in line:
            if char.isnumeric():
                lineOnlyNumbers.append(char)
        
        first = str(lineOnlyNumbers[0])
        last = str(lineOnlyNumbers[len(lineOnlyNumbers) - 1])
        combined = int(first + last)
        print(combined)
        total += combined

        print(total)

Day1()