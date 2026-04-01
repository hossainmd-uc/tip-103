# Hello

# Problem Set Version 1


def total_treasure(treasure_map):
    # Go through each of the VALUES only (.values)
    # Create a sum/total and add to it as we iterate

    total = 0
    for each in treasure_map.values():
        total += each

    return total


treasure_map1 = {"Cove": 3, "Beach": 7, "Forest": 5}

treasure_map2 = {"Shipwreck": 10, "Cave": 20, "Lagoon": 15, "Island Peak": 5}

# print(total_treasure(treasure_map1))
# print(total_treasure(treasure_map2))


def can_trust_message(message):
    # Clear Whitespace and
    # Turn string into set

    message = message.replace(" ", "")
    the_set = set(message)

    # print(the_set)

    return len(the_set) == 26


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"


# print(can_trust_message(message1))
# print(can_trust_message(message2))


def find_duplicate_chests(chests):
    # Create a dictionary to count freq of each number
    chest_dict = {}

    for each in chests:
        if each in chest_dict:
            chest_dict[each] += 1
        else:
            chest_dict[each] = 1

    l = []
    for k, v in chest_dict.items():
        if v == 2:  # Potential Edge case
            l.append(k)

    return l


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))


def can_make_balanced(code):
    # Constraint:
    # One letter has to be removed

    # Create a Freq map of each letter

    # If highest freq occurring letter is 1 off and all others are same: then ✅
    #

    freq_map = {}
    max_count = 0

    for each in code:
        if each in freq_map:
            freq_map[each] += 1
        else:
            freq_map[each] = 1
        max_count = max(max_count, freq_map[each])

    # must remove one letter
    for k in freq_map:
        if freq_map[k] == max_count:
            freq_map[k] -= 1
            break

    return len(set(freq_map.values())) == 1


code1 = "arghh"
code2 = "haha"

# print(can_make_balanced(code1))
# print(can_make_balanced(code2))


def find_treasure_indices(gold_amounts, target):
    # Assume 1 solution
    # don't use same value twice

    # create dictionary that contains k,v with value and index
    # create a complement variable equal to target - current value
    # search dict.keys() for complement, if its dict[ke]

    my_dict = {}

    for i in range(len(gold_amounts)):
        complement = target - gold_amounts[i]
        if complement in my_dict.keys():
            return [my_dict[complement], i]
        else:
            my_dict[gold_amounts[i]] = i


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))
print(find_treasure_indices(gold_amounts2, target2))
print(find_treasure_indices(gold_amounts3, target3))
