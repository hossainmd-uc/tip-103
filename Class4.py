"""
Problem 1: Balanced Art Collection
Problem 2: Verifying Authenticity
Problem 3: Gallery Wall
Problem 4: Gallery Subdomain Traffic
Problem 5: Beautiful Collection
Problem 6: Counting Divisible Collections in the Gallery
"""

# Problem [Number]: [Problem Title/Description]
#
# UNDERSTAND:
# - [What is the problem asking?]
# - [What are the inputs?]
# - [What are the outputs?]
# - [What are the constraints/edge cases?]
#
# PLAN:
# - [Step-by-step approach]
# - [What data structures or algorithms to use?]
# - [How to break down the problem?]
#
# IMPLEMENT:
# [Your code here]

# Problem 1: Balanced Art Collection

# A balanced collection is one where the difference between the maximum and minimum
# value of the art pieces is exactly 1.
from collections import Counter


def find_balanced_subsequence(art_pieces):

    # build a counter
    piece_counter = Counter(art_pieces)

    # dictionary/counter object✅
    key_dict = dict(sorted(piece_counter.items()))

    max_balance = 0
    # find the difference of the keys which = 1 ✅
    for key in key_dict.keys():

        current_balance = key_dict.get(key) + key_dict.get(key + 1, -999)
        if current_balance > max_balance:
            max_balance = current_balance
    return max_balance


# dict.get(key[, default_value])

# for key, _ in key_dict.items():
#     # initalize the value of the previous key for comparison
#     if prev_val is None:
#         prev_val = key
#         continue
#     # checking if the difference between 2 key is 1
#     if prev_val - key == -1:
#         # counting the combined frequency and checking to see if it is max
#         current_balance = key_dict[prev_val] + key_dict[key]
#         if current_balance > max_balance:
#             max_balance = current_balance
#     prev_val = key
# return max_balance
# in those keys we wanted to find the highest freq count ✅

# sum the value of the counter ✅
# of those keys we identify


# art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
# art_pieces2 = [1, 2, 3, 4]
# art_pieces3 = [1, 1, 1, 1]


# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))
# Problem [Number]: [Problem Title/Description]
#
# UNDERSTAND:
# - [What is the problem asking?]
# 1 , 1
# 1,2,2
# 1,2,3,3  L=n+1
# - [What are the inputs?] an array
# - [What are the outputs?] a boolean
# - [What are the constraints/edge cases?]
#
# PLAN:
# - [Step-by-step approach]
# sort, 1, 2,3,3.  , check the last one to see the biggest one,
# - [What data structures or algorithms to use?]
# - [How to break down the problem?]
#   we find n by doing length - 1
#
# IMPLEMENT:
# [Your code here]
# Problem 2: Verifying Authenticity

def is_authentic_collection(art_pieces):
    n = len(art_pieces) - 1
    l = len(art_pieces)
    valid_set = {i for i in range(1, l)}  #n = 3 , 1,2,3 l=4

    # Check if expected set range is equal to incrementing part of original
    # Check if original is 1 off when compared to valid set
    # Ensure that the LAST value (n) appears twice
    if set(art_pieces) == valid_set and len(valid_set) + 1 == len(art_pieces) and art_pieces.count(n) == 2:
        return True
    return False
    # find and sure that the art piece has all numbers in the valid set
    
   
    # once the set is empty (meaning that the array should have all the valid number at least once) --> return true


collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
