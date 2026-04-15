# Group 11

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

# Problem 1: Next in Queue


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        # Create a new node
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        #
        if self.is_empty():
            return None

        temp = self.front.value
        self.front = self.front.next

        return temp

    def peek(self):
        return self.front.value if not self.is_empty() else None


# # Create a new Queue
# q = Queue()

# # Add elements to the queue
# q.enqueue(("Love Song", "Sara Bareilles"))
# q.enqueue(("Ballad of Big Nothing", "Elliot Smith"))
# q.enqueue(("Hug from a Dinosaur", "Torres"))
# print_queue(q)

# # View the front element
# print("Peek: ", q.peek())

# # Remove elements from the queue
# print("Dequeue: ", q.dequeue())
# print("Dequeue: ", q.dequeue())

# # Check if the queue is empty
# print("Is Empty: ", q.is_empty())

# # Remove the last element
# print("Dequeue: ", q.dequeue())

# # Check if the queue is empty
# print("Is Empty:", q.is_empty())


def merge_playlists(playlist1, playlist2, a, b):

    # Things to watch ot for
    #  Err
    # Loop through playlist1 to find the position of a
    prev_a = playlist1

    for _ in range(a - 1):
        prev_a = prev_a.next

    # find the variable the we keep going after insert the second list
    current = prev_a.next
    for _ in range(b - a):
        current = current.next
    # The part that we will insert after the second playlist is inserted
    after = current.next

    # connect the prev_a to the second
    prev_a.next = playlist2

    # find the end of the playlist2

    temp = playlist2
    while temp.next:
        temp = temp.next

    # connect the end of the platylist2 to the after variables the we have createdtime and space complexity of your solution.
    temp.next = after

    return playlist1


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


playlist1 = Node(
    ("Flea", "St. Vincent"),
    Node(
        ("Juice", "Lizzo"),
        Node(
            ("Tenderness", "Jay Som"),
            Node(
                ("Ego Death", "The Internet"), Node(("Empty", "Kevin Abstract"))
            ),
        ),
    ),
)

playlist2 = Node(("Dreams", "Solange"), Node(("First", "Gallant")))

# print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))


# Problem 3: Shuffle Playlist


# Perhaps a recursive solution would be easier to reverse
def reverse_linked(head, prev=None):

    if not head:
        return prev

    next_node = head.next
    head.next = prev
    return reverse_linked(next_node, head)


def shuffle_playlist(playlist):
    # Constraint: You may not modify the values in the list's nodes.
    # Only the order of the nodes themselves may be changed.

    # Output: Return the head of the shuffled list.

    # slow moves 1 step, fast moves 2 steps
    # when fast reaches the end slow is in the middle
    slow = playlist
    fast = playlist

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    head = slow.next
    slow.next = None  # Split the list into two halves
    reversed_second_half = reverse_linked(head)

    # Do we need this?
    # head.next = None

    # Works!
    # print_linked_list(reversed_second_half)

    # Merge the two halves
    first_half = playlist
    second_half = reversed_second_half

    while first_half and second_half:
        # Save the next nodes
        temp1 = first_half.next
        temp2 = second_half.next

        # Shuffle the nodes
        first_half.next = second_half
        if temp1:  # Check if there is a next node in the first half
            second_half.next = temp1

        # Move to the next nodes
        first_half = temp1
        second_half = temp2

    if second_half:  # If there are remaining nodes in the second half
        first_half.next = second_half

    return playlist


# Testing
# shuffle_playlist(playlist1)

# playlist1 = Node(1, Node(2, Node(3, Node(4))))

playlist3 = Node(
    ("Respect", "Aretha Franklin"),
    Node(
        ("Superstition", "Stevie Wonder"),
        Node(
            ("Wonderwall", "Oasis"),
            Node(
                ("Like a Prayer", "Madonna"),
                Node(("Bohemian Rhapsody", "Queen")),
            ),
        ),
    ),
)

print_linked_list(shuffle_playlist(playlist3))
