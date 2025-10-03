### 1. What is a Hash Table?

A **hash table** (or hash map) is a **key–value data structure**.

* You don’t search by index like arrays.
* Instead, you use a **key** → a hash function converts that key into an index where the value is stored.

👉 Think of it like a **dictionary** in real life:

* Word = Key
* Definition = Value
* The dictionary “hashes” the word to find its page quickly.

---

### 2. Components

* **Key**: Identifier (like “username”).
* **Value**: Data stored (like “Sarmad123”).
* **Hash Function**: Converts key into an index in an array.
* **Buckets/Slots**: The array positions where data is stored.

---

### 3. Operations

* **Insert** (key, value) → Hash the key, put value in the slot.
* **Search** (key) → Hash key, go to slot, return value.
* **Delete** (key) → Hash key, find slot, remove it.

---

### 4. Collisions

Sometimes, two keys hash to the **same index**.

* **Chaining** → Each slot stores a linked list of values.
* **Open Addressing** → Find another free slot nearby.

---

### 5. Python Example (using `dict`)

```python
# Create a hash table (dict in Python)
hash_table = {}

# Insert
hash_table["name"] = "Alice"
hash_table["age"] = 25
hash_table["city"] = "Lahore"
print("Hash Table:", hash_table)

# Search
print("Name:", hash_table["name"])

# Delete
del hash_table["age"]
print("After deletion:", hash_table)
```

Output (roughly):

```bash
Hash Table: {'name': 'Alice', 'age': 25, 'city': 'Lahore'}
Name: Alice
After deletion: {'name': 'Alice', 'city': 'Lahore'}
```

---

### 6. Real-Life / Computer Uses

* **Databases** → Indexing (fast lookups).
* **Compilers** → Symbol tables.
* **Caching** → Store recent results for quick access.
* **Password storage** → Hashing for security.

---

✨ Quick check for you:
Imagine we use a hash table to store **student roll numbers** (key) and their **names** (value).
If roll number `101` maps to `"Ali"`, and `105` also maps to the same hash slot — what problem did we just face, and what’s one way to handle it?
