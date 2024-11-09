class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            x1=x
            r=0
            while(x>0):
                d=x%10
                r=r*10+d
                x=x//10
            if x1==r:
                return True
            else:
                return False
                

        
        