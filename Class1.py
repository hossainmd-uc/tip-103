print("Hello World!")


def linear_search(items, target):

    # Use for/while loop to keep track of the index
    # Go through and check every item
    # If match found, return index.
    # Increment after each loop
    # If loop terminates, then return -1
    i = 0

    while i < len(items):
        if items[i] == target:
            return i
        i += 1
    return -1


items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
target = "hunny"
# print(linear_search(items, target))

items = ["bed", "blue jacket", "red shirt", "hunny"]
target = "red balloon"
# print(linear_search(items, target))


def final_value_after_operations(operations):
    # Set tigger to 1
    # For loop through list
    # if we see bouncy, flouncy: increment by 1
    # ....., decrement by 1
    # return tigger

    tigger = 1

    for each in operations:
        if each in ("bouncy", "flouncy"):
            tigger += 1
        elif each in ("trouncy", "pouncy"):
            tigger -= 1
    return tigger


operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))


def tiggerfy(word):
    # First make the word all lowercase (.lower)
    #

    word_l = word.lower()

    final = ""
    i = 0

    while i < len(word):
        single = word_l[i]
        double = word_l[i : i + 2]

        if double == "gg" or double == "er":
            i += 2
        elif single == "t" or single == "i":
            i += 1
        else:
            final += word[i]
            i += 1

    return final


# word = "Trigger"
# print(tiggerfy(word))

# word = "eggplant"
# print(tiggerfy(word))

# word = "Choir"
# print(tiggerfy(word))

import math


def non_decreasing(nums):
    # Go through each number (for loop)
    # Use counter to keep track of how many modifications are needed
    # Use a variable to keep track of last. Then compare against last
    # If current is < last:
    # modifications += 1
    # If modifications > 1:
    # return False
    # return True otherwise?

    last = nums[0]
    count = 0

    for i in range(1, len(nums)):  # start from first

        if nums[i] < last:  # check condition (is it <=?)
            count += 1

        if count > 1:  # short circuit
            return False

        last = nums[i]

    return True


nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))
