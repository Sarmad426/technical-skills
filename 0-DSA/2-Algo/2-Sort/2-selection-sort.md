## Selection Sort

**Definition:** Find the smallest element in the unsorted portion and swap it with the first unsorted element. Repeat until the entire list is sorted.

**Code:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))
```

**Time Complexity:** O(n²) for all cases (best, average, worst)

**Space Complexity:** O(1)

---

## Step-by-Step Execution

**Initial array:** `[64, 34, 25, 12, 22, 11, 90]`

**Pass 1:** Find min (11), swap with first → `[11, 34, 25, 12, 22, 64, 90]`

**Pass 2:** Find min (12), swap with second → `[11, 12, 25, 34, 22, 64, 90]`

**Pass 3:** Find min (22), swap with third → `[11, 12, 22, 34, 25, 64, 90]`

**Pass 4:** Find min (25), swap with fourth → `[11, 12, 22, 25, 34, 64, 90]`

**Pass 5:** Find min (34), already in place → `[11, 12, 22, 25, 34, 64, 90]`

**Pass 6:** Find min (64), already in place → `[11, 12, 22, 25, 34, 64, 90]`

**Final sorted array:** `[11, 12, 22, 25, 34, 64, 90]`