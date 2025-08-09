# 9 Aug 2025
# Binary Trees

from L0T_BinaryTrees import *
import random

def ref_implementation(bst_node, user):
    """Reference BST insertion implementation"""
    if bst_node.val is None:
        bst_node.val = user
    elif user < bst_node.val:
        if bst_node.left is None:
            bst_node.left = BSTNode(user)
        else:
            ref_implementation(bst_node.left, user)
    elif user > bst_node.val:
        if bst_node.right is None:
            bst_node.right = BSTNode(user)
        else:
            ref_implementation(bst_node.right, user)

def ref_inorder(node, result):
    """Reference in-order traversal implementation"""
    if node is not None and node.val is not None:
        ref_inorder(node.left, result)
        result.append(node.val)
        ref_inorder(node.right, result)
    return result



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
    (3),
    (5),
]

submit_cases = run_cases + [
    (10),
]


def test(num_users):
    users = get_users(num_users)
    expected_bst = BSTNode()
    for user in users:
        ref_implementation(expected_bst, user)
    print("=====================================")
    print("Expecting Tree:")
    print("-------------------------------------")
    print_tree(expected_bst)
    print("-------------------------------------\n")
    actual_bst = BSTNode()
    for user in users:
        print(f"Inserting {user} into tree...")
        actual_bst.insert(user)
    print("\n")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_bst)
    print("-------------------------------------")
    if ref_inorder(actual_bst, []) == ref_inorder(expected_bst, []):
        print("Pass \n")
        return True
    print("Fail \n")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
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
