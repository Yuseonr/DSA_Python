# 9 Aug 2025
# Binary Trees

from L0T_BinaryTrees import *
import random


class User:
    def __init__(self, id):
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other):
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other):
        return isinstance(other, User) and self.id > other.id

    def __repr__(self):
        return "".join(self.user_name)


def get_users(num):
    random.seed(1)
    users = []
    ids = []
    for i in range(num * 3):
        ids.append(i)
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        user = User(id)
        users.append(user)
    return users


run_cases = [
    (
        4,
        [User(7), User(0), User(11), User(8)],
    ),
    (
        6,
        [User(10), User(5), User(0), User(9), User(16), User(17)],
    ),
]

submit_cases = run_cases + [
    (
        12,
        [
            User(34),
            User(22),
            User(2),
            User(19),
            User(17),
            User(10),
            User(11),
            User(18),
            User(30),
            User(27),
            User(23),
            User(33),
        ],
    ),
]


def test(num_characters, expected):
    characters = get_users(num_characters)  # Adjust according to your project structure
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print(print_tree(bst))
    print("-------------------------------------\n")
    print(f"Expecting: {expected}")
    try:
        actual = bst.preorder([])
        print(f"Actual: {actual}")
        if expected == actual:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    print("\n".join(lines))


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
