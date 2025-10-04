# Trees: BST, AVL, and B-Tree — organized step-by-step


## 1. Binary Search Tree (BST)

### Definition
A BST is a binary tree where for every node:
- Left subtree values < node value
- Right subtree values > node value
This property holds recursively.

### Insertion Logic (short)
1. Start at the root.
2. Compare value: go left if smaller, right if larger.
3. Repeat until you find a null child, then insert.

### Example (step-by-step): Insert 5, 7, 8, 3, 6, 2, 4
Start with an empty tree and add elements one by one.

Step 1: Insert 5
```
5
```

Step 2: Insert 7 (7 > 5 → right)
```
5
 \
  7
```

Step 3: Insert 8 (8 > 5 → right; 8 > 7 → right)
```
5
 \
  7
   \
    8
```

Step 4: Insert 3 (3 < 5 → left)
```
  5
 / \
3   7
     \
      8
```

Step 5: Insert 6 (6 > 5 → right; 6 < 7 → left)
```
    5
   / \
  3   7
     / \
    6   8
```

Step 6: Insert 2 (2 < 5 → left; 2 < 3 → left)
```
      5
     / \
    3   7
   /   / \
  2   6   8
```

Step 7: Insert 4 (4 < 5 → left; 4 > 3 → right)
```
      5
     / \
    3   7
   / \ / \
  2  4 6  8
```

Final BST:
```
      5
     / \
    3   7
   / \ / \
  2  4 6  8
```

### Traversals (on final BST)
- Inorder (L, Root, R) → 2, 3, 4, 5, 6, 7, 8 (sorted)
- Preorder (Root, L, R) → 5, 3, 2, 4, 7, 6, 8
- Postorder (L, R, Root) → 2, 4, 3, 6, 8, 7, 5

### Pros / Cons / Use cases
- Pros: Simple; average O(log n) for ops.
- Cons: Can become unbalanced → worst-case O(n).
- Use cases: In-memory datasets with random insertions, basic symbol tables.

---

## 2. AVL Tree (self-balancing BST)

### Definition
An AVL Tree is a BST that maintains a height-balance property: for every node, the heights of left and right subtrees differ by at most 1. Rebalancing uses rotations (left, right, left-right, right-left).

### Insertion concept
- Insert like BST.
- After insertion, update heights and balance factors upward.
- If a node becomes unbalanced (factor > 1 or < -1), perform appropriate rotation(s) to restore balance.

### Example (step-by-step): Insert 10, 20, 30, 40, 50, 25
Step 1: Insert 10
```
10
```

Step 2: Insert 20 (right of 10)
```
10
 \
 20
```

Step 3: Insert 30 (right of 10 → right of 20). Unbalanced at 10 (right-right case) → left rotate at 10
Before rotation:
```
10
 \
 20
  \
   30
```
After left rotation at 10:
```
 20
 / \
10  30
```

Step 4: Insert 40 (goes right of 30)
```
  20
  / \
10  30
      \
       40
```

Step 5: Insert 50 (right of 40). Unbalanced at 30 (right-right) → left rotate at 30
Before rotation:
```
  20
  / \
10  30
      \
       40
         \
          50
```
After rotation at 30:
```
   20
  /  \
10    40
      / \
     30  50
```

Step 6: Insert 25 (25 > 20 → right; 25 < 40 → left; 25 < 30 → left of 30)
```
     20
    /  \
  10    40
        / \
      30  50
     /
   25
```
Now node 20's right subtree is heavier with a right-left case at 20 → perform right rotation on 40, then left rotation on 20 (right-left double rotation).

Final AVL Tree:
```
      30
     /  \
   20    40
  /  \     \
10   25    50
```

### Pros / Cons / Use cases
- Pros: Guaranteed O(log n) for search/insert/delete; good lookup performance.
- Cons: More complex; rotations add overhead on writes.
- Use cases: In-memory indices, situations requiring strict balance and fast lookups.

---

## 3. B-Tree (balanced multi-way tree, good for disk)

### Definition
A B-Tree of order m allows each node to have up to m children and up to m-1 keys. It is height-balanced and designed to minimize disk reads/writes by storing multiple keys per node.

### Properties (brief)
- All leaves at same depth.
- Nodes (except root) have between ceil(m/2)-1 and m-1 keys.
- Splits and merges during insert/delete keep the tree balanced.

### Example (order = 3, meaning node keys between 1 and 2? Commonly order = max children; here we use 3 → nodes can have 2 keys max)
We'll use the sequence: 10, 20, 5, 6, 12, 30, 7, 17. Show how nodes split as they overflow.

Step 1: Insert 10 → [10]

Step 2: Insert 20 → [10, 20]

Step 3: Insert 5 → [5, 10, 20]

Step 4: Insert 6 → Node would have 4 keys (overflow); split around middle key (10). 10 becomes root.
Before split: [5,6,10,20]
After split:
```
      [10]
     /    \
  [5,6]  [20]
```

Step 5: Insert 12 → goes to right child [20] → [12,20]

Step 6: Insert 30 → right child becomes [12,20,30]

Step 7: Insert 7 → goes to left child [5,6] → becomes [5,6,7]

Step 8: Insert 17 → goes to right child [12,20,30]; that node overflows on inserting 17 → split around 20. 20 moves up into root.
After split:
```
     [10,20]
    /   |   \
[5,6,7] [12,17] [30]
```

Final B-Tree (balanced and shallow) is ideal for minimizing disk accesses.

### Pros / Cons / Use cases
- Pros: Low height, minimizes disk I/O; suited for large datasets stored on disk.
- Cons: More complex implementation than binary trees.
- Use cases: Database indexes, file systems.

---

## Comparison (concise)
- BST: Simple, good for in-memory when data is random; can degrade to O(n).
- AVL: Balanced binary tree; guaranteed O(log n); better for read-heavy workloads.
- B-Tree: Multi-way balanced tree; optimized for disk I/O and very large datasets.

---

## Quick Reference / Takeaways
- Follow insertion step-by-step to understand structure evolution.
- BST teaches basic ordering and traversal concepts.
- AVL teaches rotations and maintaining balance.
- B-Tree teaches node splitting and disk-oriented design.
