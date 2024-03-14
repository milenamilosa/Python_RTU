class Node:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def is_empty(self):
        return self.height == 0

    def push(self, value, position):
        new_node = Node(value, position)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        return temp

def balancets(s):
    stack = Stack()
    brackets_map = {')': '(', '}': '{', ']': '['}   #  the closing brackets are KEYS and opening brackets are VALUES
                                                    # {'key' : 'value',  .. } This order is to directly access corresponding closing bracket in time O(1) 

    for index, element in enumerate(s,1):      # iterate over each character (bracket) in the input string along with its index
        if element in brackets_map.values():       # if the current character is an opening bracket, 
            stack.push(element, index)             # push it onto the stack
        elif element in brackets_map.keys():        # check if stack is not empty and the top element corresponds to the opening bracket of the current closing bracket
            if not stack.is_empty() and stack.top.value == brackets_map[element]:       # checks if the stack is not empty AND if the value of the top element of the stack matches the corresponding opening bracket for the current closing bracket
                stack.pop()
            else:                       # meaning if the stack is empty or the closing bracket does not match
                return index
    
    if stack.is_empty():                # if the stack is empty, it means all brackets are properly balanced
        return "Success"
    else:
        return stack.top.position       # if the stack is not empty, return the position of the last unmatched opening bracket

# Explanation:

# We create an empty stack to store opening brackets encountered in the string.
# We define a dictionary brackets_map that maps closing brackets to their corresponding opening brackets.
# We loop through each character in the string.
# If the character is an opening bracket, we push it onto the stack along with its index.
# If the character is a closing bracket:
# We check if the stack is not empty and if the top bracket on the stack matches the corresponding opening bracket.
# If it matches, we pop the matching opening bracket from the stack.
# If it doesn't match, we return the index of the mismatched closing bracket.
# After processing all brackets, if the stack is empty, all brackets are balanced, so we return "Success".
# If the stack is not empty, there are unmatched opening brackets left, so we return the position of the last unmatched opening bracket.



#      uncomment     CLEAN CODE:


# def balancets(s):
#     stack = Stack()
#     brackets_map = {')': '(', '}': '{', ']': '['}   

#     for index, element in enumerate(s,1):      
#         if element in brackets_map.values():     
#             stack.push(element, index)            
#         elif element in brackets_map.keys():     
#             if not stack.is_empty() and stack.top.value == brackets_map[element]:     
#                 stack.pop()
#             else:                      
#                 return index
    
#     if stack.is_empty():             
#         return "Success"
#     else:
#         return stack.top.position

s = input("Ievadiet rindu: ")
print(balancets(s))
