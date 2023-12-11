"""
clarify:
so basically a string (is input)

input:
s - str

output:
all 10-letter-long sequences (substrings) that occur more than once. may be returned in any order

edge case:
input is less than 20 characters (not possible to have 2 duplicates of 10)

strategy:
the obvious way -
find all 10 letter long substrings
for each, check if it has an equivalent
a better way?
sliding window?
well, in the case, the window would have to not change size. so always be of length 10. in a hash table, we can store a mapping from the string to to its count
then, at the end, return all entries where count is 2 or greater
side note <- this means that sliding window can also be for a window of a fixed size

test:
a..a,b..b,a..a
{a..a:2,b..b:1}
return a..a

"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        sequences = set()
        result = set()
        for right in range(9,len(s)):
            window = s[left:right + 1]
            if window in sequences:
                result.add(window)
            sequences.add(window)
            # at end, bump left
            left += 1
        return result
