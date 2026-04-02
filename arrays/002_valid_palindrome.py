# ============================================
# LeetCode #125 - Valid Palindrome
# Difficulty: Easy
# Topic: Strings, Two Pointers
# Date: 02/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# A phrase is a palindrome if it reads the same forwards and backwards
# ignoring spaces, punctuation and uppercase/lowercase.

# Example:
# Input:  "A man, a plan, a canal: Panama"
# Output: True

# APPROACH: Two Pointers
# Place one pointer at start, one at end
# Skip non-letters/numbers
# Compare characters moving inward
# If any mismatch → not a palindrome

# TIME:  O(n) — one pass through the string
# SPACE: O(1) — no extra memory used

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1      # pointers at both ends

        while left < right:               # keep going until they meet

            # skip spaces and punctuation on the left
            while left < right and not s[left].isalnum():
                left += 1

            # skip spaces and punctuation on the right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare both characters (ignore case)
            if s[left].lower() != s[right].lower():
                return False              # mismatch! not a palindrome

            left += 1                     # move left pointer inward
            right -= 1                    # move right pointer inward

        return True                       # all matched! it's a palindrome

# ============================================
# TEST CASES
# ============================================
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))                      # False
print(solution.isPalindrome("Was it a car or a cat I saw?"))    # True

# ============================================
# WHAT I LEARNED
# ============================================
# - Two Pointers: start from both ends, walk inward
# - isalnum() skips spaces and punctuation automatically
# - .lower() handles uppercase/lowercase comparison
# - Use this pattern whenever checking symmetry in strings