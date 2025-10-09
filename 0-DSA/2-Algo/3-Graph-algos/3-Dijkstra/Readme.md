Perfect 👏 — now we’re stepping into **weighted graph algorithms**, and **Dijkstra’s Algorithm** is the cornerstone of them all.

Let’s break it down in the same structured, documentation-style format so it fits your learning system (and your README structure).

---

# 🚀 Dijkstra’s Algorithm

## 📘 Overview

**Dijkstra’s Algorithm** is used to find the **shortest path** between nodes in a **weighted graph** (where each edge has a cost or distance).

It answers questions like:

> “What’s the fastest route from A to B?”
> “What’s the minimum cost to send data across a network?”

It’s a **greedy algorithm**, meaning it always picks the **next closest node** at every step — building the shortest path incrementally.

---

## ⚙️ How It Works

Let’s say we’re finding the shortest path from a **source node** to all other nodes.

1. **Start** with a source node.

   * Set its distance = 0, and all others = ∞ (infinity).
2. Pick the **unvisited node** with the **smallest known distance**.
3. From that node, **update the distances** to its neighboring nodes:

   * `new_distance = current_distance + edge_weight`
   * If `new_distance < old_distance`, update it.
4. Mark the node as **visited** (we’ve found its shortest path).
5. Repeat until all nodes are visited or the target node is reached.

---

## 🧠 Intuition / Analogy

Think of it as **Google Maps route finder**:

* You’re at a starting point.
* You always pick the **nearest intersection** you can reach.
* Then, from there, you expand outward, choosing the next closest reachable point.
* Step by step, you build the shortest travel path to every destination.

That’s exactly Dijkstra’s process.

---

## 🧩 Pseudocode (Simplified)

```python
import heapq

def dijkstra(graph, start):
    # graph = {'A': {'B': 2, 'C': 4}, ...}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # priority queue (min-heap)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

---

## 🗺️ Example

```python
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'E': 3},
    'D': {'F': 1},
    'E': {'D': 2, 'F': 5},
    'F': {}
}

print(dijkstra(graph, 'A'))
```

**Output:**

```
{'A': 0, 'B': 2, 'C': 3, 'D': 8, 'E': 6, 'F': 9}
```

Meaning — the shortest path from A to F costs 9 units.

---

## 🧩 Real-World Applications

| Use Case                                     | Description                                                           |
| -------------------------------------------- | --------------------------------------------------------------------- |
| **Navigation Systems (Google Maps, Uber)**   | Finds the shortest route between locations based on time or distance. |
| **Network Routing (e.g., Internet packets)** | Determines the shortest/least-cost path between nodes in a network.   |
| **Game Development (Pathfinding AI)**        | Helps NPCs find the fastest route to a target.                        |
| **Robot Motion Planning**                    | Used in robotics to plan efficient movement paths.                    |
| **Telecom & Data Transfer**                  | Optimizes routing for data to reduce latency and cost.                |

---

## 🧮 Complexity

| Operation                   | Complexity           |
| --------------------------- | -------------------- |
| Time (using priority queue) | **O((V + E) log V)** |
| Space                       | **O(V)**             |

---

## ⚖️ When to Use

✅ When you need the **shortest path** in a **weighted** graph (with positive weights).
❌ Not suitable when there are **negative weights** (use **Bellman-Ford** instead).

---

## 🧩 Example Analogy

Think of cities connected by roads.
Each road has a distance.
You start in **City A** and want to reach **City Z** with **minimum total distance**.
You pick the shortest road at each step and gradually find the best route — that’s **Dijkstra’s Algorithm** in practice.
