## Insertion Sort

**Definition:** Take one element at a time and insert it into its correct position in the already sorted portion of the array, shifting elements as needed.

**Code:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))
```

**Time Complexity:** 
- **Best Case:** O(n) - when array is already sorted
- **Average/Worst Case:** O(n²)

**Space Complexity:** O(1)

---

## Step-by-Step Execution

**Initial array:** `[64, 34, 25, 12, 22, 11, 90]`

**Pass 1:** Insert 34 → `[34, 64, 25, 12, 22, 11, 90]`

**Pass 2:** Insert 25 → `[25, 34, 64, 12, 22, 11, 90]`

**Pass 3:** Insert 12 → `[12, 25, 34, 64, 22, 11, 90]`

**Pass 4:** Insert 22 → `[12, 22, 25, 34, 64, 11, 90]`

**Pass 5:** Insert 11 → `[11, 12, 22, 25, 34, 64, 90]`

**Pass 6:** Insert 90 → `[11, 12, 22, 25, 34, 64, 90]`

**Final sorted array:** `[11, 12, 22, 25, 34, 64, 90]`