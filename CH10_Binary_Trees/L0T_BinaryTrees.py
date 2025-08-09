# 9 Aug 2025
# Binary Trees

#--------------------------------L1 : Trees --------------------------------

# Nope (Salah)
# Sure, why not

#--------------------------------L2 : Trees --------------------------------

# multiple, one

#--------------------------------L3 : Binary Trees --------------------------------

# 2

#--------------------------------L4 : Binary Trees --------------------------------

# Ordered: left child < parent < right child

#--------------------------------L5 : Insert Nodes --------------------------------


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val == val :
            return
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)  
            else:
                self.left.insert(val)     
                return
        if val > self.val:
            if self.right is None:
                self.right = BSTNode(val) 
            else:
                self.right.insert(val)    
                return


#--------------------------------L6 : Insert Review --------------------------------

# O(log(n))

#--------------------------------L7 : Min Max --------------------------------

class BSTNode:
    def get_min(self):
        if self.left is None:
            return self.val
        return self.left.get_min()

    def get_max(self):
        if self.right is None:
            return self.val
        return self.right.get_max()

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


#--------------------------------L8 : Delete --------------------------------

class BSTNode:
    def delete(self, val):
        current = self
        if current.val is None : return None

        if val < current.val :
            if current.left :
               current.left = current.left.delete(val)
            return current
        
        if val > current.val :
            if current.right :
                current.right = current.right.delete(val)
            return current
        
        if val == current.val :
            if current.right is None :
                return current.left
            
            if current.left is None :
                return current.right
            
            curr_right_oleft = current.right
            while curr_right_oleft.left is not None :
                curr_right_oleft = curr_right_oleft.left

            current.val = curr_right_oleft.val

            current.right = current.right.delete(curr_right_oleft.val)

            return current




    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val


#--------------------------------L9 : Deletion Review --------------------------------

# 14 levels

#--------------------------------L10 : Deletion Review --------------------------------

# O(log(n))

#--------------------------------L11 : PreOrder Traversal --------------------------------

class BSTNode:
    def preorder(self, visited):
        visited.append(self.val)
        if self.left and self.right:
            self.left.preorder(visited)
            self.right.preorder(visited)
        elif self.left :
            self.left.preorder(visited)
        elif self.right :
            self.right.preorder(visited)
        return visited

        

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

# bstnode_1 = BSTNode(3)
# bstnode_2 = BSTNode(4)
# bstnode_3 = BSTNode(2)

# bstnode_1.right = bstnode_2
# bstnode_1.left = bstnode_3

# print(f'bst1 ; left = {bstnode_1.left.val}')
# print(f'bst1 ; right = {bstnode_1.right.val}')
# print(bstnode_1.preorder([]))

#--------------------------------L12 : Post Order Traversal --------------------------------

class BSTNode:
    def postorder(self, visited):
        if self.left and self.right:
            self.left.postorder(visited)
            self.right.postorder(visited)
        elif self.left :
            self.left.postorder(visited)
        elif self.right :
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


#--------------------------------L13 : In Order Traversal --------------------------------

class BSTNode:
    def inorder(self, visited):
        if self.left :
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right :
            self.right.inorder(visited)
        return visited

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


#--------------------------------L14 : Node Exists --------------------------------

class BSTNode:
    def exists(self, val):
        if val == self.val :
            return True
        if self.right or self.left :
            if val < self.val :
                return self.left.exists(val)
            else :
                return self.right.exists(val)
        return False

        # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

#--------------------------------L15 : Height --------------------------------

class BSTNode:
    def height(self):
        if self.val is None :
            return 0
        left = 0 if self.left is None else self.left.height()
        right = 0 if self.right is None else self.right.height()
        return max(left,right)+1

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

