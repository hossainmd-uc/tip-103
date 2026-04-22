# Breakout room 21

from collections import deque


# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


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

# Unit 9 PS1


class Puff:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


from collections import deque


def listify_design(design):
    # BFS approach
    # Understand
    # I: BST
    # O: List of Lists
    # C:
    # E: Empty List -> []
    # Plan
    # Potentially at each level, we maintain a List

    # Base
    if not design:
        return []

    # Recursive
    q = deque()
    q.append(design)

    res = []

    while q:
        level_size = len(q)
        level = []

        # traverse through each level
        for _ in range(level_size):
            item = q.popleft()
            level.append(item.val)

            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)

        res.append(level)

    return res


croquembouche = Puff(
    "Vanilla",
    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")),
    Puff("Strawberry"),
)
# print(listify_design(croquembouche))


def zigzag_icing_order(cupcakes):
    # BFS
    # Understand
    # I: BST
    # O: List of items
    # C:
    # E: Empty List -> []

    # Base

    if not cupcakes:
        return []

    # Recursive
    q = deque()
    q.append(cupcakes)

    res = []

    reverseBool = False

    while q:
        level_size = len(q)
        level = []

        # traverse through each level
        for _ in range(level_size):
            item = q.popleft()
            level.append(item.val)

            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)

        # toggle reverse
        if reverseBool:
            # Append the reverse version
            # level = level[::-1]
            level.reverse()

        res.extend(level)
        reverseBool = not reverseBool

    return res


flavors = [
    "Chocolate",
    "Vanilla",
    "Lemon",
    "Strawberry",
    None,
    "Hazelnut",
    "Red Velvet",
]
cupcakes = build_tree(flavors)
# print(zigzag_icing_order(cupcakes))


def larger_order_tree(orders):

    # Provcess right, root, left
    total = 0

    def helper(order):
        nonlocal total

        if not order:
            return

        helper(order.right)
        total = total + order.val
        order.val = total
        helper(order.left)

    helper(orders)

    return orders


order_sizes = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))
