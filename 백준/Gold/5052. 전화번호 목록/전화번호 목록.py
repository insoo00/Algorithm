class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        
        cur.data = string

    def search(self, string):
        cur = self.head

        for char in string:
            if char in cur.children:
                cur = cur.children[char]
                if cur.data is not None and cur.data is not string:
                    return False
            else:
                return False
        
        if cur.data == string:
            return True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    strings = []
    for _ in range(n):
        string = input()
        strings.append(string)
        trie.insert(string)

    Flag = True
    for string in strings:
        if not trie.search(string):
            Flag = False
            break
    
    if Flag == True:
        print('YES')
    else:
        print('NO')
