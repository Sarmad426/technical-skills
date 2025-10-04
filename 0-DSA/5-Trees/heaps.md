# 🌲 Heap Data Structure

### 📖 Definition

A **Heap** is a special kind of **binary tree** that satisfies the **heap property**:

* **Max-Heap** → Parent ≥ Children
* **Min-Heap** → Parent ≤ Children

👉 Always a **Complete Binary Tree (CBT)**:

* Filled level by level, from **left to right** (no gaps except possibly the last level).

---

# 🛠 Types of Heaps

### 1. **Max-Heap**

* The largest value is always at the root.
* Example:

```
        50
       /  \
     30    40
    /  \
  10   20
```

* Every parent is **greater than or equal to** its children.

---

### 2. **Min-Heap**

* The smallest value is always at the root.
* Example:

```
        10
       /  \
     20    30
    /  \
  40   50
```

* Every parent is **smaller than or equal to** its children.

---

# ⚡ Operations on Heap

1. **Insertion** (O(log n))

   * Place the new element at the end (last available position).
   * “Bubble up” (heapify up) until the heap property is restored.

2. **Deletion (remove root)** (O(log n))

   * Remove the root.
   * Place the last element at the root.
   * “Bubble down” (heapify down) until the heap property is restored.

3. **Peek/Find-Max/Min** (O(1))

   * Just return the root.

---

# 📦 Implementation in Python

In Python, heaps are implemented using the **`heapq` module**, which provides a **Min-Heap** by default.

```python
import heapq

# create a heap
heap = []

# insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 30)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

print("Min-Heap:", heap)  # [5, 10, 20, 30]

# remove the smallest element
print("Pop:", heapq.heappop(heap))  # 5
print("After pop:", heap)           # [10, 30, 20]
```

👉 To simulate a **Max-Heap**, we insert negative values.

```python
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -20)

print("Max-Heap:", [-x for x in max_heap])  # [30, 10, 20]
```

---

# 🎯 Use Cases of Heaps

* **Priority Queues** → tasks with highest priority executed first.
* **Heap Sort** → efficient sorting algorithm.
* **Graph Algorithms** → Dijkstra’s shortest path, Prim’s MST.
* **Scheduling** → CPU job scheduling, bandwidth management.
* **Top-K Problems** → Find k largest/smallest elements quickly.

---

✅ Summary:

* **Heap = Complete Binary Tree** with **heap property**.
* **Min-Heap → smallest root**, **Max-Heap → largest root**.
* Efficient for **priority-based problems**.


Perfect 👍 Let’s **walk through Heap operations step by step with diagrams**.
We’ll use a **Max-Heap** (easier to visualize with "biggest number on top").

---

# 🔹 Step 1: Insert elements into a Max-Heap

We’ll insert in order: **10, 20, 5, 6, 1, 8**

---

### Insert `10`

```
10
```

---

### Insert `20`

* Insert at next available spot → left of `10`.
* Compare with parent (`10`). Since `20 > 10`, **swap**!

```
    20
   /
 10
```

---

### Insert `5`

* Goes to the right of `20`.
* `5 < 20` → no swap.

```
    20
   /  \
 10    5
```

---

### Insert `6`

* Goes to the left of `10`.
* Compare with parent → `6 < 10` → no swap.

```
      20
     /   \
   10     5
  /
 6
```

---

### Insert `1`

* Goes to the right of `10`.
* `1 < 10` → no swap.

```
      20
     /   \
   10     5
  /  \
 6    1
```

---

### Insert `8`

* Goes to the left of `5`.
* Compare: `8 > 5` → swap.

```
      20
     /   \
   10     8
  /  \   /
 6    1 5
```

Heap is complete ✅

---

# 🔹 Step 2: Deletion (Remove Root)

### Current Heap

```
      20
     /   \
   10     8
  /  \   /
 6    1 5
```

* Root = `20` (max).
* Remove it → replace with **last element (`5`)**.

```
      5
     /   \
   10     8
  /  \
 6    1
```

### Heapify Down

* Compare `5` with children (`10` and `8`).
* Largest child = `10`. Swap with `10`.

```
      10
     /   \
    5     8
   / \
  6   1
```

* Compare `5` with its children (`6`, `1`).
* Largest child = `6`. Swap with `6`.

```
      10
     /   \
    6     8
   / \
  5   1
```

✅ Heap property restored!

---

# ⚡ Key Insight

* **Insertion → bubble up** until parent > child.
* **Deletion → bubble down** until parent > children.

---

👉 Do you want me to also explain **Heap Sort** using this same Max-Heap (it’s basically repeated deletions)?
