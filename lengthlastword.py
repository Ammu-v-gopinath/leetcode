class Solution(object):
    def lengthOfLastWord(self, s):
        l=s.strip().split()
        lw=len(l[-1])
        return lw