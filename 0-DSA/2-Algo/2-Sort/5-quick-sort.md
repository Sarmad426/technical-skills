## Quick Sort

**Definition:** Pick a pivot element, partition the array so that elements smaller than the pivot are on the left and larger ones on the right, then recursively sort both partitions. 

Quick Sort is typically the fastest comparison-based sorting algorithm for random data in practice.

**Code:**
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))
```

**Time Complexity:** 
- **Best/Average Case:** O(n log n)
- **Worst Case:** O(n²) - when array is already sorted

**Space Complexity:** O(log n) - for recursion stack

---

## Step-by-Step Execution

**Initial array:** `[64, 34, 25, 12, 22, 11, 90]`

```
Pivot = 90
Left: [64, 34, 25, 12, 22, 11]  |  90  |  Right: []

    Pivot = 11
    Left: []  |  11  |  Right: [64, 34, 25, 12, 22]
    
        Pivot = 22
        Left: [12]  |  22  |  Right: [64, 34, 25]
        
            Pivot = 25
            Left: []  |  25  |  Right: [64, 34]
            
                Pivot = 34
                Left: []  |  34  |  Right: [64]
```

**Merging back:**
```
[] + [11] + [12] + [22] + [] + [25] + [] + [34] + [64] + [90] + []
```

**Final sorted array:** `[11, 12, 22, 25, 34, 64, 90]`