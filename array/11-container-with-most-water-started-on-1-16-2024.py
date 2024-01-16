"""
clarify:
n vertical lines. endpoints of ith line are (i, o) and (i, height[i])
clarification:
assuming largest container is bordered by heights 7 and 8, only the shortest height matters. so you could assume those heights are both the height of the shortest.
what about the distance on the x axis that separates the two tallest? the x-wise distance would be the difference of the indices.
so now we've talked about how to calculate the size of the largest container assuming we'ce already found the heights that make it. but how do we find the heights that make it in the first place?
well, one idea for how we could do this is to keep a running record, and essentially update the largest container whenever we find one that is larger. in that case, maybe we could use a sliding window type thing. so let's say you have left and right pointers
we could keep left where it is, and advance right each time, updating if we ever find a larger container size. but when would we advance left?
hmm, no clear path
what else can we think about? how about - what are we trying to maximize? well, you want to maximize the area, and that means you want to maximize both the distance of the indices and the height, or the number at those indices.
I'm still kind of stuck, so I could try an example
1 x x x x x x x x 5 5 1
so container from 1 to 1 would hold more than container from 5 to 5 because the length (x-axis distance) times the height would be the largest
it's starting to seem like... I might actually might want to find every possible combination as a part of this problem? like find every possible container. that would mean starting from each index and then expanding all the way to the end. which wouldn't give a good time complexity. Complexity would be O(n^2)
Referencing a video now.
After referencing the video, I see that we can get O(n) time by using a two-pointer approach. We can use the two-pointer variant in which we start at the ends and move inwards. To know whether to advance left or right, we can advance whichever is shortest, since the shortest height is the bottleneck.
Is there another way I can think of articulating this that would help me in the future? Well, the above approach does maximize width, since it starts at the ends. And, in advancing either left or right based on which is the shortest, it also maximizes height.

input:
height - int array, length n

output:
using two lines that with x-axis form container, such that container contains the most water - todo clarify what this means
return the max amount of water a container can store

edge case:
length of height is 2
heights are all the same

strategy:
described above

test:
[1,8,6,2,5,4,8,3,7]
l at 1
r at 7
max = 8
l at 8
r at 7
max = 49
and so on...
stop when l == r

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        largest = 0
        while l != r:
            # update largest
            area = (r - l) * min(height[l], height[r])
            if largest < area:
                largest = area
            # move
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return largest
