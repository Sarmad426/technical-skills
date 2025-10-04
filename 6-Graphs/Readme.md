# 📘 Graphs in Data Structures & Algorithms (DSA)

### 🔹 Introduction

A **Graph** is a data structure that models relationships. It consists of:

* **Vertices (nodes):** Entities (e.g., cities, people, webpages).
* **Edges (links):** Connections between vertices (e.g., roads, friendships, hyperlinks).

Graphs are everywhere: maps, social networks, recommendation engines, internet routing, workflows, supply chains.

---

### 🔹 Why Do We Need Graphs?

Graphs allow us to:

* Represent **networks** (roads, flights, computers).
* Solve **pathfinding problems** (shortest route in GPS).
* Model **dependencies** (tasks in a project).
* Optimize **resources** (minimum cost of connecting systems).

👉 Real examples:

* **Google Maps** → shortest path between locations.
* **Facebook/LinkedIn** → who you’re connected to.
* **Uber** → roads as graphs to optimize trip routes.
* **Amazon/Netflix** → recommendations via bipartite graphs (user ↔ item).

---

### 🔹 Graph Representations

#### 1. **Adjacency Matrix**

* A 2D array (size `n x n`) where `matrix[i][j] = 1` (or weight) if edge exists, otherwise `0`.
* Always uses `n²` space.

**Example:** Graph with edges A–B, A–C, B–D, C–D

```
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 1 ]
D [ 0 1 1 0 ]
```

✅ Fast edge lookup (`O(1)`)
❌ Wastes space for sparse graphs

---

#### 2. **Adjacency List**

* Each vertex stores a list of its neighbors.
* Uses space proportional to edges (`O(V+E)`).

**Example (same graph):**

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
print(graph["A"])  # ['B', 'C']
```

✅ Space-efficient for sparse graphs
❌ Slower edge lookup (`O(degree)`)

---

### 🔹 Side-by-Side

| Feature            | Adjacency Matrix                                              | Adjacency List                           |
| ------------------ | ------------------------------------------------------------- | ---------------------------------------- |
| **Space**          | `O(V²)`                                                       | `O(V+E)`                                 |
| **Edge lookup**    | Fast (`O(1)`)                                                 | Slower                                   |
| **Graph type**     | Dense                                                         | Sparse                                   |
| **Real-world use** | Small dense networks, algorithms needing constant-time checks | Large maps, social graphs, road networks |

---

### 🔹 The Uber Example

* Uber models **roads between locations**.
* Each city point connects to only a few others → **sparse graph**.
* **Adjacency List** is used to store roads: memory efficient, avoids “junk” zeros, and works better with shortest-path algorithms like Dijkstra’s.

---

### 🔹 Types of Graphs (high-level)

* **Directed vs Undirected** → one-way vs two-way edges.
* **Weighted vs Unweighted** → edges may have costs (distance, time).
* **Cyclic vs Acyclic** → whether loops exist (trees are acyclic).

---

### 🔹 Python Snippet – BFS Traversal (Unweighted Shortest Path)

```python
from collections import deque

graph = {
    "A": ["B","C"],
    "B": ["A","D"],
    "C": ["A","D"],
    "D": ["B","C"]
}

def bfs(start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        print("Visiting:", node)
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

bfs("A")
```

Output (order of exploration):

```
Visiting: A
Visiting: B
Visiting: C
Visiting: D
```

---

### 🔹 Key Takeaway

Graphs are the universal tool whenever **connections or relationships matter**.

* Adjacency List = memory efficient, real-world scale (Uber, Facebook).
* Adjacency Matrix = quick lookups, better for small dense graphs.
* Algorithms (BFS, DFS, Dijkstra, MST, Max Flow) unlock powerful problem-solving on graphs.
