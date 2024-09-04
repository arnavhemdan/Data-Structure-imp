class sqrtd:
    def __init__(self,arr,size):
        self.arr=arr
        self.size=size
        self.newsize=int(size**0.5)
        self.b=[0]*self.newsize
        self.logic()
       
        
    def logic(self):
        for i in range(self.size):
            self.b[i//self.newsize]+=self.arr[i]

    def update(self,newvalue,i):
        diff=newvalue-self.arr[i]
        self.arr[i]=newvalue
        self.b[i//self.newsize]+=diff

    def display(self):
        for i in self.arr:
            print (i, end=' ')
        print()
    def rangesum(self,l,r):
        su=0
        bl=l//self.newsize
        br=r//self.newsize
        if bl==br:
            for i in range(l,r+1):
                su+=self.arr[i]
        else:
         i=l
         while i//self.newsize ==bl:
            su+=self.arr[i]
            i+=1
         i=r
         while i//self.newsize==br:
            su+=self.arr[i]
            i-=1
         for i in range(bl+1,br):
             su+=self.b[i]
        print(su)    

if __name__=='__main__':
    n=int(input("enter size of array"))
    arr = list(map(int, input("Enter all elements separated by space: ").split()))  
    obj1=sqrtd(arr,n)
   
    while 1:
        print("Enter your choice:\n1. Update\n2. Range sum\n3. Display\n4. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            index = int(input("Enter index: "))
            value = int(input("Enter value: "))
            obj1.update(value, index)
        elif ch == 2:
            l = int(input("Enter starting range: "))
            r = int(input("Enter ending range: "))
            obj1.rangesum(l,r)
        elif ch == 3:
            obj1.display()
        elif ch == 4:
            break
        else:
            print("Invalid choice. Please try again.")
    
    
    
