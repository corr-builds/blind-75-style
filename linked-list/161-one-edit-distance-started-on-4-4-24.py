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

test:

"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def helper(s: str, t: str) -> bool:
            # edge case
            if s == "" and len(t) == 1:
                return True

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
                while j < len(s) and i < len(t):
                    if s[j] != t[i]:
                        if unequal_found:
                            return False
                        i += 1 # speed it up by 1
                        unequal_found = True
                    j += 1
                    i += 1
                # get pointers back in range
                j -= 1
                i -= 1

                if unequal_found:
                    if t[i] == s[j]:
                        return True # because the last character is an extra
                    else:
                        return False
                else:
                    if t[i] == s[j]:
                        return False
                    else:
                        return True

            return unequal_found
        return helper(s, t) or helper(t, s)


        
