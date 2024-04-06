"""
clarify:
word - sequence of non-space characters
no allocating extra space

input:
s - character array

output:
array with words reversed

edge case:

strategy:
maybe I have 1 ptr to "start at the end" and one pointer to track the words
pointer a goes until it finds a space or the start of the array
so does pointer b. then, pointer b traverses back, inserting each character at the insertion place (and deleting it from the original place), until it reaches a space (also insert the space) or the end of the array. each time you do an insert, in addition to incrementing the insertion pointer, increment a and b, so they'll still point to the same characters
the insertion pointer will initially be at index 0 (insert immediately before it) and each time after you insert a letter, it will be increment by 1 (so that it stays at the start of the word being added)

test:
s = ["t","k","o"," ","y","e"]
a is at e
b is at e
insertion is at t
a is at y
a is at " " so stop and
set b at " "
insert
["y","t","k","o"," ","e"]
increment a and b so that they're still at the same spot

and so on...
["y","e"," ","t","k","o"]

I think, ultimately, we can stop when b is at the last index

"""

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = b = len(s) - 1
        insertion = 0
        while b < len(s):
            # take a to the start of the next word
            while a >= 0 and s[a] != " ":
                a -= 1
            b = a
            # take b to read the word
            while b < len(s) and s[b] != " ":
                s.insert(insertion, s[b])
                # keep them pointing at the same letter, but advance b
                insertion += 1
                b += 2
                a += 1
                # clean up the character we inserted
                del s[a]
            # add the space
            if a >= 0 and s[a] == " ":
                s.insert(insertion, s[b])
                # keep them pointing at the same letter, but advance b
                insertion += 1
                b += 2
                a += 1
                # clean up the character we inserted
                del s[a]
        
