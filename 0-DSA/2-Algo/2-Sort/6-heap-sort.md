## Heap Sort

**Definition:** Convert the array into a max heap (a tree where parent nodes are larger than children), then repeatedly extract the maximum element and place it at the end of the array.

**Code:**
```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(arr))
```

**Time Complexity:** O(n log n) for all cases

**Space Complexity:** O(1)

---

## Step-by-Step Execution

**Initial array:** `[64, 34, 25, 12, 22, 11, 90]`

**Build Max Heap:**
```
Step 1: Heapify from index 2 → [64, 34, 25, 12, 22, 11, 90]
Step 2: Heapify from index 1 → [64, 34, 25, 12, 22, 11, 90]
Step 3: Heapify from index 0 → [90, 34, 25, 12, 22, 11, 64]

Max Heap: [90, 34, 25, 12, 22, 11, 64]
```

**Extract Max and Heapify:**

**Pass 1:** Swap 90 with 64, heapify → `[64, 34, 25, 12, 22, 11 | 90]`

**Pass 2:** Swap 64 with 11, heapify → `[34, 22, 25, 12, 11 | 64, 90]`

**Pass 3:** Swap 34 with 11, heapify → `[25, 22, 11, 12 | 34, 64, 90]`

**Pass 4:** Swap 25 with 12, heapify → `[22, 12, 11 | 25, 34, 64, 90]`

**Pass 5:** Swap 22 with 11, heapify → `[12, 11 | 22, 25, 34, 64, 90]`

**Pass 6:** Swap 12 with 11 → `[11 | 12, 22, 25, 34, 64, 90]`

**Final sorted array:** `[11, 12, 22, 25, 34, 64, 90]`