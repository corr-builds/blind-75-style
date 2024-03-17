"""
task:
get from start of word to end of word
append the word to a new string

ptrs:
- start
- end

"  hello world  "

better runtime:
Whenever we find the start of a word, read to the end of the world. Then, append to and of current string, preceded by a space (if the output string is not empty)
so:
1 ptr for strt of string (left) 1 ptr for end of string (right)

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        start = end = 0
        while start < len(s) and end < len(s):
            if s[start] == " ":
                start += 1
                continue
            end = start
            while end < len(s) and s[end] != " ":
                end += 1
            rev = s[start:end] + " " + rev
            # set up next iter
            start = end # a whitespace

        if rev != "":
            rev = rev[0:len(rev) - 1] # cut trailing space
        return rev
