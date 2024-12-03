# Colin Ryerse

# Advent of Code Day 2 Puzzle Solution

# *For a safe report* BOTH are true
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three

def getInput():
    with open("day2-puzzle-input.txt", "r") as file:
        levels = file.readlines()
        reports = [line.strip() for line in levels]
    return reports
        

def isSafe(report):

    # splits the list into individual integers 
    levels = list(map(int, report.split()))

    # Checks if the levels are increasing or decreasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    if not (increasing or decreasing):
        return False

    # Check differences between adjacent levels
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if not (1 <= diff <= 3):
            return False
        
    return True

def numberSort():
    reports = getInput()
    safeCount = 0

    for report in reports:
        if isSafe(report):
            safeCount += 1

    print(f"Number of safe reports: {safeCount}")

numberSort()