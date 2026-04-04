# ============================================
# LeetCode #217 - Contains Duplicate
# Difficulty: Easy
# Topic: Arrays, Hash Set
# Date: 03/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Return True if any value appears more than once
# Return False if all values are unique

# Example:
# Input:  [1, 2, 3, 1]
# Output: True  (1 appears twice)

# APPROACH: Hash Set
# Walk through array one by one
# Before adding each number — check if already seen
# If yes → duplicate found → return True
# If no  → add to set and continue
# If loop ends → all unique → return False

# TIME:  O(n) — one pass through the array
# SPACE: O(n) — set stores up to n elements

class Solution:
    def containsDuplicate(self, nums):
        seen = set()               # empty checklist

        for num in nums:           # go through every number
            if num in seen:        # seen it before?
                return True        # yes! duplicate found
            seen.add(num)          # no? add to checklist

        return False               # no duplicates found

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))    # Expected: True
print(solution.containsDuplicate([1, 2, 3, 4]))    # Expected: False
print(solution.containsDuplicate([1, 1, 1, 3, 3])) # Expected: True

# ============================================
# WHAT I LEARNED
# ============================================
# - Hash Set: use when you only need to track WHAT you've seen
# - Hash Map: use when you need to track WHERE you saw it
# - set.add() vs dict[key]=value vs list.append()
# - Sets are faster than lists for membership checking