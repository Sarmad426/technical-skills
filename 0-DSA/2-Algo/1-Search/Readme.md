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


Binary search would be the preferred approach for searching usernames due to its efficiency, especially as the user base grows. To utilize binary search, the usernames must be sorted **lexicographically** (i.e., in dictionary order). This allows for a more efficient search by narrowing down the search space. The logarithmic time complexity of binary search offers significant performance advantages over linear search, especially for larger datasets.


Sorting usernames works the same as sorting numbers — except instead of comparing **numerical value**, Python (and most languages) compare **lexicographic order** (dictionary order).

So:

* `"adam" < "sam"` because `"a"` comes before `"s"`.
* `"sam" < "sara"` because after `"s"`, `"a"` comes before `"a"+"r"`.

### Python Example

```python
usernames = ["zain", "ali", "sam", "sara", "ahmed", "bilal"]

# Sort lexicographically (dictionary order)
usernames.sort()
print(usernames)  
# Output: ['ahmed', 'ali', 'bilal', 'sam', 'sara', 'zain']

# Now we can apply binary search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:  # dictionary comparison
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(usernames, "sam"))  # Output: 3
```

---

### 🔥 Real-world link for usernames:

* **Social media (Facebook, Instagram, Twitter/X):** When you search a username, they don’t brute-force check every user.

  1. They **sort or index** all usernames lexicographically.
  2. Use **binary search (or B-Trees/Hashing for scale)** to quickly narrow down results.
  3. For autocomplete, they don’t just check `"sam"` — they find the *first match* with `"sam"` and then scan forward for `"sami"`, `"samar"`, `"samuel"` etc.

---

👉 Here’s a question for you, Sarmad:
If you were building **search for usernames** in your SaaS product, would you stick with **binary search on sorted usernames**, or would you consider something faster like **hashing**? Why?
