# 10 Aug 2025
# Red Black Trees

#--------------------------------L1 : Unbalanced Trees --------------------------------

# O(n)

#--------------------------------L2 : Unbalanced Trees --------------------------------

# No

#--------------------------------L3 : Red-Black Trees --------------------------------

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current is not self.nil :
            parent = current
            if new_node.val < current.val :
                current = current.left 
            elif new_node.val> current.val :
                current = current.right
            else : return
        new_node.parent = parent
        if parent is None :
            self.root = new_node
        else :
            if parent.val < new_node.val :
                parent.right = new_node
            else : 
                parent.left = new_node


#--------------------------------L4 : Rules --------------------------------

# False

#--------------------------------L5 : Rules --------------------------------

# True

#--------------------------------L6 : Rotation --------------------------------

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent is self.nil or pivot_parent.right is self.nil:
            return
        
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left

        if pivot.left is not self.nil :
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent

        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent.parent.left == pivot_parent :
            pivot_parent.parent.left = pivot
        elif pivot_parent.parent.right == pivot_parent :
            pivot_parent.parent.right = pivot

        pivot.left = pivot_parent
        pivot_parent.parent = pivot
        
    def rotate_right(self, pivot_parent):
        if pivot_parent is self.nil or pivot_parent.left is self.nil:
            return
    
        # Pivot is now the LEFT child (inverted from right)
        pivot = pivot_parent.left
        
        # Set pivot_parent's LEFT child to pivot's RIGHT child (directions inverted)
        pivot_parent.left = pivot.right

        # If pivot's RIGHT child is not nil, update its parent (inverted from left)
        if pivot.right is not self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent

        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent.parent.left == pivot_parent:
            pivot_parent.parent.left = pivot
        elif pivot_parent.parent.right == pivot_parent:
            pivot_parent.parent.right = pivot
        
        # Set pivot's RIGHT child to pivot_parent (inverted from left)
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

        # don't touch below this line

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
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
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node


#--------------------------------L7 : Fix Insert --------------------------------

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
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
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Complete step 1: Call the balancing method after inserting
        self.fix_insert(new_node)


    def fix_insert(self, node):
        # While the current node is not the root and has a red parent
        while node != self.root and node.parent.red:
            # Identify the parent, grandparent, and uncle nodes
            parent = node.parent
            grandparent = parent.parent
            
            # If the parent is a right child of the grandparent
            if parent == grandparent.right:
                uncle = grandparent.left
                
                # If the uncle is red
                if uncle.red:
                    # Recolor the uncle and parent to black
                    uncle.red = False
                    parent.red = False
                    # Recolor the grandparent to red
                    grandparent.red = True
                    # Move up the tree by making the current node the grandparent
                    node = grandparent
                else:
                    # If the uncle is black
                    # If the current node is the left child of the parent
                    if node == parent.left:
                        # Move up the tree by making the current node the parent
                        node = parent
                        # Rotate right around the current node
                        self.rotate_right(node)
                        # Set the parent to be the current node's parent
                        parent = node.parent
                    
                    # Recolor the parent to black
                    parent.red = False
                    # Recolor the grandparent to red
                    grandparent.red = True
                    # Rotate left around the grandparent
                    self.rotate_left(grandparent)
            
            # If the parent is a left child of the grandparent
            else:
                uncle = grandparent.right
                
                # If the uncle is red
                if uncle.red:
                    # Recolor the uncle and parent to black
                    uncle.red = False
                    parent.red = False
                    # Recolor the grandparent to red
                    grandparent.red = True
                    # Move up the tree by making the current node the grandparent
                    node = grandparent
                else:
                    # If the uncle is black
                    # If the current node is the right child of the parent
                    if node == parent.right:
                        # Move up the tree by making the current node the parent
                        node = parent
                        # Rotate left around the current node
                        self.rotate_left(node)
                        # Set the parent to be the current node's parent
                        parent = node.parent
                    
                    # Recolor the parent to black
                    parent.red = False
                    # Recolor the grandparent to red
                    grandparent.red = True
                    # Rotate right around the grandparent
                    self.rotate_right(grandparent)
        
        # Recolor the root to black
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot


#--------------------------------L8 : Quiz --------------------------------

# No, it breaks rule #4

#--------------------------------L9 : Quiz --------------------------------

# True


