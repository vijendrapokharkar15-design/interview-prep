# ============================================
# LeetCode #242 - Valid Anagram
# Difficulty: Easy
# Topic: Strings, Hash Map, Counter
# Date: 06/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Given two strings s and t, return True if t
# is an anagram of s, otherwise return False.
# Anagram = same letters, same count, different order.

# Example:
# Input:  s = "anagram", t = "nagaram"
# Output: True
# Input:  s = "rat", t = "car"
# Output: False

# APPROACH: Counter (Frequency Map)
# Count how many times each letter appears in both strings
# If counts match perfectly → anagram!
# Early exit: if lengths differ → instantly False

# TIME:  O(n) — counting each string once
# SPACE: O(n) — counter stores up to n unique characters

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):          # different lengths = never anagram
            return False

        return Counter(s) == Counter(t)  # compare letter counts

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Expected: True
print(solution.isAnagram("rat", "car"))          # Expected: False
print(solution.isAnagram("listen", "silent"))    # Expected: True
print(solution.isAnagram("hello", "world"))      # Expected: False

# ============================================
# WHAT I LEARNED
# ============================================
# - Counter automatically counts frequency of each element
# - Comparing two Counters with == checks if identical
# - Early exit saves time on obvious cases
# - Counter vs Hash Map: use Counter when you just need counts
#   use Hash Map when you need custom values like indices