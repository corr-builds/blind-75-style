"""
clarify:
find the longest substring without repeating characters
so "ss" would not be valid, but "se" would
considering the definition of this, we can say that a string has no repeating characters if the count of the number of times each character occurs in the string is 1
supposing you add a character to a string, each time, the string would be valid until you add another character that already exists in the string

input:
a string

output:
the substring without repeating characters that is longer than any other substrings without repeating characters

edge case:
length is 0 or 1

strategy:
we need to find the longest substring, so we will need to store all of the strings, and at the end return the longest
or, just update the longest string when we find one that is longer
in terms of knowing how to finish a substring, we can stop when a char is added that already exists in the substring. we can probably use a sliding window with hashmap for this
what do we do when we find where the substring ends? from which index do we start the algorithm again?
well, one way is to start again from the following index - is there a better way than that? hmm, seems good enough for now

I think actually I should make it so that when I encounter an index with the end pointer, I make the letter there a candidate to be added to the current window, rather than immediately adding it to the current window

example:
input: syshy
longest = sy
start again at y
window = y
window = ys
window = ysh
longest = ysh
window = shy
so, I want to get clear on one thing - you immeidately add new rightmost character at each iteration. then, just shrink window from start if you have a duplicate

seems like a game plan. let's see what we can do

"""

# I think there's an issue here. I'm not accounting for the smallest size. Size 1. This has the issue that if there is never any repeated character, it would not have desired behavior, because it's only tracking the longest string in the moment it finds a violation. instead, it should track the longest string to check if it has discovered a longer one either if a violation is found or if it gets to the end of the string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        longest_start = 0
        longest_end = 0
        hm = {}
        start = 0
        for end in range(0, len(s)):
            char = s[end]
            while end != 0 and (char in hm or end == len(s) - 1): #that means we have found the current longest substring
                if end - start > longest_end - longest_start: # update longest
                    longest_end = end
                    longest_start = start
                del hm[char]
                start += 1
            else:
                hm[char] = 1 # continue to grow the window
        return longest_start - longest_end


        
