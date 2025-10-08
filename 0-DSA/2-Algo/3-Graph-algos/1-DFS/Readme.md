# 🧭 Depth-First Search (DFS)

## 📘 Overview

**Depth-First Search (DFS)** is a **graph traversal algorithm** that explores as far as possible along a branch before backtracking.
It dives **deep** into one path, visiting nodes recursively (or using a stack), then backtracks when no unvisited neighbors remain.

Think of DFS like exploring a **maze** — you follow one corridor all the way to the end, and only when you hit a dead end do you turn back.

---

## ⚙️ How It Works

1. Start from a **source node**.
2. Mark it as **visited**.
3. Visit the **first unvisited neighbor** and go deeper recursively.
4. If no unvisited neighbors remain, **backtrack** to explore other paths.
5. Continue until all nodes are visited.

> DFS can be implemented **recursively** or **iteratively** using a **stack**.

---

## 🧠 Intuition / Analogy

Imagine a **file system**:

* You open a folder.
* Then open subfolders inside it.
* You keep going deeper until there’s no more subfolder.
* Then you go back and explore the next folder.

That’s exactly how DFS works — **go deep, then backtrack**.

---

## 💡 Key Points

* Uses **Stack (LIFO)** or **recursion**.
* Traverses **depth-first**.
* Doesn’t guarantee shortest path (unlike BFS).
* Time Complexity: **O(V + E)**
* Space Complexity: **O(V)** (due to recursion stack or explicit stack)

---

## 🧩 Pseudocode (Recursive)

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
```

---

## 🧩 Pseudocode (Iterative)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in reversed(graph[node]):  # reversed to maintain order
                if neighbor not in visited:
                    stack.append(neighbor)
```

---

## 🗺️ Example

```python
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

dfs(graph, 'A')
```

**Output:**

```
A B D E F C
```

👉 DFS goes **deep** first — explores one branch fully before moving to another.

---

## 🧰 Real-World Applications

| Use Case                           | Explanation                                          |
| ---------------------------------- | ---------------------------------------------------- |
| **Pathfinding / Maze Solving**     | Explores deep routes before backtracking.            |
| **Topological Sorting**            | Used in scheduling or dependency resolution.         |
| **Cycle Detection**                | Detects cycles in directed or undirected graphs.     |
| **Connected Components**           | Finds isolated parts of a graph.                     |
| **Solving Puzzles (e.g., Sudoku)** | Explores every possibility recursively.              |
| **Web Crawling (Deep mode)**       | Crawls deep into linked pages before moving to next. |

---

## 🆚 DFS vs BFS

| Feature                    | DFS                      | BFS                      |
| -------------------------- | ------------------------ | ------------------------ |
| Data Structure             | Stack / Recursion        | Queue                    |
| Traversal                  | Depth-wise               | Level-wise               |
| Shortest Path (Unweighted) | ❌ Not guaranteed         | ✅ Yes                    |
| Memory Usage               | Lower (usually)          | Higher                   |
| Backtracking               | Yes                      | No                       |
| Typical Use                | Search all possibilities | Find shortest connection |

---

## 🧩 Example Analogy

Exploring folders in a computer:

* You open one folder.
* Keep diving into subfolders.
* Once done, you come back and open the next folder.
  That’s **Depth-First Search** in real life.
