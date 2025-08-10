# 10 Aug 2025
# Red Black Trees

from L0T_RedBlackTree import *

import random

def ref_impl_ins(tree, user):
    """
    Reference implementation for Red-Black Tree insertion with balancing
    """
    # Step 1: Standard BST insertion
    new_node = RBNode(user)
    new_node.parent = None
    new_node.left = tree.nil
    new_node.right = tree.nil
    new_node.red = True

    parent = None
    current = tree.root
    while current != tree.nil:
        parent = current
        if new_node.val < current.val:
            current = current.left
        elif new_node.val > current.val:
            current = current.right
        else:
            # duplicate, just ignore
            return

    new_node.parent = parent
    if parent is None:
        tree.root = new_node
    elif new_node.val < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node

    # Step 2: Call fix_insert to maintain Red-Black properties
    ref_fix_insert(tree, new_node)


def ref_fix_insert(tree, node):
    """
    Reference implementation for fixing Red-Black Tree properties after insertion
    """
    # While the current node is not the root and has a red parent
    while node != tree.root and node.parent.red:
        # Identify parent, grandparent
        parent = node.parent
        grandparent = parent.parent
        
        # If parent is a right child of grandparent
        if parent == grandparent.right:
            uncle = grandparent.left  # Uncle is left child
            
            # If uncle is red
            if uncle.red:
                # Recolor uncle and parent to black
                uncle.red = False
                parent.red = False
                # Recolor grandparent to red
                grandparent.red = True
                # Move up the tree by making current node the grandparent
                node = grandparent
            else:
                # Uncle is black
                # If current node is left child of parent
                if node == parent.left:
                    # Move up the tree by making current node the parent
                    node = parent
                    # Rotate right around current node
                    tree.rotate_right(node)
                    # Set parent to be current node's parent
                    parent = node.parent
                
                # Recolor parent to black
                parent.red = False
                # Recolor grandparent to red
                grandparent.red = True
                # Rotate left around grandparent
                tree.rotate_left(grandparent)
        
        # If parent is a left child of grandparent
        else:
            uncle = grandparent.right  # Uncle is right child
            
            # If uncle is red
            if uncle.red:
                # Recolor uncle and parent to black
                uncle.red = False
                parent.red = False
                # Recolor grandparent to red
                grandparent.red = True
                # Move up the tree by making current node the grandparent
                node = grandparent
            else:
                # Uncle is black
                # If current node is right child of parent
                if node == parent.right:
                    # Move up the tree by making current node the parent
                    node = parent
                    # Rotate left around current node
                    tree.rotate_left(node)
                    # Set parent to be current node's parent
                    parent = node.parent
                
                # Recolor parent to black
                parent.red = False
                # Recolor grandparent to red
                grandparent.red = True
                # Rotate right around grandparent
                tree.rotate_right(grandparent)
    
    # Recolor the root to black
    tree.root.red = False


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
    (4),
]

submit_cases = run_cases + [
    (10),
]


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    reference_tree = RBTree()
    for user in users:
        tree.insert(user)
        ref_impl_ins(reference_tree, user)
    print("=====================================")
    print("Expecting:")
    print("-------------------------------------")
    print(print_tree(reference_tree))
    print("-------------------------------------\n")
    print("Actual:")
    print("-------------------------------------")
    print(print_tree(tree))
    print("-------------------------------------\n")

    if print_tree(tree) == print_tree(reference_tree):
        print("Pass \n")
        return True
    print("Fail \n")
    return False


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    return "\n".join(lines)


def format_tree_string(node, lines, level=0):
    if node.val is not None:
        format_tree_string(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        format_tree_string(node.left, lines, level + 1)


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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
