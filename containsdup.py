class Solution(object):
    def containsDuplicate(self, n):
        for i in range(0,len(n)):
            for j in range(i+1,len(n)):
                if(n[i]==n[j]):
                    return True
                
        return False
