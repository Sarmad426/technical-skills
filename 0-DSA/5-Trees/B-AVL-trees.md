### 1. Introduction to B-Trees

A **B-tree** (short for Balanced tree) is a self-balancing search tree data structure, commonly used in databases and file systems. It's designed to keep data sorted while allowing efficient insertion and deletion operations.

Key characteristics:

*   Each node can have more than two children.
*   The number of children at each level increases by one from left to right.
*   All internal nodes are fully balanced.

### 2. B-Trees Properties

*   **Fully Balanced**: Nodes maintain a balance between the height and the number of keys, ensuring efficient search
operations.
*   **Non-Empty Nodes**: All non-empty nodes have at least two children (left child and right child).
*   **Leaf Nodes**: The lowest level of the tree consists of leaf nodes.

### 3. B-Trees Operations

*   **Insertion**: Inserting a new key in a B-tree involves creating a new node if necessary, then balancing the tree.
*   **Deletion**: Deleting a key from a B-tree requires rebalancing the tree to maintain the balance property.

### 4. Advantages of B-Trees

*   **Efficient Search**: B-trees provide fast search operations with an average time complexity of O(log n).
*   **Balanced Tree**: The self-balancing nature ensures that the height of the tree remains relatively constant, leading to
efficient insertion and deletion operations.

### 5. Disadvantages of B-Trees

*   **Insertion and Deletion Overhead**: Inserting or deleting a key in a B-tree can lead to the creation of new nodes,
potentially affecting performance.
*   **Space Complexity**: B-trees require more memory compared to other data structures like arrays.

### 6. AVL Trees vs. B-Trees

While both trees are self-balancing search trees, there are some key differences:

*   **Balancing Factor**: In an AVL tree, the balancing factor is calculated as (height of left subtree) - (height of right
subtree). In a B-tree, the balancing factor is calculated as 2 times the number of children minus one.
*   **Number of Children**: In an AVL tree, each node can have at most two children. In a B-tree, nodes can have more than two
children.
*   **Balancing Algorithm**: AVL trees use a specific algorithm to balance the tree when the balancing factor is greater than 1
or less than -1. B-trees use a different algorithm that involves rebalancing the tree based on the number of keys.

### 7. Comparison with Other Data Structures

| Operation | Array | Linked List | AVL Tree | B-Tree |
| --- | --- | --- | --- | --- |
| Insertion | O(n) | O(1) | O(log n) | O(log n) |
| Deletion | O(n) | O(1) | O(log n) | O(log n) |

In general, AVL trees and B-trees offer better performance than arrays and linked lists for insertion and deletion operations.
However, they may have higher space complexity compared to arrays and linked lists.

Here's an example implementation of a B-tree in Python:
```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BTreeNode:
    def __init__(self, degree, leaf=False):
        self.degree = degree
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, degree=3):
        self.root = BTreeNode(degree)

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.root.degree) - 1:
            # Splitting process
            temp = Node(key)
            self.split_child(root, 0)
            self.insert_non_full(temp)
        else:
            # Inserting into an internal node
            self.insert_non_full(key)

    def insert_non_full(self, key):
        root = self.root
        i = len(root.keys) - 1
        while i >= 0:
            if key < root.keys[i]:
                if root.child[i].leaf:
                    # Inserting into a leaf node
                    root.insert_non_leaf(key)
                    break
                else:
                    i -= 1
            elif key > root.keys[i]:
                pass
            else:
                return

        # Creating a new node and inserting it
        new_node = Node(key)
        self.split_child(root, i + 1)
        self.insert_non_full(key)

    def split_child(self, root, index):
        degree = root.degree
        child = root.child[index]
        t = Node(child.key)
        child.key = float('inf')
        if len(child.keys) < degree // 2:
            # Splitting the left child
            self.split_child(root, index - 1)
            t.left = child.left
            child.left = None
            root.keys.insert(index, child.key)
            child.keys.append(float('inf'))
            root.child.insert(index + 1, t)
        else:
            # Splitting the right child
            if len(child.right):
                self.split_child(root, index + 1)
                t.right = child.right
                child.right = None
                root.keys.insert(index, float('inf'))
                child.key = t.key
                t.key = float('inf')
                root.child.insert(index, t)
                return

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if not node:
            return
        print("Node Key:", node.key)
        if node.leaf:
            for key in node.keys:
                print(key, end=' ')
        else:
            print("(Internal Node)")
            print("Keys:", node.keys)
            print("Children:")
            for child in node.child:
                self._print_tree(child)

# Usage
btree = BTree()
btree.insert(10)
btree.insert(20)
btree.insert(30)
btree.print_tree()
```
