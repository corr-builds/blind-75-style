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

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        l, r = [], []
        while head:
            if head.val < x:
                l.append(head.val)
            else:
                r.append(head.val)
            head = head.next
        vhead = prev = ListNode()
        for val in l:
            current = ListNode(val, ListNode())
            prev.next = current
            prev = current
            current = current.next
        for val in r:
            current = ListNode(val, ListNode())
            prev.next = current
            prev = current
            current = current.next
        prev.next = None
        return vhead.next
        
