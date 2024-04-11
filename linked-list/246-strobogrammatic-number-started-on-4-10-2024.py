"""
for each number, store its opposite, which is strobogromattic. then, 2ptr to the ceneter
1 - 1
2 - x
3 - x
4 - x
5 - 5
6 - 9
7 - x
8 - 8
9 - 6
0 - 0
"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo = {"1":"1", "6":"9", "8":"8", "9":"6", "0":"0"}
        l = 0
        r = len(num) - 1
        while l <= r:
            if num[l] in strobo:
                if strobo[num[l]] != num[r]:
                    return False
            else:
                return False
            l += 1
            r -= 1
        return True
        
