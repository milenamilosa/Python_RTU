# Demonstrates how to detect the minimum and maximum value of an array in Python.

# Time Complexity: O(n log n), where n is the number of elements in the array, as we are using a sorting algorithm.
# Auxiliary Space: O(1), as we are not using any extra space.

# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#               Maximum element is: 9

# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#               Maximum element is: 35



def getMinMax(arr):
    arr.sort()
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax
 
arr = [1000, 11, 445, 1, 330, 3000]
minmax = getMinMax(arr)
 
print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])