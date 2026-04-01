# Problem [Number]: [Problem Title/Description]
#
# UNDERSTAND:
# - [What is the problem asking?] method to check if a parameter is in a list
# - [What are the inputs?] string
# - [What are the outputs?] list of strings
# - [What are the constraints/edge cases?] nothing is valid
#
# PLAN:
# - [Step-by-step approach] for loop through list
# - [What data structures or algorithms to use?] list
# - [How to break down the problem?]
#
# IMPLEMENT:
# [Your code here]

# Problem 2: Add Furniture


class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.neighbor = neighbor
        self.furniture = []

    def add_item(self, item_name):
        # Create list of valid items
        valid = [
            "acoustic guitar",
            "ironwood kitchenette",
            "rattan armchair",
            "kotatsu",
            "cacao tree",
        ]
        if item_name in valid:
            self.furniture.append(item_name)


# print(apollo.name)
# print(apollo.species)
# print(apollo.catchphrase)
# print(apollo.furniture)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# Problem 3: Group by Personality


def of_personality_type(townies, personality_type):

    final = []

    for villager in townies:
        if villager.personality == personality_type:
            final.append(villager.name)
    return final


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))


# Problem 4: Telephone


def message_received(start_villager, target_villager):

    # Might be able to use to track if cycle exists
    explored = set()

    # Maybe while loop? While villager.neighbor?
    # Just make sure there's no cycle?

    # While loop
    # Go through each neighbor starting with start_neighbor
    # If we encounter target_villager -> return true
    # If target_villager in explored -> return False

    current = start_villager

    while current:
        if current in explored:
            return False
        if current == target_villager:
            return True

        explored.add(current)
        current = current.neighbor

    return False


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))

# isabelle -> tom_nook -> kk_slider -> isabelle
