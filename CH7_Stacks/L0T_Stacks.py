# 6 Aug 2025
# Stacks

#--------------------------------L1 : Stack --------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)


#--------------------------------L2 : Stack Speed --------------------------------

# All of them

#--------------------------------L3 : Stack Speed --------------------------------

# top

#--------------------------------L4 : Pop and Peek --------------------------------

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty() : return None
        return self.items[-1]

    def pop(self):
        if self.isEmpty() : return None
        return self.items.pop()


#--------------------------------L5 : Stack Review --------------------------------

# Any of these

#--------------------------------L6 : Stack Review --------------------------------

# O(n), because all other items need to be popped first

#--------------------------------L7 : Using Stack --------------------------------

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty() : return None
        return self.items[-1]

    def pop(self):
        if self.isEmpty() : return None
        return self.items.pop()

# Dump Answer not using stacks at al X_X

# def is_balanced(input_str):
#     open,close = 0,0
#     open_idx, close_idx = [],[]
#     for i,char in enumerate(input_str):
#         if char == '(':
#             open+=1
#             open_idx.append(i)
#         elif char == ')':
#             close+=1
#             close_idx.append(i)
#     if open != close :
#         return False
#     else :
#         for i in range(open):
#             if open_idx[i]>close_idx[i]:
#                 return False
#     return True

# Try using stack

def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() == None :
                return False
    return stack.size() == 0