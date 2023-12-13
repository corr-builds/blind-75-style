"""
clarify:
return len
get longest substring where count of each char >= k
so a hash table comes to mind
and a sliding window
supposing we keep track of the counts of chars in our window
the only issue might be the point in the loop where we check if EACH character has a frequency greater than or equal to k
because that introduces extra looping, potentially of size O(n) in the worst case of a large window
how might we improve that?

input:
s - str
k - int

output:
len of longest substring where count of each char >= k,
else 0 if does not exist

edge case:
the longest substring does not exist, so return 0
k > len(s). if that is the case, we can immediately return 0

strategy:
continuing from "clarify". can we eliminate that inefficiency?
well, fundamentally, there's one kind of true/false thing that we care about for the window. it only meets our invariant if EVERY character in the window is >= k. So in a sense, what we might be able to do is track the count (frequency) of the least commonly ocurring character
continuing the thought experiment...
let's suppose k=2 and our ht looks like
{'a':1}
we can do
least_common_count = 1
and we check that variable, instead of checking the entire hash table, to determine whether the window is valid (meets the invariant)
continuing
maybe s = "abb..."
so we have
{'a':1, 'b':2}
when we update the count of b to be 2, we set
least_common_count = 2 <-- correction: from now on, I will be referring to this variable as "most_common_count" because if the most commonly ocurring character is >= k, we'll know the window is valid. BUT - how would we know when to update this variable? obviously, if we update the count of a character, and it is greater, then we can update this. but also, when would we decrease it? well, it wouldn't work to simply decrement it if the value you decremented was previously == to most_common_count, because there could be multiple characters that had that same count. so, we could introduce a second variable, count_equal_to_most_common_count, that we increment and decrement. we increment if updating a new -> stopping my thinking right here. I need to regroup
and so we know that the window is valid
we advance left
{'a':1, 'b':2}
regroup:
could I use sorting? suppose I maintain the hash table, but also store the values in a sorted list. I could make these 2 data structures "parallel" so the ht entry at an index corresponds to the value at that index of the list. except, that doesn't make sense if I'm sorting things. because indexes are prone to change. in that case... is it possible to have a hash table (dict) sorted by value?
if I could do that, what would be the benefit?
well, if I could sort by values in ascending order, then I would always know, by checking the first element, whtether the window was valid (if first element >= k)
the problem here is that it looks like in python, there's no dict structure that maintains sorted order by value
coming back to this after some time away... if ANY character in the window has a count below k, then the window is invalid.
coming back again... okay. i don't think it's actually brute force because the max size of the hash table would be 26 since english has 26 characters

test:
I think I walked thru enough of a test above
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        longest = left = 0
        ht = defaultdict(int)
        for right in range(len(s)):
            ht[s[right]] += 1
            # make the window meet invariant
            def meets_invariant():
                print(ht)
                for v in ht.values():
                    if v < k:
                        return False
                return True
            while not meets_invariant():
                # advance left
                ht[s[left]] -= 1
                if ht[s[left]] == 0:
                    del ht[s[left]]
                left += 1

            longest = max(longest, right - left + 1)
        return longest
        
