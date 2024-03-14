# Python program for implementation of Selection 
# Demonstrates how to sort elements in an array using traversal through all array elements.

# Complexity Analysis of Selection Sort:
# Time Complexity: O(N^2) as there are two nested loops. One loop to select an element of the array one by one = O(N), 
# and another loop to compare that element with every other array element = O(N). 
# Therefore, the overall complexity = O(N) * O(N) = O(N^2).

# Sort 
import sys 
A = [64, 25, 12, 22, 11] 

# Traverse through all array elements 
for i in range(len(A)): 
	
	# Find the minimum element in remaining unsorted array 
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 
			
	# Swap the found minimum element with the first element		 
	A[i], A[min_idx] = A[min_idx], A[i] 

# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
	print("%d" %A[i],end=" , ") 
