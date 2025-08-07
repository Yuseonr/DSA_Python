# 7 Aug 2025
# Queues

#--------------------------------L1 : What is Queue--------------------------------

# The absurdly long line of millennials without children waiting to get into DisneyLand

#--------------------------------L2 : Queue Class --------------------------------

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        if not self.items : return None
        return self.items.pop()

    def peek(self):
        if not self.items : return None
        return self.items[-1]

    def size(self):
        if not self.items : return 0
        return len(self.items)
    
    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"


#--------------------------------L3 : Queue Speed --------------------------------

# O(1)

#--------------------------------L4 : Queue Speed --------------------------------

# O(n) because you might have to pop all the items in the queue

#--------------------------------L5 : Queue Speed --------------------------------

# Because you have to move all the elements over by one index to make room for the new element.

#--------------------------------L6 : Match making queue--------------------------------

def matchmake(queue, user):
    name,action = user
    match action :
        case 'leave':
            queue.search_and_remove(name)
        case 'join':
            queue.push(name)
        case _ :
            None
    if queue.size() >= 4 :
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    else :
        return "No match found"

