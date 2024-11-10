class Solution(object):
    def isValid(self, s):
        opcl = dict(('()', '[]', '{}'))
        list = []
        for i in s:
          
            if i in '([{':
                list.append(i)
            elif len(list) == 0 or i != opcl[list.pop()]:
                return False
        return len(list) == 0
      
        
        