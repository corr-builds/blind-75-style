"""
clarify:
u want langest substring
w/ at most 2 distinct characters
aka, if keeping hashmap or set,
max size is 2

input:
s- a string

output:
length of the longest string

edge case:
there are only 1 or 2 characters in s
all characters in s are distinct

strategy:
consider using sliding window
assuming the window starts and ends
at 2 pointers, called left and right,
let right advance on each iteration
and let left advance when? when to shrink the window?
well, let's suppose we keep the window so that it always meets our invariant, the invariant being that there are at most 2 distinct characters. so let's try to shrink whil the window is valid, and only actually perform the shrink if shrinking would not cause the window to become invalid

well, actually i should talk this out. there are some options here
1. while the window is valid, move left
2. if advancing left will not make the window invalid, advance left
num 1 introduces the possibility that, at times, the window will not be valid inside the body of the while loop
num 2 does not
let's choose num 2
let's track unique characters in the window in a set

test:
s = abcc
set = []
left = 0
right points to a
set = [a]
longest = 1
right points to b
set = [a, b]
longest = 2
right points to c (first)
set = [a, b, c]
since the set is invalid (length greater than 2) move left <--- important!!!
set = [b, c]
right points to c (second)
set = [b, c]
set is valid, so update longest <-- important
longest = 3

soo after going thru it, let's advance left if, after advancing right, we get a window that is invalid

while solving - ohh, new complication. we do need a hashmap, for when we advance left
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest = 0
        distincts = defaultdict(int)
        left = 0
        for right in range(len(s)):
            distincts[s[right]] += 1
            while len(distincts) > 2: # window is invalid
                # advance left
                distincts[s[left]] -= 1
                if distincts[s[left]] == 0:
                    del distincts[s[left]]
                left += 1
            longest = max(longest, right - left + 1)

        return longest
        
