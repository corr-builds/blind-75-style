"""
clarify:
find length of longest substring without repeating characters
so in other words, the moment a character which has already been encountered is encountered, the current substring is invalid

input:
s - str

output:
Length of the longest substring without repeating characters

edge case:
length is 0
all characters are the same
all charactrs are unique

strategy:
well, it seems straightforward. track each character you've encountered before, perhaps in a hashtable for O(1) access, then window becomes invalid when duplicate is encountered
use sliding window
so - when to advance left pointer of window?
so if you have "abcabcd"
the moment you encounter the second "a", you would adbance left to point to the duplicate character which was encountered

test:
"abcabcd"
map = {}
i'm not going to iterate, but at some iteration we'd have "a", "b", and "c" in the map, and at another point we'd have that and also "d"
let's store just 1 as the value

here we go

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        longest = left = 0
        for right, c in enumerate(s):
            # if window would be invalid, make window valid
            # clean up ht
            while c in ht:
                del ht[s[left]]
                left += 1
            ht[c] = 1
            longest = max(longest, right - left + 1)
        return longest
        
