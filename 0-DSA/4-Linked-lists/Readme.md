### 1. What is a Linked List?

A **linked list** is a linear data structure, but unlike arrays, elements are **not stored in contiguous memory**.

* Each element (called a **node**) has:

  1. **Data** → the value
  2. **Pointer/Reference** → link to the next node

👉 Think of a **train**:

* Each bogie (node) has passengers (data) and a connector (pointer) to the next bogie.

---

### 2. Types of Linked Lists

1. **Singly Linked List** → each node points to the next one.
2. **Doubly Linked List** → nodes point both **forward** and **backward**.
3. **Circular Linked List** → the last node points back to the first node.

---

### 3. Operations

* **Traversal** → Go through nodes one by one.
* **Insertion** → Add node at beginning, end, or middle.
* **Deletion** → Remove a node.
* **Search** → Find an element by value.

---

### 4. Python Example (Singly Linked List)

```python
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If empty list
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Print linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.display()
```

Output:

```bash
A -> B -> C -> None
```

---

### 5. Real-Life / Computer Uses

* **Undo functionality** (move back and forth between states).
* **Music playlists** (next/previous songs).
* **Image viewers** (next/previous images).
* **Dynamic memory allocation** (OS uses linked lists for memory blocks).

---

✨ Quick check for you:
If you want to **insert an element in the middle of a linked list**, why might it be **faster** than doing the same in an array?
