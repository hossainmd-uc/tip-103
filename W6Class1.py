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


# Problem 1: Selective DNA Deletion


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next


def edit_dna_sequence(dna_strand, m, n):
    # Keep track of the current position in the linked list
    current = dna_strand
    # iterate through the linked list until we reach the end
    while current:
        # Keep the first m nodes
        for _ in range(m - 1):
            # if we reach the end of the linked list, return the modified linked list
            if not current:
                return dna_strand
            current = current.next

        if not current:
            return dna_strand

        # After keeping the first m nodes, we need to delete the next n nodes
        tail = current
        for _ in range(n):
            if not tail.next:
                break
            tail = tail.next
        # Connect the last node of the kept nodes to the next node after the deleted nodes
        current.next = tail.next
        # Move the current pointer to the next node after the deleted nodes
        current = tail.next

    return dna_strand


# Space Complexity: O(1) - We are modifying the linked list in place and not using any additional data structures that grow with the input size.


# dna_strand = Node(
#     1,
#     Node(
#         2,
#         Node(
#             3,
#             Node(
#                 4,
#                 Node(
#                     5,
#                     Node(
#                         6,
#                         Node(
#                             7,
#                             Node(
#                                 8,
#                                 Node(9, Node(10, Node(11, Node(12, Node(13))))),
#                             ),
#                         ),
#                     ),
#                 ),
#             ),
#         ),
#     ),
# )
# print_linked_list(edit_dna_sequence(dna_strand, 2, 3))


# Problem 2: Protein Folding Loop Detection


# Output: List of the cycle nodes
def cycle_length(protein):

    # Create a slow and fast pointer
    slow = fast = protein

    # Use while loop to move the pointers through the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Check if slow and fast meet, if they do, we have a cycle
        if slow is fast:
            cycle_vals = []
            node = slow
            # Use whiel loop to traverse the cycle and collect the values of the nodes in the cycle
            while True:
                cycle_vals.append(node.value)
                node = node.next
                if node is slow:
                    return cycle_vals
    return []


# protein_head = Node("Ala", Node("Gly", Node("Leu", Node("Val"))))
# protein_head.next.next.next.next = protein_head.next
# print(cycle_length(protein_head))


# Problem 3: Segmenting Protein Chains for Analysis


# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def split_protein_chain(protein, k):

    # Find total length of the linked list
    total_length = 0
    current = protein
    while current:
        total_length += 1
        current = current.next

    # Find how many will go into each container at minimum
    part_size = total_length // k
    # Find how many will have an extra node to account for the remainder
    remainder = total_length % k

    # Create the buckets for the split linked lists
    buckets = [[] for _ in range(k)]

    # Iterate through the protein linked list and distribute the nodes into the buckets
    current = protein
    bucket_index = 0
    while current:
        # distribute the nodes into the buckets based on the part size and add an additional node from the remainder if remainder is greater than 0
        for _ in range(part_size):
            if current:
                buckets[bucket_index].append(current.value)
                current = current.next
        if remainder > 0:
            if current:
                buckets[bucket_index].append(current.value)
                current = current.next
            remainder -= 1
        bucket_index += 1
    return buckets


protein1 = Node(
    "Ala",
    Node(
        "Gly",
        Node(
            "Leu",
            Node("Val", Node("Pro", Node("Ser", Node("Thr", Node("Cys"))))),
        ),
    ),
)
protein2 = Node("Ala", Node("Gly", Node("Leu", Node("Val"))))

parts = split_protein_chain(protein1, 3)
print(parts)


parts = split_protein_chain(protein2, 5)
print(parts)
