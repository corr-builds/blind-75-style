"""
clarify:
at most k distinct characters
so if k = 3 then
aaaeeeeooo has 3 distinct characters
you want to return the length of the longest
we can use a hash table

input:
s - str
k - int

output:
return longest substring of s that contains at most k distinct characters

edge case:
s is all the same character

strategy:
use a hash table to track the character to its count
use sliding window
when advancing left, update the count

test:
s=abcfb
k=3
{a:1, b:1, c:1}
window = abc
{a:1, b:1, c:1, f:1}
{ b:1, c:1, f:1}
window = bcf
{ b:2, c:1, f:1}
window = bcfb
return 4

"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        left = 0
        char_counts = defaultdict(int)
        longest = 0
        for right in range(len(s)):
            char_counts[s[right]] += 1
            while len(char_counts) > k: # advance left
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    del char_counts[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
        print(longest)
        return longest

        
