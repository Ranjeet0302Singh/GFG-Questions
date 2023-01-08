#User function Template for python3

#User function Template for python3

class Solution:

    def countPairs (self, n, arr, k):

        arr.sort()

        

        dict1={0:1}

        diff=0

        total=0

        for i in range(1,n):

            diff+=abs(arr[i]-arr[i-1])

            if diff%k not in dict1:

                dict1[diff%k]=1

            else:

                dict1[diff%k]+=1

        total=0

        for i in dict1:

            countz=dict1[i]

            total+=(countz*(countz-1))//2

        

        return total





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        
        ob = Solution()
        print(ob.countPairs(n,arr,k))
# } Driver Code Ends