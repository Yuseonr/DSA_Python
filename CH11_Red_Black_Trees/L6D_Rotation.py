# 10 Aug 2025
# Red Black Trees

from L0T_RedBlackTree import *
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


def ref_impl_left(tree, pivot_parent):
    """
    Reference implementation for left rotation.
    Rotates left at pivot_parent node.
    """
    # Step 1: If pivot_parent is nil or pivot_parent's right child is nil, return
    if pivot_parent is tree.nil or pivot_parent.right is tree.nil:
        return
    
    # Step 2: Let pivot be pivot_parent's right child
    pivot = pivot_parent.right
    
    # Step 3: Set pivot_parent's right child to be pivot's left child
    pivot_parent.right = pivot.left
    
    # Step 4: If pivot's left child isn't a nil leaf node, set pivot's left child's parent to pivot_parent
    if pivot.left is not tree.nil:
        pivot.left.parent = pivot_parent
    
    # Step 5: Set pivot's parent to pivot_parent's parent
    pivot.parent = pivot_parent.parent
    
    # Step 6: Handle root and parent-child relationships
    if pivot_parent.parent is None:
        # pivot_parent is the root, set the root to pivot
        tree.root = pivot
    elif pivot_parent == pivot_parent.parent.left:
        # pivot_parent is its parent's left child
        pivot_parent.parent.left = pivot
    else:
        # pivot_parent is its parent's right child
        pivot_parent.parent.right = pivot
    
    # Step 7: Set pivot's left child to be pivot_parent
    pivot.left = pivot_parent
    
    # Step 8: Set pivot_parent's parent to be pivot
    pivot_parent.parent = pivot


def ref_impl_right(tree, pivot_parent):
    """
    Reference implementation for right rotation.
    Rotates right at pivot_parent node (all directionality inverted from left rotation).
    """
    # Step 1: If pivot_parent is nil or pivot_parent's left child is nil, return
    if pivot_parent is tree.nil or pivot_parent.left is tree.nil:
        return
    
    # Step 2: Let pivot be pivot_parent's left child (inverted: left instead of right)
    pivot = pivot_parent.left
    
    # Step 3: Set pivot_parent's left child to be pivot's right child (inverted: left/right swapped)
    pivot_parent.left = pivot.right
    
    # Step 4: If pivot's right child isn't a nil leaf node, set pivot's right child's parent to pivot_parent (inverted: right instead of left)
    if pivot.right is not tree.nil:
        pivot.right.parent = pivot_parent
    
    # Step 5: Set pivot's parent to pivot_parent's parent (same)
    pivot.parent = pivot_parent.parent
    
    # Step 6: Handle root and parent-child relationships (same logic)
    if pivot_parent.parent is None:
        # pivot_parent is the root, set the root to pivot
        tree.root = pivot
    elif pivot_parent == pivot_parent.parent.left:
        # pivot_parent is its parent's left child
        pivot_parent.parent.left = pivot
    else:
        # pivot_parent is its parent's right child
        pivot_parent.parent.right = pivot
    
    # Step 7: Set pivot's right child to be pivot_parent (inverted: right instead of left)
    pivot.right = pivot_parent
    
    # Step 8: Set pivot_parent's parent to be pivot (same)
    pivot_parent.parent = pivot


def ref_compare(node1, node2):
    """
    Reference function to compare two Red-Black trees for structural equality.
    Returns True if trees have the same structure and values.
    """
    # Both nodes are None/nil
    if (node1 is None or (hasattr(node1, 'val') and node1.val is None)) and \
       (node2 is None or (hasattr(node2, 'val') and node2.val is None)):
        return True
    
    # One is None/nil, the other isn't
    if (node1 is None or (hasattr(node1, 'val') and node1.val is None)) or \
       (node2 is None or (hasattr(node2, 'val') and node2.val is None)):
        return False
    
    # Compare values and colors
    if node1.val != node2.val or node1.red != node2.red:
        return False
    
    # Recursively compare children
    return (ref_compare(node1.left, node2.left) and 
            ref_compare(node1.right, node2.right))

run_cases = [
    (4),
]

submit_cases = run_cases + [
    (10),
]


def test_rotate(tree, node, reference_tree, reference_node, direction):
    print(f"Rotating {direction} at {node.val}...")
    print("-------------------------------------")
    if direction == "left":
        tree.rotate_left(node)
        ref_impl_left(reference_tree, reference_node)
    else:
        tree.rotate_right(node)
        ref_impl_right(reference_tree, reference_node)
    print("Expected Tree:")
    print("-------------------------------------")
    print_tree(reference_tree)
    print("-------------------------------------")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")
    return ref_compare(tree.root, reference_tree.root)


def test_rotations(tree, reference_tree):
    return (
        test_rotate(tree, tree.root, reference_tree, reference_tree.root, "left")
        and test_rotate(tree, tree.root, reference_tree, reference_tree.root, "right")
        and test_rotate(
            tree, tree.root.right, reference_tree, reference_tree.root.right, "left"
        )
        and test_rotate(
            tree, tree.root.left, reference_tree, reference_tree.root.left, "right"
        )
    )


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    reference_tree = RBTree()
    for user in users:
        tree.insert(user)
        reference_tree.insert(user)
    print("=====================================")
    print("Starting Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")

    if test_rotations(tree, reference_tree):
        print("Pass \n")
        return True
    print("Fail 1 \n")
    return False


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


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    print("\n".join(lines))


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
