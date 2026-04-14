# ============================================
# LeetCode #206 - Reverse Linked List
# Difficulty: Easy
# Topic: Linked List, Three Pointers
# Date: 08/04/2026
# Status: Accepted ✅
# ============================================

# PROBLEM:
# Given the head of a singly linked list, reverse it.

# Example:
# Input:  1 → 2 → 3 → 4 → 5 → None
# Output: 5 → 4 → 3 → 2 → 1 → None

# WHAT IS A LINKED LIST?
# A chain of nodes where each node has:
# - val  = the value stored
# - next = pointer to the next node
# Last node points to None

# APPROACH: Three Pointers
# prev     = node behind us (starts as None)
# curr     = node we're currently at
# next_node = node ahead (save before breaking link!)
# Reverse each arrow one by one

# TIME:  O(n) — visit every node once
# SPACE: O(1) — only three pointers used

class Solution:
    def reverseList(self, head):
        prev = None          # will become new tail (points to None)
        curr = head          # start at the beginning

        while curr is not None:           # until we reach the end
            next_node = curr.next         # SAVE next before breaking link!
            curr.next = prev              # reverse the arrow
            prev = curr                   # move prev forward
            curr = next_node             # move curr forward

        return prev                       # prev is now the new head

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

# Build list: 1 → 2 → 3 → 4 → 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Before:", end=" ")
print_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)
print("After: ", end=" ")
print_list(reversed_head)

# ============================================
# WHAT I LEARNED
# ============================================
# - Linked List: chain of nodes, each has val and next pointer
# - Always save next_node BEFORE breaking the link
# - Three pointers: prev, curr, next_node
# - When loop ends, prev = new head of reversed list
# - Arrays vs Linked Lists: arrays = index access,
#   linked lists = pointer traversal