### 1. What is a Stack?

A **stack** is a **linear data structure** that works on the **LIFO principle**:
👉 **Last In, First Out** — the most recently added element is the first to be removed.

Real-life analogy:

* Think of a stack of plates. You put the newest plate on top, and when you remove, you always take the top plate first.

---

### 2. Key Operations

* **Push** → Add an element to the top of the stack.
* **Pop** → Remove the top element from the stack.
* **Peek/Top** → Look at the top element without removing it.
* **IsEmpty** → Check if the stack is empty.
* **Size** → Count the number of elements.

---

### 3. Types of Stacks

* **Simple Stack** → Basic LIFO.
* **Two-Stack Structures** → Sometimes used in advanced problems (e.g., implementing a queue with two stacks).
* **Stack in Recursion** → The function call stack is an example (each function call is “pushed” and “popped”).

---

### 4. Python Example (Stack using `list`)

```python
# Create a stack
stack = []

# Push
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack after pushing:", stack)

# Pop
top = stack.pop()
print("Popped element:", top)
print("Stack after popping:", stack)

# Peek
print("Top element:", stack[-1])

# Size
print("Stack size:", len(stack))
```

Output (roughly):

```bash
Stack after pushing: ['A', 'B', 'C']
Popped element: C
Stack after popping: ['A', 'B']
Top element: B
Stack size: 2
```

### 📌 Where **Stacks** are used:

1. **Undo/Redo in editors** → Every action is “pushed” on a stack. Undo = pop the last action.
2. **Function calls (Recursion)** → Each function call goes on the **call stack**, popped when the function returns.
3. **Back/Forward in browsers** → Pages are stacked; when you press back, it pops the most recent page.
4. **Expression evaluation** → Compilers use stacks for arithmetic evaluation and parsing parentheses.

   * Example: `(2 + (3 * 4))` → handled by stacks internally.


If the current stack is `['A', 'B', 'C']`, and we push D, then pop once — which element will be removed?