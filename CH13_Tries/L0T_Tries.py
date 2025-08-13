# 13 Aug 2025
# Tries

#--------------------------------L1 : Tries --------------------------------

class Trie:
    def add(self, word):
        curr_level = self.root
        for char in word :
            if char not in curr_level :
                curr_level[char] = {}
            curr_level = curr_level[char]
        curr_level[self.end_symbol] =  True

        
    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


#--------------------------------L2 : Exist --------------------------------

class Trie:
    def exists(self, word):
        curr_dic = self.root
        for char in word :
            if char not in curr_dic : return False
            curr_dic = curr_dic[char]

        if self.end_symbol in curr_dic : return True 

        return False

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


#--------------------------------L3 : Prefix Matching --------------------------------

# Exact matching

#--------------------------------L4 : Prefix Matching --------------------------------

# The length of the word

#--------------------------------L5 : Words with Prefix --------------------------------

class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level : words.append(current_prefix)
        for char in sorted(current_level) :
            if char is not self.end_symbol :
                extend_current_prefix =  current_prefix + char
                self.search_level(current_level[char],extend_current_prefix,words)
        return words


    def words_with_prefix(self, prefix):
        matching_words = []
        curr_level = self.root
        for char in prefix :
            if char not in curr_level :
                return []
            curr_level = curr_level[char]
        return self.search_level(curr_level,prefix,matching_words)
        

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True


#--------------------------------L6 : Find Matches --------------------------------

class Trie:
    def find_matches(self, document):
        match = set()
        for i in range(len(document)) :
            curr_level = self.root
            for j in range(i,len(document)) :
                if document[j] not in curr_level :
                    break
                curr_level = curr_level[document[j]]
                if self.end_symbol in curr_level :
                    match.add(document[i:j+1])
        return match

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True


#--------------------------------L7 : Find Matches Review --------------------------------

# O(n * log(n)) where n is the length of the document (wrong)
# O(n * m)

#--------------------------------L8 :  Find Matches Review --------------------------------

# Because we would need to check every substring in the document, but using a Trie allows us to bail early on each given starting character

#--------------------------------L9 : Longest Common Prefix --------------------------------

class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ''
        while True :
            key = list(current.keys())
            if self.end_symbol in key :
                break
            if len(key) == 1 :
                prefix += key[0]
                current = current[key[0]]
            else :
                break
        return prefix
            

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True


#--------------------------------L10 : Advance Find Matches --------------------------------

class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations :
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
