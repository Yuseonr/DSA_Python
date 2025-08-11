# 11 Aug 2025
# Hashmaps

# --------------------------------L1 : Hashmaps -------------------------------

# Arrays

# --------------------------------L2 : Hashmaps --------------------------------

# O(n)

# --------------------------------L3 : Hashmaps --------------------------------

# string, any (Wrong)
# Hashable

# --------------------------------L4 : Hash Function --------------------------------
import random

class HashMap:
    def key_to_index(self, key):
        return sum([ ord(char) for char in key ]) % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

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



# --------------------------------L5 : Insert --------------------------------

class HashMap:
    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = (key,value)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final

# --------------------------------L6 : Get --------------------------------

class HashMap:
    def get(self, key):
        idx = self.key_to_index(key)
        if self.hashmap[idx] :
            return self.hashmap[idx][1]
        else : raise Exception ("sorry, key not found")

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final


# --------------------------------L7 : Hashmaps review --------------------------------

# They would collide because they have the same unicode sum

# --------------------------------L8 : Hashmaps review --------------------------------

# It allocates a large List in memory even when we haven't filled all the indexes

# --------------------------------L9 : Resizing --------------------------------

class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]

        if self.current_load() < 0.05 :
            return
        
        past_hash = self.hashmap
        self.hashmap = [None for _ in range (len(past_hash)*10)]

        for bucket in past_hash :
            if bucket is not None :
                key, value = bucket
                idx = self.key_to_index(key)
                self.hashmap[idx] = (key,value)

    def current_load(self):
        if len(self.hashmap) == 0 :
            return 1
        filled_bucket = 0
        for stuff in self.hashmap :
            if stuff :
                filled_bucket += 1
        return (filled_bucket/len(self.hashmap))
       

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final


# --------------------------------L10 : Linear probing --------------------------------

class HashMap:
    def insert(self, key, value):
        idx = self.key_to_index(key)
        original_idx = idx
        first_iter = True
        while self.hashmap[idx] is not None and self.hashmap[0] != key :
            if not first_iter and idx == original_idx:
                raise Exception("hashmap is full")
            idx = (idx + 1) % len(self.hashmap)
            first_iter = False
        self.hashmap[idx] = (key,value)

    def get(self, key):
        idx = self.key_to_index(key)
        original_idx = idx
        first_iter = True
        while self.hashmap[idx] is not None :
            if self.hashmap[idx][0] == key :
                return self.hashmap[idx][1]
            if not first_iter and idx == original_idx :
                raise Exception("sorry, key not found")
            if self.hashmap[idx][0] != key :
                idx = (idx + 1) % len(self.hashmap)
            first_iter = False
        raise Exception("sorry, key not found")

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
