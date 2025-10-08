# **Breadth-First Search (BFS)**

### *Graph Traversal Algorithm*

---

## 🧠 **Overview**

**Breadth-First Search (BFS)** is a fundamental graph traversal algorithm used to explore nodes level by level.
Starting from a **source node**, BFS visits all its **neighbors first**, then moves outward to the next level of nodes.

It’s often compared to a “wave expansion” — visiting everything one step away before moving further.

---

## ⚙️ **Core Idea**

BFS uses a **Queue (FIFO)** data structure to keep track of nodes to visit.
It also maintains a **Visited Set** to prevent reprocessing the same node.

---

## 🧩 **Algorithm Steps**

1. Start from a given source node.
2. Enqueue it and mark it as visited.
3. While the queue is not empty:

   * Dequeue a node.
   * Visit it (process or print).
   * Enqueue all *unvisited* adjacent nodes.
4. Continue until all reachable nodes are processed.

---

## 💻 **Python Implementation**

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

bfs(graph, 'A')
```

**Output:**

```
A B C D E
```

---

## ⏱️ **Complexity Analysis**

| Type      | Complexity | Description                       |
| --------- | ---------- | --------------------------------- |
| **Time**  | O(V + E)   | Visits every vertex and edge once |
| **Space** | O(V)       | Queue + visited set               |

> **V:** number of vertices
> **E:** number of edges

---

## 🌍 **Real-World Applications**

### 1. **Shortest Path (Unweighted Graphs)**

Used to find the shortest path between two nodes (e.g., in road or network graphs).

* **Example:** Finding the minimal number of connections in a social network.
* **Algorithm:** Each BFS level = 1 more edge from the source.

---

### 2. **Social Networks (Facebook, LinkedIn)**

BFS helps find *mutual friends* and *connection levels*:

* 1st Level → Direct Friends
* 2nd Level → Friends of Friends
* 3rd Level → Extended Network

---

### 3. **Web Crawlers**

Used to traverse the web starting from one page (node) and discovering all reachable URLs (neighbors) level by level.

---

### 4. **Navigation Systems (Google Maps, Uber)**

In *unweighted* graphs, BFS finds the shortest route (fewest hops) between two points.
If edges have weights (distances), **Dijkstra’s Algorithm** is used instead.

---

### 5. **Broadcasting & Networking**

BFS is used for **message broadcasting**, **flood fill algorithms**, and **peer-to-peer discovery**, ensuring even distribution across network nodes.

---

## 🧭 **When to Use BFS**

| Scenario                                       | Why BFS?                                    |
| ---------------------------------------------- | ------------------------------------------- |
| Need shortest path in an unweighted graph      | Explores level by level                     |
| Need to discover connected components          | Systematically covers all reachable nodes   |
| Working with social, web, or computer networks | Natural representation for graph structures |

---

## 📘 **Summary**

| Property                | Description                              |
| ----------------------- | ---------------------------------------- |
| **Traversal Order**     | Level-by-level                           |
| **Data Structure Used** | Queue (FIFO)                             |
| **Ideal For**           | Shortest paths, network analysis         |
| **Complexity**          | O(V + E)                                 |
| **Applications**        | Maps, Social Media, Crawlers, Networking |

---

### 🧩 Example Visualization

```
Graph:
A — B — D
|   |
C   E

BFS Traversal (start from A):
A → B → C → D → E
```
