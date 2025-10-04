### 1. What is a Queue?

A **queue** is a **linear data structure** that works on the **FIFO principle**:
👉 **First In, First Out** — the first element added is the first one to be removed.

**Real-life analogy:**

* Think of a line at a ticket counter. The first person who enters the line is the first to get the ticket and leave.

---

### 2. Key Operations

Here are the main things you can do with a queue:

* **Enqueue** → Add an element to the end of the queue.
* **Dequeue** → Remove an element from the front of the queue.
* **Peek/Front** → See the front element without removing it.
* **IsEmpty** → Check if the queue is empty.
* **Size** → Count how many elements are in the queue.

---

### 3. Types of Queues

* **Simple Queue**: Basic FIFO.
* **Circular Queue**: Connects end to front, efficient use of memory.
* **Deque (Double-Ended Queue)**: Can add/remove from both ends.
* **Priority Queue**: Elements are dequeued based on priority, not order.

---

### 4. Python Example (Simple Queue using `collections.deque`)

```python
from collections import deque

# Create a queue
queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after enqueuing:", queue)

# Dequeue
front = queue.popleft()
print("Dequeued element:", front)
print("Queue after dequeuing:", queue)

# Peek
print("Front element:", queue[0])

# Check size
print("Queue size:", len(queue))
```

Output (roughly):

```bash
Queue after enqueuing: deque(['A', 'B', 'C'])
Dequeued element: A
Queue after dequeuing: deque(['B', 'C'])
Front element: B
Queue size: 2
```


### 📌 Where **Queues** are used:

1. **Print Spoolers** → Documents sent to the printer wait in a queue. First document in → printed first.
2. **CPU Scheduling** → Processes waiting for execution are in a queue.
3. **Customer Support Systems** → Calls or tickets are queued, handled in arrival order.
4. **Messaging Systems (WhatsApp, Kafka, RabbitMQ)** → Messages are enqueued and processed FIFO.



---

✨ Quick check for you:
If we enqueue `D` and then dequeue once, which element will be removed?
