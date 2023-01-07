#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
from heapq import heappush as hpush, heappop as hpop
class Solution():
    def flatten(self,root):
        curr = root
        def solve(dummy, root1, root2):
            if not root1:
                dummy.bottom = root2
                return
            if not root2:
                dummy.bottom = root1
                return
            if root1.data <= root2.data:
                dummy.bottom = root1
                solve(dummy.bottom,root1.bottom,root2)
            else:
                dummy.bottom = root2
                solve(dummy.bottom,root1,root2.bottom)
        def func(root):
            if not root: return None
            start = Node(-1)
            solve(start, root, func(root.next))
            root = start.bottom
            return root
        return func(root)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
        

def printList(node):
    while(node is not None):
        print(node.data,end=" ")
        node=node.bottom
        
    print()


if __name__=="__main__":
    t=int(input())
    while(t>0):
        head=None
        N=int(input())
        arr=[]
        
        arr=[int(x) for x in input().strip().split()]
        temp=None
        tempB=None
        pre=None
        preB=None
        
        flag=1
        flag1=1
        listo=[int(x) for x in input().strip().split()]
        it=0
        for i in range(N):
            m=arr[i]
            m-=1
            a1=listo[it]
            it+=1
            temp=Node(a1)
            if flag is 1:
                head=temp
                pre=temp
                flag=0
                flag1=1
            else:
                pre.next=temp
                pre=temp
                flag1=1
                
            for j in range(m):
                a=listo[it]
                it+=1
                tempB=Node(a)
                if flag1 is 1:
                    temp.bottom=tempB
                    preB=tempB
                    flag1=0
                else:
                    preB.bottom=tempB
                    preB=tempB
        obj=Solution()
        root=obj.flatten(head)
        printList(root)
        
        t-=1
            
# } Driver Code Ends