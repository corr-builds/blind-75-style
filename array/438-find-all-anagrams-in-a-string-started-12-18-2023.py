"""
clarify:
so an anagram is a rearangement of the letters
so one way to do this is generate all the anagrams of p, then search for each of them in s
there's got to be a better way to do this
well, suppose we use sliding window
I suppose we could maintain some sort of list of the letters in p, or maybe a map of the letters in p to their count
then when we could also have a map that represents the count of characters in our window
when we expand the window, we could add a character to the window hashmap.
- if that character that was added to the window hashmap does not exist in p's hash table, then window is invalid, and we should shrink until it's valid
- the window is also invalid if the character count in the actual window exceeds the count for that character in p's hash table

input:
s - str
p - str

output:
all start indices of p's anagrams in s
can be in any order

edge case:
s == p

strategy:
the strategy was pretty much outlined above
assignment for after: what is the big O of checking whether a key exists in a hash table? (dict)

test:
s = "aab"
p = "ab"
p_dict = {a:1, b:1}
window = {a:1}
window = {a:2}
it's invalid so
window = {a:1}
window = {a:1, b:1}
window == p_dict, so
add to our result list
result = [1] <- start index

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        goal = defaultdict(int)
        window = defaultdict(int)
        for i in range(len(p)):
            goal[p[i]] += 1
            window[s[i]] += 1
        result = [0] if goal == window else []
        left = 0
        right = len(p)
        while right < len(s):
            window[s[right]] += 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
            right += 1
            if goal==window:
                result.append(left)
        return result
        
