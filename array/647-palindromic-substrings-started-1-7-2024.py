"""
clarify:
palindrome - reads same forward and backwards
so if even length, you can traverse with left and right pointers and each character will be equal.
if odd length, you can traverse with left and right pointers and each character except the center will be equal

input:
s - a string

output:
number of palindromic substrings in s
so not the strings themselves, but the count of how many there are

edge case:
length is 1 - return true

strategy:
maybe use two pointers starting from left and right
i guess you could keep traversing while they are equal
but when to "close in"?
well, let's say you have something like "aaybbbxa"
so you start with left and right at ends
keep traversing because both = a
then you have left at a and right at x
they are not equal
so what do you do?
you could advance both, I suppose
so now left is at y and right is at b
well if we adbance both again
then left as at b and right is at the second b
and you would end up returning 2, instead of 3, which is wrong
so maybe i need to do this process of closing in multiple times from different indices?
so let's say if when i have left at a and right at x, I just bump...
oh, something just dawned on me
it might be smarter to start from the middle and work out than to start from the ends
so, let's start from the middle and work out for each index in the list
so we'd have an i idx to traverse, from which bloom a left and right pointer each iteration
so to run through it
we start with i at a, and can't go left, so we increment the number of palindromic substrings
then we have our right pointer check to the right of i, and see the letters are equal, so increment total again
then advance i so it's at the second a. a is equal to itself, with the left and right pointers starting at a the equal each other, so increment the total. avance i
right and left are equal, so increment total
oh, I'm starting to see a pattern. i don't know if we would really need a left pointer. we might be able to just use i and right. so maybe this becomes more of a sliding window
what if I cahnge input to:
"aaybobxa"? if we only had i and right and started at the left b, how would the right pointer know to keep advancing after the o?
I need to think about this more. circle back. I have two cases, really - odd and even length. some example inputs include:
"bob", "bccb"
for this odd case, I would have to have the behavior of starting from each index and sending out "feeler" pointers to the left and right.
for the even case, I would have to have the behavior of, at each index, doing the same as above, except before sendout out the feeler pointers, increment right by 1 so that i and right are adjacent.
we can say that we have encountered a palindrome if: right and left are equal. right and left should be equal in the beginning for both of the above cases
todo -
afterwards, consider "bba" and "abb" - the above approach works for these, too

test:
"bobbccb"
at index b
- odds case - increment, then can't go left
- evens case - move right ptr, but not equal
at index o - ditto
at index b
- odds case - self
- evens case - increment, then not equal
at index c
- ditto
at index b
- same as beginning

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i, char in enumerate(s):
            left, right = i, i
            # odds case
            while left >= 0 and right < len(s) and s[right] == s[left]:
                count += 1
                # expand
                left -= 1
                right += 1
            left, right = i, i + 1
            # evens case
            while left >= 0 and right < len(s) and s[right] == s[left]:
                count += 1
                # expand
                left -= 1
                right += 1
        return count
        
