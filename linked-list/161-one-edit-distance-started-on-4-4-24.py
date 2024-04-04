"""
clarify:
edit distance apart -
- insert 1 char
 - s is 1 char shorter than t
 - when traversing s and t with pointers, the values at the two pointers can be unequal once
 - if the values are unequal, increment the pointer that is moving allong the longer string
- delete 1 char
 - s is 1 char shorter than t
 - when traversing s and t with pointers, the values at the two pointers can be unequal once
 - if the values are unequal, increment the pointer that is moving allong the longer string
- replace 1 char
 - s is equal length to t
 - when traversing s and t with pointers, the values at the two pointers can be unequal once
after any of the above, s would equal t

changing the second approach - for diff lengths:
- traverse both simultaneously. if chars found that are not equal, increment ptr on the longer AND also use the counter of 1 to determine if this has been encountered before

input:
s, t - strings

output:
true - if s and t are edit distance apart
else, false

edge case:

strategy:
re-thinking -
let's say we have both short and long string - what makes the 2 of them valid?
  that when we have travelled to the end of both of them, we have only encountered 1 character that is different
  what do we do when we encounter a character that is different? we skip it
  what if we ecnounter a character that is different and we had previously skipped a character? we return false
  what if we do not encounter a chracter that is different? well, let's say we're traversing based on the long string. if we're on the last char of the long string and the index on the short string is out of bounds, then we can actually immediately return true, since then there is 1 "difference"

test:

"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # edge case
        if s == "" and len(t) == 1:
            return True
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        unequal_found = False
        if len(s) == len(t):
            i = 0
            for j in range(len(s)):
                if s[j] != t[i]:
                    if unequal_found:
                        return False
                    else:
                        unequal_found = True
                i += 1
        elif len(s) + 1 == len(t):
            i = 0
            j = 0
            while i < len(t):
                if i == len(t) - 1 and j == len(s):
                    if unequal_found:
                        return False
                    return True
                if t[i] != s[j]:
                    if unequal_found:
                        return False
                    unequal_found = True
                    j -= 1
                i += 1
                j += 1


        return unequal_found


        
