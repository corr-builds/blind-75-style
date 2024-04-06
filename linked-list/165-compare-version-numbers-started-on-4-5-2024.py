"""
clarify:
compare versions
revisions joined by .
revision - digits, maybe with leading zeroes. at least 1 character

compare in left to right order
revisions compared using integer value ignoring leading zeroes

input:
version1, version2

output:
-1 if version1 < version2
1 if version1 > version2
else 0

edge case:
they are equal, they are equal after ignoring leading 0s

strategy:
how to compare individual revision:
maybe we go right to left between each dot, multiplying the digit by 10 each time to account for place value, and storing the values
but no, I think it'll be more efficient if we have a solution that compares left to right. for comparing left to right:
let's say we traverse up to the first period. the index of the first period will tell us the highest place value. then we can have another pointer multiply the current digit by the highest place value, then decrement by 1. at each step compare, and if 1 version is higher than the other, then we can exit
if we reach the end have not returned yet, we can assume they are equal

actually about finding the place value, i guess we'd have to move the slow pointer to the previous period at the ery end, so max place value can be v1_fast - v1_slow, etc

test:
version1 = "0.1", version2 = "1.1"
v1_fast = 1
v1_slow = 0
v1_place = 1
v2_fast = 1
v2_slow = 0
v2_place = 1

current sum at v1 = 0*1 = 0
decrement v1_place
current sum at v1 = 1*1 = 1
decrement v2_place
is 1 greater than the other? yes, v2
so return -1

what about the case where they have a different number of revisions?
let's say they are all equal, except that version2 has 1 more revision, and it has a greater value?

well, I guess after we finish iterating both, we could iterate over the remainder of the longer one that is uniterated. if its value is non-zero, return that that one is larger. else, return 0
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 += "."
        version2 += "."
        print(version1)
        print(version2)
        v1_fast = 1
        v2_fast = 1
        v1_slow = 0
        v2_slow = 0
        while v1_fast < len(version1) or v2_fast < len(version2):
            while v1_fast < len(version1) and version1[v1_fast] != ".":
                v1_fast += 1
            while v2_fast < len(version2) and version2[v2_fast] != ".":
                v2_fast += 1
            # print(v1_fast)
            # print(version1[v1_slow:v1_fast])
            # print(v2_fast)
            # print(version1[v2_slow:v2_fast])
            # print("--------")
            rev1 = 0 if v1_fast == len(version1) else int(version1[v1_slow:v1_fast])
            rev2 = 0 if v2_fast == len(version2) else int(version2[v2_slow:v2_fast])
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
            v1_fast += 1 if v1_fast < len(version1) else 0
            v2_fast += 1 if v2_fast < len(version2) else 0
            v1_slow = v1_fast
            v2_slow = v2_fast

        return 0

        
