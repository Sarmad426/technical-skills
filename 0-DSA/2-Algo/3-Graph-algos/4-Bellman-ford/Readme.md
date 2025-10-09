# ⚙️ Bellman-Ford Algorithm

## 📘 Overview

**Bellman-Ford Algorithm** is another **shortest path algorithm**, similar to Dijkstra —
but the key difference is:

> 🧠 It can handle **negative edge weights** (and even detect **negative weight cycles**).

That’s what makes it essential for graphs where edges may reduce total cost (like debts, currency exchanges, or variable costs).

---

## 💡 Why Bellman-Ford?

Dijkstra fails when you have **negative edge weights**, because its greedy nature assumes “shortest now = shortest later.”
Bellman-Ford doesn’t make that assumption — it **relaxes all edges repeatedly**, ensuring even negative weights are considered correctly.

---

## 🧩 How It Works (Conceptually)

1. **Initialize distances**:

   * Distance to source = 0
   * All others = ∞ (infinity)

2. **Relax all edges** `V-1` times (V = number of vertices):

   * For each edge `(u, v)` with weight `w`:

     ```
     if distance[u] + w < distance[v]:
         distance[v] = distance[u] + w
     ```

3. **Check for negative weight cycles** (optional step):

   * Run one more iteration — if any distance still improves → a negative cycle exists.

---

## 🧮 Time Complexity

| Operation | Complexity                          |
| --------- | ----------------------------------- |
| Time      | **O(V × E)** (slower than Dijkstra) |
| Space     | **O(V)**                            |

So it’s slower, but **more powerful** (handles negative edges).

---

## 🧩 Python Example

```python
def bellman_ford(graph, vertices, start):
    distance = {v: float('inf') for v in vertices}
    distance[start] = 0

    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative weight cycles
    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            print("Negative weight cycle detected")
            return None

    return distance


edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('C', 'B', -1),
    ('B', 'D', 2),
    ('C', 'D', 3)
]

vertices = ['A', 'B', 'C', 'D']
print(bellman_ford(edges, vertices, 'A'))
```

**Output:**

```
{'A': 0, 'B': 1, 'C': 2, 'D': 4}
```

---

## 🌍 Real-World Applications

| Use Case                                     | Description                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------- |
| **Financial Modeling / Currency Conversion** | Detects negative cycles that could represent arbitrage opportunities.           |
| **Network Routing (like RIP protocol)**      | Handles variable link costs that can be negative (due to congestion or policy). |
| **Pathfinding with Penalties**               | Useful when certain paths have rewards or penalties (negative costs).           |

---

## ⚖️ Bellman-Ford vs Dijkstra

| Feature                  | **Dijkstra**            | **Bellman-Ford**                      |
| ------------------------ | ----------------------- | ------------------------------------- |
| Handles negative weights | ❌ No                    | ✅ Yes                                 |
| Detects negative cycles  | ❌ No                    | ✅ Yes                                 |
| Time Complexity          | O((V + E) log V)        | O(V × E)                              |
| Approach                 | Greedy (Priority Queue) | Dynamic Programming (Edge Relaxation) |
| Speed                    | ⚡ Fast                  | 🐢 Slower                             |
| Use case                 | Positive weights        | Mixed or negative weights             |

---

## 🎯 TL;DR

> 🔹 **Dijkstra** = Fast, for positive weights
> 🔹 **Bellman-Ford** = Slower, but works even when weights are negative or unstable
