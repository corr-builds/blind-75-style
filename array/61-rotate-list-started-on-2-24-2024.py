"""
just thinking of how things would move:

rotations past a full rotation are pretty irrelevant
what I mean to say is that if your list is length 5 and you want to rotate it 7 times, that's the same as rotating it 2 times
to get the above, just do 7%5 or k%length

and then, what about the final place of every item?
let's assume k is now fixed with the modulo
then each item's final place would be either current idx + k if that is less than the length of the list OR if it is not less than the length of the list, then the final place would be idx + k - length of the list. so for example if k = 1 and something is at the end of a list of length 5, then it would be at 5 + 1 - 5 = 1. ohh, that's wrong I need to subtract one so instaed of idx + k - length it is idx + k - length - 1 due to zero indexing

but then the question remaining is, if I know the index, how to create the linked list if I know the index of every item?

well let's say I do one initial pass thru the ll just to get the length.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
well what could you do to get the above rotation? make 4 the head, make 5 point to 1 instead of null, and make 3 point to null instead of 4j
so that looks like
head=1->2->3->4->5
head=5->1->2->3->4->5 make 5 point to 1 (cycle)
head=4->5->1->2->3->4 (cycle)
head=4->5->1->2->3->null(no cycle)
summarizing the above in words:
make the end point to the beginning
make the new head the new head
make the new end the new end

well, some trouble with that is that ther could be duplicate numbers in the input, but since i'm thinking about cycles, I got a new idea
one thing that i could do to solve this is do the modulo technique i mentioned earlier, then connect the end to the beginning of the list to create a cycle, then move k (modulod) times, then make that the head and traverse n nodes where n is the length of the list, then make the next node null

plus 2 min to solve
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases
        if not head or head.next == None:
            return head
        # traverse to end of list to get length
        l = 1
        current = head
        while current.next:
            l += 1
            current = current.next

        k = k % l
        if k == 0:
            return head

        # connect tail to head
        current.next = head

        k = l - k + 1
        while k > 0:
            k -= 1
            current = current.next
        # now at the new head, traverse for length of list, then snip it
        head = current

        while l > 1: # greater than 1 not 0 to allow for where we'll land (at next)
            l -= 1
            current = current.next
        current.next = None
        return head
        
