# 7 Aug 2025
# Lingked Lists

#--------------------------------L1 : Lingked Lists--------------------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val


#--------------------------------L2 : Lingked List Vs List --------------------------------

# Iterating through all the nodes by following the 'next' references

#--------------------------------L3 : Lingked List Vs List --------------------------------

# Inserting/deleting items in the middle of the list

#--------------------------------L4 : Iterating--------------------------------

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        head_node = self.head
        while head_node is not None :
            yield head_node
            head_node = head_node.next
    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

#--------------------------------L5 : Add to Tail --------------------------------

class LinkedList:
    def add_to_tail(self, node):
        if self.head == None : 
            self.head = node 
            return
        else :
            last_node = None
            for cur_node in self:
                last_node = cur_node
            last_node.set_next(node) 

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


#--------------------------------L6 : Add to head --------------------------------

class LinkedList:
    def add_to_head(self, node):
        node.set_next(self.head)
        self.head = node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


#--------------------------------L7 : Lingked Lists Queues --------------------------------

class LinkedList:
    def add_to_head(self, node):
        node.set_next(self.head)
        self.head = node
        if not self.tail :
            self.tail = node

    def add_to_tail(self, node):
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None

    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


#--------------------------------L8 : Remove from QUeues --------------------------------

class LLQueue:
    def remove_from_head(self):
        if not self.head :
            return None
        old_head = self.head
        self.head = self.head.next
        if not self.head :
            self.tail = None
        old_head.set_next(None)
        return old_head

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


#--------------------------------L9 : Linked List Queues Quiz --------------------------------

# ...can have O(1) pushes and pops

#--------------------------------L10 : Linked List Queues Quiz --------------------------------

# When elements are added or removed from the first index of the array all the items need to shift, which takes O(n) time
