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
hmm is there a more clever way i can do this? what if I just keep track of 1: the length of the window 2: the count of the char with the highest occurence and what that char is
then i could do lenght - count of highest occururing char
and if that's > k, then window is invalid

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
the additional changes are because a larger window can only be found anyways if we also find a larger max frequency, so we don't need to bother decrementing it.

let's try it out

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ht = defaultdict(int)
        longest = left = 0
        highest_char_count = 0
        for right, c in enumerate(s):
            ht[c] += 1
            if ht[c] > highest_char_count:
                highest_char_count = ht[c]
            while right - left + 1 - highest_char_count > k:
                ht[s[left]] -= 1
                if ht[s[left]] == 0:
                    del ht[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
        return longest
