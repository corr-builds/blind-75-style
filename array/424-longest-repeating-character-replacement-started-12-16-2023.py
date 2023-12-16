"""
clarify:
change any char of string to other char up to k times
hmmm, so another way to think of this is that for a substring consisting of the same character, you can have up to k characters that are not that character
I am thinking we could use sliding window
and how to track?

input:
s - str
k - integer

output:
length of longest substring w/ same letter after up to k replacements

edge case:
string length is 1 or k + 1

strategy:
so how to track?
well you could track characters to their count in a hashtable
and under what invariant would the hash table be valid?
it would be valid if there were up to k + 1 elements and 1 of those characters had a count of N and all others had a count of 1
or if there were k elements and 1 of those characters had a count of N and all others had a count of 1 except 1 which had a count of 2
so another way to kind of think of this:
let's say you take the character in the ht that has the highest count. the ht will be valid if the remaining items are no greater than k in number and their counts sum up to no greater than k
so there's our invariant. and in terms of when to expand our window?
well, if we have a left and right pointer, we can say the window will be of varying size
and so we can advance the left pointer while the window does not meet the invariant, so that afterwords, the window will meet the invariant

test:
s = "abcaac", k = 1
ht = {}
ht = {a:1}
ht = {a:1, b:1}
ht = { b:1}
ht = { b:1, c:1}
ht = { c:1, a:1}
ht = { c:1, a:2}
ht = {  a:2}
ht = {  a:2, c:1}
so return right - left + 1, aka 3

let's try it out

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ht = defaultdict(int)
        longest = left = 0
        for right, c in enumerate(s):
            ht[c] += 1
            def meets_invariant(k_max):
                # todo improve?
                highest_count = 0
                highest_count_char = ""
                if len(ht) > k_max + 1:
                    return False
                for k, v in ht.items():
                    if v > highest_count:
                        highest_count = v
                        highest_count_char = k
                sum = 0
                for k, v in ht.items():
                    if k != highest_count_char:
                        sum += v
                if sum > k_max:
                    return False
                return True
            while not meets_invariant(k):
                ht[s[left]] -= 1
                if ht[s[left]] == 0:
                    del ht[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
        return longest
