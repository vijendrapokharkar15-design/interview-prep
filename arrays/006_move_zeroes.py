# ============================================
# LeetCode #283 - Move Zeroes
# Difficulty: Easy
# Topic: Arrays, Two Pointers (Slow-Fast)
# Date: 05/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Move all zeroes to the end of the array
# while maintaining order of non-zero elements.
# Must be done IN-PLACE (no new array!)

# Example:
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# APPROACH: Slow-Fast Two Pointers
# left  = slow pointer → marks next available slot
# right = fast pointer → scans for non-zero numbers
# When right finds non-zero → swap with left slot → move left forward

# TIME:  O(n) — one pass through the array
# SPACE: O(1) — in-place, no extra memory

class Solution:
    def moveZeroes(self, nums):
        left = 0                              # next available slot

        for right in range(len(nums)):        # scan every element
            if nums[right] != 0:              # found a non-zero?
                nums[left], nums[right] = nums[right], nums[left]  # swap!
                left += 1                     # move slot forward

# ============================================
# TEST CASES
# ============================================
solution = Solution()

nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(nums1)  # Expected: [1, 3, 12, 0, 0]

nums2 = [0, 0, 1]
solution.moveZeroes(nums2)
print(nums2)  # Expected: [1, 0, 0]

nums3 = [0]
solution.moveZeroes(nums3)
print(nums3)  # Expected: [0]

# ============================================
# WHAT I LEARNED
# ============================================
# - Slow-Fast Two Pointers: both start left, move right
# - left = slow (slot for next valid element)
# - right = fast (scanner looking for valid elements)
# - Python swap: a, b = b, a (no temp variable needed!)
# - Different from Valid Palindrome (inward) vs this (both rightward)