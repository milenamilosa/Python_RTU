# Demonstrates how to reverse an array in Python.

# Time Complexity: O(n). Copying elements to a new array is a linear operation.
# Auxiliary Space Complexity: O(n). Additional space is used to store the new array.


def reverse_array_extra_array(arr):
	reversed_arr = arr[::-1]

	# Print reversed array
	print("Reversed Array:", end=" ")
	for i in reversed_arr:
		print(i, end=" ")

# Example usage:
original_arr = [1, 2, 3, 4, 5]
print (original_arr[::-1])
# reverse_array_extra_array(original_arr)
