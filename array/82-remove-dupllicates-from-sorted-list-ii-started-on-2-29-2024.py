"""
clarify:
delete all nodes that have duplicate numbers
aka keep only the nodes that are unique

input:
head - head of sorted ll

output:
head - now with all duplicate numbers deleted

edge case:
size 0 or 1 - immediately return head
all are duplicates
none are duplicates

strategy:
unique node - the val of the next pointer is different
duplicate node - the val of the next pointer is the same
let's say we encounter a duplicate node. if that's the case, say we traverse until we find that the next node is different or null
at this point, we would have to connect the previous node (make a virtual head?) to the next node that is different
then, finally, we could return vHead.next

test:
[1, 1, 1, 2, 3, 3]
vhead.next = 1 (put current pointer at vhead)
iterate until next is 2
connect vhead to 2 (current pointer is at vhead)
 [2, 3, 3]
note - we always want to keep track of a prev pointer that is unique, so we can only move prev (aka current) up until a node that is proven to be unique
since 2 is unique, advance current up to it
maybe we actually have a currentprev and a currentnext pointer
anyways, advance currentnext to null. connect 2 to null
[2]
return vhead.next

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vhead = ListNode()
        vhead.next = head
        currentprev = vhead
        currentnext = head
        while currentnext != None:
            # advance currentnext - there may or may not be duplicates. if there are not duplicates, perhaps we advance both ptrs and continue
            if not currentnext.next or currentnext.val != currentnext.next.val: # currentnext is at unique number
                currentnext = currentnext.next
                currentprev = currentprev.next
                continue
            while currentnext.next and currentnext.val == currentnext.next.val:
                currentnext = currentnext.next
            currentnext = currentnext.next # at this point, currentnext should be at the next digit or None
            # delete any duplicates
            currentprev.next = currentnext
            #print("connect " + str(currentprev.val) + " to " + str(currentnext.val if currentnext else None))
        return vhead.next
        
