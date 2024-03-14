[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14253858&assignment_repo_type=AssignmentRepo)
# Task Nr. 1
Write program in `LL_1.py` file. 
## Linked List: Find Middle Node 
### Task Description

Implement the `find_middle_node` method for the `LinkedList` class. This method should return the middle node in the linked list **without** using the length attribute. If the linked list has an even number of nodes, return the first node of the second half of the list.

### Requirements

- The method should use a two-pointer approach:
  - One pointer (`slow`) moves one node at a time.
  - The other pointer (`fast`) moves two nodes at a time.
- When the `fast` pointer reaches the end of the list or has no next node, the `slow` pointer should be at the middle node of the list.
- The method should return the middle node, or the first node of the second half of the list if the list has an even number of nodes.
- The method should only traverse the linked list once, meaning you can only use one loop.

### Pseudo Code

```plaintext
INITIALIZE slow and fast pointers to head of the linked list

WHILE fast is not None and fast.next is not None:
    MOVE slow pointer one step (slow = slow.next)
    MOVE fast pointer two steps (fast = fast.next.next)

RETURN slow pointer (middle node of the linked list)

```
# Task Nr.2
Write your program in `LL_2.py` file
## Linked List: Has Loop (Interview Question)

### Task Description

Write a method called `has_loop` that is part of the linked list class. This method should be able to detect if there is a cycle or loop present in the linked list.

### Requirements

You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop. This algorithm uses two pointers:

- A **slow pointer** that moves one step at a time.
- A **fast pointer** that moves two steps at a time.

If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

### Guidelines

- Create two pointers, `slow` and `fast`, both initially pointing to the head of the linked list.
- Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
- If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return `True`.
- If the fast pointer reaches the end of the list or encounters a `None` value, it means there is no loop in the list. In this case, the method should return `False`.

### Pseudo Code

```plaintext
initialize slow and fast pointers to head of the list

while fast is not None and fast.next is not None:
    move slow pointer one step forward
    move fast pointer two steps forward

    if slow and fast pointers meet:
        return True (loop found)

return False (loop not found)
