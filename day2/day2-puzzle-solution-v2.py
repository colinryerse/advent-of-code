# Colin Ryerse

# Advent of Code Day 2 Puzzle Solution 2/2

# *For a safe report* BOTH are true
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three

# Now, the same rules apply as before, except if removing a single level
# from an unsafe report would make it safe, the report instead counts as safe.

def getInput():
    with open("day2-puzzle-input.txt", "r") as file:
        levels = file.readlines()
        reports = [line.strip() for line in levels]
    return reports
        

def isSafe(levels):

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

def isSafeWithRemoval(report):

    # Splits the report into integers
    levels = list(map(int, report.split()))

    # Bypasses function if already safe
    if isSafe(levels):
        return True
    
    # Removes one integer at a time to check if it is safe
    for i in range(len(levels)):
        modifiedLevels = levels[:i] + levels[i+1:]
        if isSafe(modifiedLevels):
            return True
        
    return False



def numberSort():
    reports = getInput()
    safeCount = sum(1 for report in reports if isSafeWithRemoval(report))

    print(f"Number of safe reports: {safeCount}")

numberSort()