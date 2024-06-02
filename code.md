## Binary Search

Binary search is an efficient searching algorithm that works on a sorted array. It follows the divide and conquer approach to find the target element in the array by repeatedly dividing the search space in half.

### Algorithm

1. Initialize two pointers, `start` and `end`, to the first and last index of the array respectively.
2. Calculate the middle index using the formula `mid = (start + end) // 2`.
3. Compare the middle element of the array with the target element.
   - If the middle element is equal to the target element, return the index.
   - If the middle element is greater than the target element, update `end` to `mid - 1` and repeat step 2.
   - If the middle element is less than the target element, update `start` to `mid + 1` and repeat step 2.
4. If the target element is not found, return -1.

### Python Code

```python
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
```

### Explanation

The `binary_search` function takes an array `arr` and a target element `target` as input. It initializes two pointers, `start` and `end`, to the first and last index of the array respectively.

Inside the while loop, it calculates the middle index using the formula `(start + end) // 2`. It then compares the middle element of the array with the target element. If they are equal, it returns the index.

If the middle element is greater than the target element, it updates `end` to `mid - 1` and repeats the process. If the middle element is less than the target element, it updates `start` to `mid + 1` and repeats the process.

If the target element is not found, the function returns -1.

In the example usage, we have an array `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]` and we want to search for the element 23. The `binary_search` function is called with the array and target element as arguments. It returns the index of the target element if found, otherwise -1. In this case, the element 23 is found at index 5, so the output is `Element 23 found at index 5`.