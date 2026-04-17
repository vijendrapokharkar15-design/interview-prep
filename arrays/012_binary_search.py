# ============================================
# LeetCode #704 - Binary Search
# Difficulty: Easy
# Topic: Arrays, Binary Search
# Date: 11/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Given a sorted array and target, return index of target.
# If not found return -1.

# Example:
# Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4

# APPROACH: Binary Search
# Set left and right boundaries
# Find middle point every step
# If target found → return mid
# If target > mid → search right half (left = mid+1)
# If target < mid → search left half (right = mid-1)
# If left > right → not found → return -1

# TIME:  O(log n) — eliminate half each step
# SPACE: O(1)     — only three pointers used

class Solution:
    def search(self, nums, target):
        left = 0                      # start of search space
        right = len(nums) - 1         # end of search space

        while left <= right:          # while search space exists
            mid = (left + right) // 2 # find middle index

            if nums[mid] == target:   # found it!
                return mid
            elif nums[mid] < target:  # target in right half
                left = mid + 1        # eliminate left half
            else:                     # target in left half
                right = mid - 1       # eliminate right half

        return -1                     # not found

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))   # Expected: 4
print(solution.search([-1, 0, 3, 5, 9, 12], 2))   # Expected: -1
print(solution.search([-1, 0, 3, 5, 9, 12], -1))  # Expected: 0
print(solution.search([5], 5))                      # Expected: 0

# ============================================
# WHAT I LEARNED
# ============================================
# - Binary Search ONLY works on sorted arrays
# - Eliminates half the search space every step → O(log n)
# - For 1 million elements → only 20 steps needed!
# - left = mid+1 → go right
# - right = mid-1 → go left
# - Loop ends when left > right → target not found
# - // is integer division (rounds down)