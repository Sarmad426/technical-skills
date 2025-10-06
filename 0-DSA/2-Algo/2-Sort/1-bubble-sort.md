## Bubble Sort

**Definition:** Compare two neighboring elements at a time and swap them if the left one is bigger than the right one. Keep doing this until the entire list is sorted.

**Code:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
```

**Time Complexity:** 
- **Best Case:** O(n) - when array is already sorted (with optimization)
- **Average/Worst Case:** O(n²)

**Space Complexity:** O(1)

---

## Step-by-Step Execution

**Initial array:** `[64, 34, 25, 12, 22, 11, 90]`

**Pass 1:** `[34, 25, 12, 22, 11, 64, 90]`

**Pass 2:** `[25, 12, 22, 11, 34, 64, 90]`

**Pass 3:** `[12, 22, 11, 25, 34, 64, 90]`

**Pass 4:** `[12, 11, 22, 25, 34, 64, 90]`

**Pass 5:** `[11, 12, 22, 25, 34, 64, 90]`

**Pass 6:** `[11, 12, 22, 25, 34, 64, 90]`

**Final sorted array:** `[11, 12, 22, 25, 34, 64, 90]`