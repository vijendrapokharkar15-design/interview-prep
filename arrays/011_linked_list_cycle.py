# ============================================
# LeetCode #141 - Linked List Cycle
# Difficulty: Easy
# Topic: Linked List, Fast & Slow Pointers
# Date: 10/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Given a linked list, determine if it has a cycle.
# A cycle = a node's next pointer points to a previous node.

# Example:
# 1 → 2 → 3 → 4 → (back to 2) → has cycle = True
# 1 → 2 → 3 → None             → has cycle = False

# APPROACH: Floyd's Cycle Detection (Fast & Slow Pointers)
# slow moves 1 step at a time
# fast moves 2 steps at a time
# If cycle exists → they will eventually meet!
# If no cycle → fast reaches None first

# TIME:  O(n) — fast pointer catches slow within one loop
# SPACE: O(1) — only two pointers used

class Solution:
    def hasCycle(self, head):
        slow = head              # moves 1 step
        fast = head              # moves 2 steps

        while fast and fast.next:     # until fast reaches end
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps

            if slow == fast:          # they met → cycle!
                return True

        return False                  # fast reached end → no cycle

# ============================================
# TEST LOCALLY
# ============================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

solution = Solution()

# Test 1: No cycle → 1 → 2 → 3 → None
head1 = ListNode(1, ListNode(2, ListNode(3)))
print(solution.hasCycle(head1))  # Expected: False

# Test 2: With cycle → 1 → 2 → 3 → back to 2
node2 = ListNode(2)
node3 = ListNode(3)
node2.next = node3
node3.next = node2   # cycle here!
head2 = ListNode(1)
head2.next = node2
print(solution.hasCycle(head2))  # Expected: True

# ============================================
# WHAT I LEARNED
# ============================================
# - Floyd's Cycle Detection: famous algorithm by Robert Floyd
# - Fast & Slow pointers: if cycle exists they MUST meet
# - Compare nodes (memory addresses) not values!
# - fast.next.next moves 2 steps safely only when fast.next exists
# - Three Two-Pointer variations: inward, slow-fast array, slow-fast cycle