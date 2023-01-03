#User function Template for python3
#User function Template for python3

import copy

class Solution:

    def longestSubseq(self,H,N):

        dp=[0]*N

        size=0

        for x in H:

            i,j=0,size

            while i!=j:

                m=(i+j)//2

                if dp[m]<x:

                    i=m+1

                else:

                    j=m

            dp[i]=x

            size=max(i+1,size)

        return size

        

        

    def removeStudents(self, H, N):

        # code here

        s1=self.longestSubseq(H,N)

        ans=N-s1

        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends