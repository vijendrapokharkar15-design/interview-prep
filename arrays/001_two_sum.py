# ============================================
# LeetCode #1 - Two Sum
# Difficulty: Easy
# Topic: Arrays, Hash Map
# Date: 01/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Given an array of numbers and a target,
# return indices of the two numbers that add up to target.
# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]  because nums[0] + nums[1] = 2 + 7 = 9

# APPROACH: Hash Map
# For each number, calculate complement = target - num
# Check if complement already exists in dictionary
# If YES → found our pair, return both indices
# If NO  → store current number and its index, move on

# TIME:  O(n) — one single pass through the array
# SPACE: O(n) — dictionary stores up to n elements

class Solution:
    def twoSum(self, nums, target):
        seen = {}                            # empty notepad

        for i, num in enumerate(nums):       # i = index, num = value
            complement = target - num        # what number do I need?

            if complement in seen:           # have I seen it before?
                return [seen[complement], i] # yes! return both indices

            seen[num] = i                    # no? write it in notepad

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Expected: [1, 2]
print(solution.twoSum([3, 3], 6))          # Expected: [0, 1]

# ============================================
# WHAT I LEARNED
# ============================================
# - Hash maps are perfect for "have I seen X before?" problems
# - complement = target - num is the key insight
# - Check FIRST, store AFTER (so a number doesn't pair with itself)
# - This pattern appears in MANY array problems