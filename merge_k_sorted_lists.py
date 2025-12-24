# https://leetcode.com/problems/merge-k-sorted-lists/
# Time Complexity- O(N*k) Space Complexity- O(1)

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists):
        # check the base case
        if len(lists) == 0:
            return None
        # create a dummy node
        dummy = ListNode(0)
        curr = dummy
        # create an empty list
        minHeap = []
        # iterate over the lists
        for lst in lists:
            if lst is not None:
                 # add the list into the minHeap which has the property of heap,that is all the nodes are ordered in the ascending order
                heapq.heappush(minHeap, NodeWrapper(lst))

        # iterate over the heap
        while minHeap:
            # pop function return the smallest elememnt from the heap
            min_node = heapq.heappop(minHeap)
            # curr is having the dummy node so recently poped min node is adding next to the dummy
            curr.next = min_node.node
            # this moves curr forward to the newly added node
            curr = curr.next
            # check the condition if the next node is present
            if min_node.node.next is not None:
                # add into the heap
                heapq.heappush(minHeap, NodeWrapper(min_node.node.next))

        return dummy.next
    


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

solution = Solution()
merged = solution.mergeKLists(lists)
print_list(merged)
