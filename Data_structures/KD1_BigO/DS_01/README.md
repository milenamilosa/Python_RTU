# Data Structure: Array - Example Files

These files are from discussions during the RTU data structure class. The repository contains 9 files:

1. **example_0_address.py**  
   Demonstrates how to access array elements in memory using numpy array structure in Python.

2. **example_0_arr.c**  
   Shows how to access each array element in memory using C.

3. **example_1.py**  
   Demonstrates how to define and use cookies in Python.

4. **example_2.py**  
   Explains how variable addressing in memory works.

5. **example_3.py**  
   Demonstrates how to reverse an array in Python.  
   - Time Complexity: O(n). Copying elements to a new array is a linear operation.
   - Auxiliary Space Complexity: O(n). Additional space is used to store the new array.

6. **example_4.py**  
   Shows how to reverse an array in Python.  
   - Time Complexity: O(n). The loop runs through half of the array, so it’s linear with respect to the array size.
   - Auxiliary Space Complexity: O(1). In-place reversal, meaning it doesn’t use additional space.

7. **example_5.py**  
   Demonstrates how to reverse an array in Python.  
   - Time Complexity: O(n). The reverse method typically has linear time complexity.
   - Auxiliary Space Complexity: O(n).

8. **example_6.py**  
   Demonstrates how to detect the minimum and maximum value of an array in Python.  
   - Time Complexity: O(n log n), where n is the number of elements in the array, as we are using a sorting algorithm.
   - Auxiliary Space: O(1), as we are not using any extra space.

9. **example_7.py**  
   Demonstrates how to sort elements in an array using traversal through all array elements.  
   - Complexity Analysis of Selection Sort:
     - Time Complexity: O(N^2) as there are two nested loops. One loop to select an element of the array one by one = O(N), and another loop to compare that element with every other array element = O(N). Therefore, the overall complexity = O(N) * O(N) = O(N^2).
