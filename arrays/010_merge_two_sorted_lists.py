# ============================================
# LeetCode #21 - Merge Two Sorted Lists
# Difficulty: Easy
# Topic: Linked List, Dummy Node
# Date: 09/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Merge two sorted linked lists into one sorted list.

# Example:
# Input:  1 → 2 → 4  and  1 → 3 → 4
# Output: 1 → 1 → 2 → 3 → 4 → 4

# APPROACH: Dummy Node + Two Pointers
# Use dummy node as fake starting point
# Compare front nodes of both lists
# Always attach the smaller one
# When one list runs out → attach remainder of other
# Return dummy.next (skip the dummy itself)

# TIME:  O(n+m) — visit every node in both lists once
# SPACE: O(1)   — only pointers, no extra memory

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)        # fake starting point
        current = dummy            # building pointer

        while list1 and list2:     # while both lists have nodes
            if list1.val <= list2.val:
                current.next = list1   # attach smaller node
                list1 = list1.next     # move list1 forward
            else:
                current.next = list2   # attach smaller node
                list2 = list2.next     # move list2 forward
            current = current.next     # move current forward

        if list1:                  # list2 ran out first
            current.next = list1   # attach remaining list1
        if list2:                  # list1 ran out first
            current.next = list2   # attach remaining list2

        return dummy.next          # skip dummy, return real head

# ============================================
# TEST LOCALLY
# ============================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" → ".join(result) + " → None")

# Build list1: 1 → 2 → 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
# Build list2: 1 → 3 → 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)
print_list(merged)  # Expected: 1 → 1 → 2 → 3 → 4 → 4 → None

# ============================================
# WHAT I LEARNED
# ============================================
# - Dummy Node: fake starting point, avoids special first-node case
# - Always return dummy.next not dummy itself
# - When loop ends, attach remaining list directly (already sorted!)
# - Two Pointers on linked lists: compare, attach, advance
# - Time is O(n+m) because we visit every node exactly once