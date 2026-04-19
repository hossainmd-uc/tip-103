"""
Problem 1: Ivy Cutting
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the
rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the
root node to the rightmost leaf node. If there is no right child, return only the root node value (the rightmost path in
this case is just the root node).

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you
believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating
time and space complexity.

U: Given the root of the plant, return a list with the value of each node in the path from the
root node to the rightmost leaf node. If there is no right child, return only the root node value (the rightmost path in
this case is just the root node).

P:
init res = []

traverse through the tree, while right node exist

add each node to res while the right node exist

"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# Problem 1: Ivy Cutting I
def right_vine(root):

    # Case where there is no right side node
    # if not root.right:
    # return [root.val]

    # Create an empty list that will hold traversal
    res = []

    # Traverse
    current = root
    while current:
        res.append(current.val)
        current = current.right

    return res


"""
If you implemented right_vine() iteratively in the previous problem, implement it recursively. If you implemented it 
recursively, implement it iteratively.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating 
time and space complexity.


"""

# Problem 2: Ivy Cutting II


def right_vine_r(root):
    res = []

    # create a helper
    def right(res, root):
        # Base
        if not root:
            return res
        # recursive case
        res.append(root.val)
        return right(res, root.right)

    ans = right(res, root)
    return ans

    # test


def right_vine_r_optimized(root):

    # Base
    if not root:
        return []

    # Recursive
    return [root.val] + right_vine_r_optimized(root.right)


# Callstack:
# right_vine_r_optimized('Root', right_vine_r_optimized(root.right)) -> ["Root"] + ["Node2", "Leaf3"]
# right_vine_r_optimized('Node2', right_vine_r_optimized(root.right)) -> ["Node2"] + ["Leaf3"]
# right_vine_r_optimized('Leaf3', right_vine_r_optimized(root.right)) -> ["Leaf3"] + []
# right_vine_r_optimized('Leaf3', right_vine_r_optimized(root.right)) -> None so return []
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine_r(ivy1))
# print(right_vine_r(ivy2))

# print(right_vine_r_optimized(ivy1))
# print(right_vine_r_optimized(ivy2))

"""
U: Given the root of a binary tree representing the magnolia, return a list of the values of each node using a 
postorder traversal. In a postorder traversal, you explore the left subtree first, then the right subtree, and 
finally the root. Postorder traversals are often used when deleting nodes from a tree.


"""
# Problem 3: Pruning Plans


def survey_tree(root):

    # Base
    if not root:
        return []

    # Then add root
    return survey_tree(root.left) + survey_tree(root.right) + [root.val]


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

# print(survey_tree(magnolia))


# Problem 4: Sum Inventory
def sum_inventory(inventory):
    # Base
    if not inventory:
        return 0

    return (
        inventory.val
        + sum_inventory(inventory.right)
        + sum_inventory(inventory.left)
    )


inventory = TreeNode(
    40, TreeNode(5, TreeNode(20)), TreeNode(10, TreeNode(1), TreeNode(30))
)

# print(sum_inventory(inventory))


# Problem 5: Calculating Yield II


def calculate_yield(root):

    # Base
    val = root.val
    # print(val)
    if isinstance(val, int):
        return root.val

    if root.val == "+":
        return calculate_yield(root.left) + calculate_yield(root.right)
    elif root.val == "-":
        return calculate_yield(root.left) - calculate_yield(root.right)
    elif root.val == "*":
        return calculate_yield(root.left) * calculate_yield(root.right)


"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

# print(calculate_yield(root))


# Problem 6: Plant Classifications
def get_most_specific(taxonomy):
    # track a res list then return it after all leaf nodes are processed
    res = []

    def helper(taxonomy):

        if not taxonomy:
            return []

        # Base
        if not taxonomy.left and not taxonomy.right:
            res.append(taxonomy.val)

        # Recursive Case
        helper(taxonomy.left)
        helper(taxonomy.right)

    helper(taxonomy)

    return res


plant_taxonomy = TreeNode(
    "Plantae",
    TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
    TreeNode(
        "Flowering",
        TreeNode("Gymnosperms"),
        TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots")),
    ),
)

# print(get_most_specific(plant_taxonomy))
from collections import deque


def count_old_growth(root, threshold):

    # Need to visit every node
    # Accumulate if threshold is greater

    if not root:
        return 0

    res = 0
    # We will use a queue to avoid maximum recursion error
    nodes = deque()
    nodes.append(root)
    while nodes:
        node = nodes.popleft()
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

        if node.val >= threshold:
            res += 1

    return res


def count_old_growth_2(root, threshold):

    if not root:
        return 0

    return (
        (1 if root.val >= threshold else 0)
        + count_old_growth(root.left, threshold)
        + count_old_growth(root.right, threshold)
    )


forest = TreeNode(
    100,
    TreeNode(1200, TreeNode(20)),
    TreeNode(1500, TreeNode(700), TreeNode(2600)),
)

# print(count_old_growth_2(forest, 1000))


def is_identical(root1, root2):
    # Two stack approach

    s1 = []
    s2 = []

    s1.append(root1)
    s2.append(root2)

    while s1 and s2:

        c1 = s1.pop()
        c2 = s2.pop()

        if c1 and c2 and c1.val != c2.val:
            return False
        elif not c1 and not c2:
            continue
        elif c1 and not c2:
            return False
        elif c2 and not c1:
            return False

        s2.append(c2.left)
        s2.append(c2.right)

        s1.append(c1.left)
        s1.append(c1.right)

    return True


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))


root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))
