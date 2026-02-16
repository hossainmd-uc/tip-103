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
