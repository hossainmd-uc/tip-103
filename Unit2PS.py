"""
Captain Blackbeard has a treasure map with several clues that point to different
locations on an island. Each clue is associated with a specific location and the number
of treasures buried there. Given a dictionary treasure_map where keys are location names
and values are integers representing the number of treasures buried at those locations,
write a function total_treasures() that returns the total number of treasures buried on
the island.
"""


def total_treasures(treasure_map):
    # Iterate through the values
    total = 0
    for treasure_count in treasure_map.values():
        total += treasure_count

    return total


treasure_map1 = {"Cove": 3, "Beach": 7, "Forest": 5}

treasure_map2 = {"Shipwreck": 10, "Cave": 20, "Lagoon": 15, "Island Peak": 5}

# print(total_treasures(treasure_map1))
# print(total_treasures(treasure_map2))

"""
Captain Feathersword has found another pirate's buried treasure, but they suspect it's 
booby-trapped. The treasure chest has a secret code written in pirate language, and 
Captain Feathersword believes the trap can be disarmed if the code can be balanced. A 
balanced code is one where the frequency of every letter present in the code is equal. 
To disable the trap, Captain Feathersword must remove exactly one letter from the 
message. Help Captain Feathersword determine if it's possible to remove one letter to 
balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a 
function can_make_balanced() that returns True if it's possible to remove one letter so 
that the frequency of all remaining letters is equal, and False otherwise.
"""


def can_make_balanced(code):
    if not code:
        return False
    if len(code) in [1, 2, 3]:
        return True

    l_map = dict()
    for letter in code:
        if letter not in l_map:
            l_map[letter] = 1
        else:
            l_map[letter] += 1

    num_freq = dict()
    for num in l_map.values():
        if num not in num_freq:
            num_freq[num] = 1
        else:
            num_freq[num] += 1

    l = sorted(list(num_freq.items()))
    if len(num_freq) > 2:
        return False
    elif len(num_freq) == 2:
        # case: lower frequency is a single letter that occurs once -> True
        # case: higher frequency is 1 frequency away and only appears once -> True

        if l[0][0] == 1 and l[0][1] == 1:
            return True
        if l[1][0] == l[0][0] + 1 and l[1][1] == 1:
            return True
    else:
        if l[0][0] == 1 or l[0][1] == 1:
            return True
    return False


code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1))
print(can_make_balanced(code2))
