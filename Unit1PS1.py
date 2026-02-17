import math

"""
Write a function linear_search() to help Winnie the Pooh locate his lost items.
The function accepts a list items and a target value as parameters. The function
should return the first index of target in items, and -1 if target is not in items.
Do not use any built-in functions.
"""


def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
target = "hunny"
# print(linear_search(items, target))

items = ["bed", "blue jacket", "red shirt", "hunny"]
target = "red balloon"
# print(linear_search(items, target))


def tiggerfy(word):
    # Only check ALL substrings if original string has changed

    word = word.strip().lower()

    changed = True
    previous = word
    while changed:
        for each in ["t", "i", "gg", "er"]:
            if each in word:
                start = word.index(each)
                word = word[0:start] + word[start + len(each) :]

        if previous == word:
            changed = False
        else:
            previous = word

    print(word)


# One Pass
def tiggerfy2(word):
    i = 0
    final = []
    two_match = ["gg", "er"]

    while i < len(word):
        one_letter = word[i].lower()
        two_letter = word[i : i + 2].lower()

        if one_letter in ["t", "i"]:
            i += 1
        elif two_letter in two_match:
            i += 2
        else:
            final.append(word[i])
            i += 1

    return "".join(final)


# word = "Trigger"
# tiggerfy2(word)

# word = "eggplant"
# print(tiggerfy2(word))

# word = "Choir"
# print(tiggerfy2(word))

"""
Given an array nums with n integers, write a function non_decreasing() that checks if 
nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i 
(0-based) such that (0 <= i <= n - 2).
"""


def non_decreasing(nums):
    # go through the array comparing curr and next.
    # if curr <= next: then counter +=1
    # if counter == 1 or 0: true
    # if counter become > 1, short circuit

    counter = 0
    for i in range(len(nums) - 1):
        curr = nums[i]
        next = nums[i + 1]

        if curr >= next:
            counter += 1
            if counter > 1:
                return False

    return True


nums = [4, 2, 3]
# print(non_decreasing(nums))

nums = [4, 2, 1]
# print(non_decreasing(nums))

"""
Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several 
hidden clues have blown away. Write a function find_missing_clues() to help Christopher 
Robin figure out which clues he needs to remake. The function accepts two integers lower 
and upper and a unique integer array clues. All elements in clues are within the 
inclusive range [lower, upper].

A clue x is considered missing if x is in the range [lower, upper] and x is not in 
clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
That is, no element of clues is included in any of the ranges, and each missing number 
is covered by one of the ranges.
"""


def find_missing_clues(clues, lower, upper):
    # start at lower since that's where range starts
    # start at the first number, if it's

    if not clues:
        return [[lower, upper]]

    clues = sorted(clues)
    f = []
    start = lower
    clue_i = 0

    while start <= upper:
        # if list exhausted, construct final range
        if clue_i == len(clues):
            if upper - start >= 0:
                f.append([start, upper])
            return f

        if lower <= clues[clue_i] <= upper:
            if clues[clue_i] - start >= 1:
                f.append([start, clues[clue_i] - 1])
                start = clues[clue_i] + 1
                clue_i += 1
            else:
                # If the start and clue overlap, then check next number
                start = clues[clue_i] + 1
                clue_i += 1
        else:
            clue_i += 1

    return f


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))


clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))

"""
Write a function local_maximums() that accepts an n x n integer matrix grid and returns 
an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

    local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered
    around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3 matrix in 
grid.
"""


def local_maximums(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if rows < 3 or cols < 3:
        raise Exception("Input matrix must have at least 3 rows and 3 columns")

    final = [[0] * (cols - 2) for _ in range(rows - 2)]

    for r in range(rows - 2):
        for c in range(cols - 2):
            max = -math.inf
            for dr in range(3):
                for dc in range(3):  # can make cleaner with generator
                    current = grid[r + dr][c + dc]
                    if current > max:
                        max = current
            final[r][c] = max

    print(final)


local_maximums([[0, 0, 0], [1, 2, 1], [3, 3, 3]])

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]
local_maximums(grid)
