# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Time complexity- O(n log (n - k)) Space Complexity- O(n-k)

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        # create a list
        pq = []
        # iterate through the given nums
        for i in range(len(nums)):
            # to add into the list while maintaining the property of the heap use the function called 'heappush'
            # adding the element into the created empty list
            heapq.heappush(pq, nums[i])
            # if the lenght of the list is greater than k
            if len(pq) > k:
                # pop the smallest element
                heapq.heappop(pq)
        # return the 0th index value
        return pq[0]


sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4],  2))