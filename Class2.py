def transpose(matrix):
    # Create a new matrix with rows and cols count flipped

    cols = len(matrix[0])
    rows = len(matrix)

    new = [[0 for _ in range(rows)] for _ in range(cols)]

    # for loop through the original (nested)
    for r in range(rows):
        for c in range(cols):
            new[c][r] = matrix[r][c]

    print(new)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpose(matrix)

matrix = [[1, 2, 3], [4, 5, 6]]
"""
[[1, 4], 
[2, 5], 
[3, 6]]

"""
# transpose(matrix)


def reverse_list(lst):
    # Edge Case: Empty List
    # Create two variables, one for front one for back
    # While front < back:
    # switch

    # # handle edge case (might not need)
    # if not lst:
    #     return []

    front = 0
    back = len(lst) - 1

    while front < back:
        lst[front], lst[back] = lst[back], lst[front]
        front += 1
        back -= 1
    return lst


lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# print(reverse_list(lst))
# Output: ["eeyore", "roo", "piglet", "christopher robin", "pooh"]


def remove_dupes(items):
    # Constraints:
    # Don't create another array
    # Modify original array

    # Create a set
    # add all elements to set

    # Edge case: array length < 2

    items.sort()

    # # Approach 1

    # p1 = 0
    # p2 = 1

    # while p2 < len(items):
    #     while items[p1] == items[p2]:
    #         p2 += 1

    #     del items[
    #         p1 + 1 : p2
    #     ]  # Not ideal because after deletion, p1 /p2 is out
    #     # of range

    #     p1 += 1
    #     p2 = p1 + 1

    # del items[p2:]  # What's this for
    # this might be wrong, theplan was to cut out any excess left after the loop ends but don't think we'll have any
    # i thinkit's better to just move unique elements to the front and perform exactly one deletion at the end, rather than deleting while looping
    # rain: I agree, delete at end

    # actually ,better idea is to start from the reverse, back to front
    # then if we remove, it won't affect the time complexity as much

    # Approach 2 :start reversed

    if len(items) < 2:
        return items

    p1 = len(items) - 1
    p2 = len(items) - 2

    while p2 > -1:  # double check
        if items[p1] != items[p2]:
            # items = items[0 : p2 + 1] + items[p1:]
            del items[p2 + 1 : p1]
            p1 = p2

        if p2 == 0:
            del items[:p1]
            return items

        p2 -= 1


items = [
    "extract of malt",  # p1
    "extract of malt",  # cut out
    "extract of malt",  # cut out
    "thistle",  # p2
    "thistle",
]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))
