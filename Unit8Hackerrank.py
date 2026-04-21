from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(elements):
    """Helper to build a BST from a level-order list."""
    if not elements:
        return None
    root = TreeNode(elements[0])
    queue = deque([root])
    i = 1
    while i < len(elements):
        curr = queue.popleft()
        if i < len(elements) and elements[i] is not None:
            curr.left = TreeNode(elements[i])
            queue.append(curr.left)
        i += 1
        if i < len(elements) and elements[i] is not None:
            curr.right = TreeNode(elements[i])
            queue.append(curr.right)
        i += 1
    return root


def tree_to_list(root):
    """Helper to visualize the tree back as a list."""
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    # Trim trailing Nones to match Example output style
    while res and res[-1] is None:
        res.pop()
    return res


def delete_node(root, key):

    # Base
    if not root:
        return None

    # Find the next in-order successor (left-most node)
    # Delete the in-order successor and replace it with in-order node if any (not leaf)
    # return the root with in-order successor

    # Recursive
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Where key == root.val

        # If leaf
        if not root.left and not root.right:
            return None
        if root.left and not root.right:
            return root.left
        # If only right subtree
        if not root.left and root.right:
            return root.right

        # If it has left and right subtree
        # Find the in-order successor
        right = root.right
        while right and right.left:
            right = right.left

        root.val = right.val
        root.right = delete_node(root.right, right.val)

    return root


# --- Running Tests ---

test_cases = [
    {
        "root": [5, 3, 6, 2, 4, None, 7],
        "key": 3,
        "expected": [5, 4, 6, 2, None, None, 7],
    },
    {
        "root": [5, 3, 6, 2, 4, None, 7],
        "key": 0,
        "expected": [5, 3, 6, 2, 4, None, 7],
    },
    {"root": [], "key": 0, "expected": []},
]

for i, test in enumerate(test_cases):
    root_tree = build_tree(test["root"])
    modified_root = delete_node(root_tree, test["key"])
    result = tree_to_list(modified_root)
    print(f"Test {i+1}: {'Passed' if result == test['expected'] else 'Failed'}")
    print(f"   Output: {result}\n")
