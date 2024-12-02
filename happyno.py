class Solution:
    def isHappy(self, n):
        r = set() 
        while n != 1 and n not in r:
            r.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n==1
