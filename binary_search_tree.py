class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
    def insert(self,val):
        if self.data:
            if self.data<val:
                if not self.right:
                    self.right=Node(val)
                else:
                    self.right.insert(val)
            else:
                if not self.left:
                    self.left=Node(val)
                else:
                    self.left.insert(val)
        else:
          self.data=val                           
    def print (self ):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()    
    def delete(self,val):
        if self.data<val:
            if self.right:
              self.right=self.right.delete(val)  
        elif self.data>val:
             if self.left:
              self.left=self.left.delete(val)    
        else:
          if not self.left and not self.right:
              return None
          if not self.left:
              return self.right
          if not self.right:
              return self.left
          succesor=self.right
          while  succesor.left:
              succesor=succesor.left
          self.data=succesor.data
          self.right=self.right.delete(succesor.data)
        return self         
                  
        
if __name__=="__main__":
    obj1=Node(5)
    obj1.insert(3)
    obj1.insert(1)
    obj1.insert(10)
    obj1.insert(4)
    obj1.print()
    obj1.delete(3)
    print("***")
    obj1.print()                            
                