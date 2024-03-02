"""
clarify:
reanage list, relative order within partitions, so that all nodes les than x come before nodes greater than or equal to x
example:
nodes less than 3 should be before nodes greater than ore equal to 3
move both 2s to the left partition since they are less than 3
move 4, 3, and 5 so that they are in the same order but in the right partition since they are greater than or equal to 3
so basically
left part = < 3
right part = >= 3
how to do that kind of node movement
well, we could just scan thru the list once, noting the values of all of the nodes
then we could create a new ll that puts them into order
so in fact, maybe as we go, we put them into either left or right lists
then use those lists to create new ll

input:
head - head of ll
x - node value

output:
head

edge case:
head is null

strategy:
see above

test:
iterate once, producing lists
l = [1, 2, 2]
r = [4, 3, 5]
create a new ll with nodes that have values in l, then nodes that have values in r

---------------
is there a way to do this in one pass?
what would that look like with the example?
1 is less than 3, so keep at left
hm.. could I do the l and r thing the same way I did with lists, but instead start l and r virtual heads that are heads of linked lists?
so starting that problem from the top
lvhead = 0
rvhead = 0
1 is less than 3, so lvhead.next = 1
rvhead.next = 4
and so on...
okay I'll just try solving this way reqlly quick

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        vleft = ListNode()
        vright = ListNode()
        l = vleft
        r = vright
        while head:
            if head.val < x:
                l.next = head
                l = l.next # update l tail
            else:
                r.next = head
                r = r.next # update r tail
            head = head.next
        l.next = vright.next
        r.next = None
        return vleft.next
        
