# ============================================
# LeetCode #70 - Climbing Stairs
# Difficulty: Easy
# Topic: Dynamic Programming, Fibonacci
# Date: 07/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# n steps staircase, can climb 1 or 2 steps at a time
# How many distinct ways to reach the top?

# Example:
# Input:  n = 5
# Output: 8

# APPROACH: Dynamic Programming (Fibonacci)
# ways(n) = ways(n-1) + ways(n-2)
# To reach step n: either came from n-1 or n-2
# Use sliding window of last two answers

# TIME:  O(n) — one pass from 3 to n
# SPACE: O(1) — only two variables stored

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:                        # base cases
            return n

        prev2 = 1                         # ways to reach step 1
        prev1 = 2                         # ways to reach step 2

        for i in range(3, n + 1):         # calculate from step 3 onwards
            current = prev1 + prev2       # fibonacci: sum of last two
            prev2 = prev1                 # slide window forward
            prev1 = current               # slide window forward

        return prev1                      # answer for step n

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.climbStairs(1))   # Expected: 1
print(solution.climbStairs(2))   # Expected: 2
print(solution.climbStairs(3))   # Expected: 3
print(solution.climbStairs(5))   # Expected: 8
print(solution.climbStairs(10))  # Expected: 89

# ============================================
# WHAT I LEARNED
# ============================================
# - Dynamic Programming: break big problem into smaller subproblems
# - Climbing stairs follows Fibonacci sequence
# - ways(n) = ways(n-1) + ways(n-2)
# - Sliding window: only keep last 2 answers, saves memory
# - Early exit handles base cases cleanly