## 🔍 Linear Search

### How it works

* Start at the first element.
* Compare it with the target.
* If found, return its index.
* If not, keep moving until the end.

### Python code

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # found at index i
    return -1  # not found

data = [12, 45, 7, 23, 89, 5]
print(linear_search(data, 23))  # Output: 3
```

### Real-world use cases

* **Databases / Logs**: Searching a log file or unsorted database rows.
* **Search in text editors**: “Find” feature in Notepad/VSCode — if text isn’t indexed, it does linear search.
* **IoT / sensors**: Scanning raw sensor readings in a simple device where efficiency isn’t critical.

👉 Linear search is used when:

1. Data is **small**.
2. Data is **unsorted**.
3. You don’t want extra memory overhead for preprocessing.

---

## ⚡ Binary Search

### How it works

* Works only on **sorted data**.
* Repeatedly divide the search space in half until you find the target or narrow to empty.

### Python code

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1  # search right half
        else:
            high = mid - 1  # search left half
    return -1  # not found

data = [5, 7, 12, 23, 45, 89]
print(binary_search(data, 23))  # Output: 3
```

### Real-world use cases

* **Databases**: Indexes in SQL (like B-Trees, which are an extension of binary search).
* **Search engines**: Looking up words in a dictionary for autocomplete.
* **E-commerce**: Price filtering (if sorted by price, binary search finds ranges quickly).
* **Gaming**: Collision detection or finding nearest values (like in a leaderboard sorted by scores).

👉 Binary search is used when:

1. Data is **large**.
2. Data is **sorted or indexed**.
3. Fast lookup is critical.

---

### Big Picture

* **Linear search** = brute force, universal, but slow.
* **Binary search** = smart, efficient, but needs sorted data.
* Together, they highlight the classic **trade-off**: preprocessing (sorting, indexing) vs direct search time.

---

💡 Quick thought for you, Sarmad:
If you had a **startup product** with a feature like **searching users by username**, would you prefer linear search or binary search (and why)?
Given that usernames are typically unique and can be sorted, I would prefer **binary search** for searching users by username. This is because:
1. **Efficiency**: Binary search is much faster for large datasets, reducing the time complexity from O(n) to O(log n).
2. **Scalability**: As the user base grows, binary search will handle larger datasets more efficiently.
3. **User Experience**: Faster search results lead to a better user experience, which is crucial for user retention.
4. **Sorted Data**: Usernames can be easily sorted and indexed, making binary search a practical choice.