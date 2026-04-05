# ============================================
# LeetCode #53 - Maximum Subarray
# Difficulty: Easy
# Topic: Arrays, Kadane's Algorithm
# Date: 04/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Find the contiguous subarray with the largest sum
# and return that sum.

# Example:
# Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6  (subarray [4, -1, 2, 1] = 6)

# APPROACH: Kadane's Algorithm
# At every step ask: start fresh OR continue?
# current = max(num, current + num)
# Track the best sum seen so far

# TIME:  O(n) — one single pass
# SPACE: O(1) — only two variables used

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]      # running total right now
        max_sum = nums[0]          # best total ever seen

        for num in nums[1:]:       # start from second element
            # start fresh OR continue — pick the bigger one
            current_sum = max(num, current_sum + num)
            # is this the best we've ever seen?
            max_sum = max(max_sum, current_sum)

        return max_sum

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected: 6
print(solution.maxSubArray([1]))                                 # Expected: 1
print(solution.maxSubArray([-5, -3, -1]))                       # Expected: -1

# ============================================
# WHAT I LEARNED
# ============================================
# - Kadane's Algorithm: max(num, current + num) at every step
# - If past is negative → drop it, start fresh
# - If past is positive → keep adding to it
# - Start at nums[0] not 0 (handles all-negative arrays)