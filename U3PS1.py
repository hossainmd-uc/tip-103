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

# Problem 1: Arrange Guest Arrival Order

# Input: String of Characters
# Output: An integer

# Constraints:
# "I" = next number larger; 'D' = next number smaller
# Return the lexicographically smallest number order


def arrange_guest_arrival_order(arrival_pattern):
    ap = arrival_pattern + "I"

    stack = []
    final = []

    ind = 1

    for i in range(len(ap)):
        if ap[i] == "I":
            offset = len(stack) + ind
            next = offset + 1
            while stack:
                final.append(offset)
                stack.pop()
                offset -= 1
            final.append(ind)
            ind = next
        else:
            stack.append("D")

    return final


arrival_pattern = "IIIDIDDD"
# arrival_pattern = "III"
# print(arrange_guest_arrival_order(arrival_pattern))


"""

def arrange_guest_arrival_order(arrival_pattern):
    ap = arrival_pattern + "I"

    stack = []
    final = []

    curr = 1

    for i in range(len(ap)):
        if ap[i] == "I":
            final.append(curr)

            while stack:
                final.append(stack.pop())
            curr += 1
        else:
            stack.append(curr)
            curr += 1

    return final
"""

from collections import deque


def reveal_attendee_list_in_order(attendees):

    attendees = sorted(attendees)
    next = 0

    dq = deque(i for i in range(len(attendees)))
    final = [0] * len(attendees)

    m = 0

    while dq:
        if m % 2 == 0:
            print(final)
            final[dq.popleft()] = attendees[next]
            next += 1
        else:
            dq.append(dq.popleft())

        m += 1

    return final


# print(reveal_attendee_list_in_order([17, 13, 11, 2, 3, 5, 7]))

import heapq
import itertools


# def arrange_attendees_by_priority(attendees, priority):
#     # One pass attendees
#     # add out of priotity to heapq
#     # empty heap

#     final = []
#     heap = []

#     count = itertools.count()

#     for each in attendees:
#         if each < priority:
#             final.append(each)
#         else:
#             if each > priority:
#                 heapq.heappush(heap, (1, next(count), each))
#             else:
#                 heapq.heappush(heap, (0, next(count), each))

#     while heap:
#         final.append(heapq.heappop(heap)[2])

#     return final


def arrange_attendees_by_priority(attendees, priority):
    l1 = []
    l2 = []
    l3 = []

    for each in attendees:
        if each < priority:
            l1.append(each)
        elif each > priority:
            l3.append(each)
        else:
            l2.append(each)

    return l1 + l2 + l3


# print(arrange_attendees_by_priority([9, 12, 5, 10, 14, 3, 10], 10))
# print(arrange_attendees_by_priority([-3, 4, 3, 2], 2))


# def rearrange_guests(guests):
#     pos = []
#     neg = []

#     for each in guests:
#         if each > 0:
#             pos.append(each)
#         else:
#             neg.append(each)

#     return [item for pair in zip(pos, neg) for item in pair]


def rearrange_guests(guests):

    final = [0] * len(guests)

    p = 0
    n = 1

    for i in range(len(guests)):
        g = guests[i]

        if g > 0:
            final[p] = g
            p += 2
        else:
            final[n] = g
            n += 2

    return final


# print(rearrange_guests([3, 1, -2, -5, 2, -4]))
# print(rearrange_guests([-1, 1]))


def min_changes_to_make_balanced(schedule):

    s = []

    unclosed = 0

    for each in schedule:
        if each == ")":
            if not s:
                unclosed += 1
            else:
                s.pop()
        else:
            s.append(each)

    return len(s) + unclosed


# print(min_changes_to_make_balanced("())"))
# print(min_changes_to_make_balanced("((("))

# input: two strings
# out: list of ints


# def mark_event_timeline(event, timeline):

#     t = "".join(["?"] * len(timeline))

#     q = deque()
#     q.append((t, []))

#     max_idx = len(timeline) - len(event)  # check from 0 - max_idx
#     possiblities = [i for i in range(0, max_idx + 1)]
#     max_tries = len(timeline) * 10

#     while q:
#         # print(q)
#         item = q.popleft()
#         # operationally define 'moving closer' to the timeline as
#         # at least maintaining or decreasing the current number of matches

#         matches = sum(pair[0] == pair[1] for pair in zip(item[0], timeline))
#         actual_p = [x for x in possiblities if x not in item[1]]
#         for start in actual_p:
#             new = item[0][:start] + event + item[0][start + len(event) :]
#             matches_after_checked = sum(
#                 pair[0] == pair[1] for pair in zip(new, timeline)
#             )

#             # print(
#             #     f"new: {new} -- o: {timeline}: matched {matches_after_checked - matches} more times"
#             # )

#             if matches_after_checked == len(timeline):
#                 item[1].append(start)
#                 return item[1]

#             if matches_after_checked >= matches:
#                 if len(item[1]) < max_tries:
#                     # print("enqueuing")
#                     temp = item[1][:]
#                     temp.append(start)
#                     q.append((new, temp))

#     return []


def mark_event_timeline(event, timeline):

    # t = "".join(["?"] * len(timeline))

    q = deque()
    q.append((timeline, []))

    max_idx = len(timeline) - len(event)  # check from 0 - max_idx
    possibilities = [i for i in range(0, max_idx + 1)]
    max_tries = len(timeline) * 10

    while q:
        item = q.pop()
        word = item[0]
        unstamped = item[1]

        if len(unstamped) >= max_tries:
            continue

        matches = word.count("?")
        unstamped_idx = [x for x in possibilities if x not in unstamped]

        # Goal is to turn all places into ?
        for i in unstamped_idx:
            middle = word[
                i : i + len(event)
            ]  # Original part of to be placed area
            print(middle)
            replaced = [
                "?" if x == y else y for x, y in zip(event, middle)
            ]  # Replacing
            print(replaced)
            new = word[:i] + "".join(replaced) + word[i + len(event) :]

            print(new)

            # new = word[:i] + event + word[i + len(event) :]
            new_matches = new.count("?")
            additional_matches = new_matches - matches

            if new_matches == len(timeline):
                unstamped.append(i)
                return unstamped

            if additional_matches > 0:
                # enqueue
                temp = unstamped[:]
                temp.append(i)
                q.append((new, temp))

    return []


# print(mark_event_timeline("abc", "ababc"))
# print(mark_event_timeline("abca", "aabcaca"))

# print(mark_event_timeline("a", "aaaaaaaaaaaaaaa"))


# Problem 1: Blueprint Approval Process
import heapq


def blueprint_approval(blueprints):

    q = []

    for each in blueprints:
        heapq.heappush(q, each)

    final = []
    while q:
        final.append(heapq.heappop(q))

    return final


print(blueprint_approval([3, 5, 2, 1, 4]))
print(blueprint_approval([7, 4, 6, 2, 5]))
