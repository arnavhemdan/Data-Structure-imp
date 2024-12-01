class trienode:
    def __init__(self):
        self.child = [None for i in range(26)] 
        self.is_word = False
        
        
class trie:
    def __init__(self):
        self.root = self.getnode()
        
    def getnode(self):
         return trienode()
    
    def insert(self, string):
        node = self.root
        l = len(string) 
        for i in range(l):
            index = ord(string[i]) - ord('a')
            if not node.child[index]:
                node.child[index] = self.getnode()
            node = node.child[index]
        node.is_word = True     
   
    def search(self, string):
        node = self.root
        l = len(string)
        for i in range(l):
            index = ord(string[i]) - ord('a')
            if not node.child[index]:
                return False
            node = node.child[index]
        return node.is_word
    def _delete(self, node, word, index):
        if index == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0
        
        char = word[index]
        if char not in node.children:
            return False
        
        should_delete_current_node = self._delete(node.children[char], word, index + 1)
        
        if should_delete_current_node:
            del node.children[char]
            return len(node.children) == 0
        
        return False
    
    def delete(self, word):
        return self._delete(self.root, word, 0)

 

if __name__ == "__main__":
    t1 = trie()
    t1.insert('anu')
    print(t1.search('anu'))  


  while True:
        ch = int(input("Enter your choice: 1. insert\n2. search\n3. delete\n"))
        if ch == 1:
            string = input("Enter string:")
            t1.insert(string)
        elif ch == 2:
            l = int(input("search  "))
             tring = input("Enter string:")
             t1.search(string)

            
        elif ch == 3:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
