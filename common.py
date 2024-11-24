import os

FOLDER = "inputs"

def getDayInput(day, test=False):
    if test:
        fileName = f"input{day}-test.txt"
    else:
        fileName = f"input{day}.txt"

    filePath = os.path.join(FOLDER, fileName)

    with open(filePath, "r") as f:
        lines = f.read().splitlines()

        return lines
    