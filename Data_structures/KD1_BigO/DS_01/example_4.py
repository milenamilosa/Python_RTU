# Shows how to reverse an array in Python.

# Time Complexity: O(n). The loop runs through half of the array, so it’s linear with respect to the array size.
# Auxiliary Space Complexity: O(1). In-place reversal, meaning it doesn’t use additional space.

# Iterative python program to reverse an array 
 
# Function to reverse A[] from start to end 
def reverseList(A, start, end): 
    while start < end: 
        A[start], A[end] = A[end], A[start] 
        start += 1
        end -= 1
 
# Driver function to test above function 
A = [1, 2, 3, 4, 5, 6] 
print(A) 
reverseList(A, 0, 5) 
print("Reversed list is") 
print(A) 
# This program is contributed by Pratik Chhajer 