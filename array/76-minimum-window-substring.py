"""
clarify:
s and t are strings
s is length m
t is length n
return "minimum window substring" of s such that: every character in t (including duplicates) is included in the window. else if there is no such substring, return ""
eg
BANC might get returned as a substring of s if t is ABC
eg
a might get returned as a substring of s if t is a
eg
"" might get returned if t is aa and s is a, since both a's from t must be included in the window
The answer will be unique - explore more of what that means
I suppose that this means the following:
if you had BANC in s and also BNCA in s, and t was ABC, then that would not be a valid case. they seem to be saying that there will only be one minimum window substring
so for what that means for me
I'm not looking for an array of return values in the case of multiple minimum window substrings because that would be an invalid test case. I am looking only for one: the ONLY minimum window substring, which either exists in s or does not exist in s

input:
s - str
t - str

output:
minimum window substring of s such that every character in t, including duplicates, is included in the window (keep in mind that the order of the characters in t does not matter)

edge case:
the minimum window substring does exist in s
the minimum window substring does not exist in s
t 2 characters long and s is one character long. they are the same character. this is invalid because duplicates count

strategy:
it seems like there's quite a bit to break down here. let's consider...
well, maybe I should start with the simpler case. that is, let's ignore the duplicates for now
how do I tell that for s="ab" and t="ab", that s contains t?
well, we could represent this as a mapping from characters to counts
let's say I first scan t, gathering a mapping of each character to the number of times it appears in the string
then, i could go through s, and each time I encounter a letter, create or increment a map entry
(okay, so maybe i am not ignorning duplicates yet, because the mapping and count tracking would handle this)
well, that's a pretty simple case. but what about s="acb" and t="ab"?
well, we could still use mappings. but the way we iterate over s would differ. first we notice we have a, then we find c and do not put it in the map since it doesn't exist in the map for string t. then we find b, and since that exists in the map of string t, we have our valid minimum window substring
BRIEF ASIDE - THE CASE WHERE IT DOES NOT EXIST
supposing s = "ac" and t="ab" we could return "" because a matching mapping was never satisfied
then the more ineresting question - what if s is really, really long?
we'd probably use something like sliding window
when do we increment the end pointer of the window? each iteration
when do we increment the start pointer of the window? since we're trying to find the minimum, we could increment it while the chars in the window represent a valid mapping
if/when we find a valid mapping, we will just store the pointers of where it is located.

test:
s = "caobyyyycob" t = "cb"
tMap = {c: 1, b:1}
endChar = c
sMap = {c: 1}
endChar = a
sMap = {c: 1, a:1}
endChar = o
sMap = {c: 1, a:1, o:1}
sMap = {c: 1, a:1, o:1, b:1}
minWinSub = caob
sMap = {c: 1, a:1, o:1, b:1, y:4}
sMap = {c: 2, a:1, o:1, b:1, y:4}
startChar = b
sMap = {c: 1, a:1, o:2, b:1, y:4}
and so on...

I'm feeling pretty confident about this mechanism, so I'm going to implement it. let's go. wish me luck, me :) :D
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): # edge case
            return ""
        tMap = defaultdict(int)
        sMap = defaultdict(int)
        left = 0
        minWinStart = 0
        minWinEnd = float("inf")
        def meets_invariant(s_map, t_map):
            # it would meet the invariant if we can subtract each item in t from s without coming up empty
            t = t_map.copy()
            s = s_map.copy()
            for k, v in t_map.items():
                # hmm, is there a better way to do this? could I some how keep track of whether it meets the invariant as we iterate? for now I'll define this. I'll come back
                for i in range(v):
                    if k in s:
                        s[k] -= 1
                        if s[k] == 0:
                            del s[k]
                    else:
                        return False
                return True

        # put the chars in t into a mapping
        for char in t:
            tMap[char] += 1
        for right in range(len(s)):
            sMap[s[right]] += 1
            while meets_invariant(sMap, tMap):
                # advance left
                sMap[s[left]] -= 1
                if sMap[s[left]] == 0:
                    del sMap[s[left]]
                left += 1
            if meets_invariant(sMap, tMap): # todo define

                # check if min needs updated
                if minWinEnd - minWinStart + 1 > right - left + 1:
                    minWinStart = left
                    minWinEnd = right
        return "" if minWinEnd == float("inf") else s[minWinStart:minWinEnd + 1]
        
