class Solution(object):
    def missingNumber(self,a):
        
        n=len(a)
        totl = list(range(0, n+1))
        miss = sum(totl) - sum(a)
        return miss
