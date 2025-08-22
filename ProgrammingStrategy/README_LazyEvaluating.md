# Lazy Evaluation

* **Definition**: An evaluation strategy where expressions are **not computed immediately** but **only when their value is needed**.
* **Key idea**: *Delay work until absolutely necessary*.
* **Advantages**:

  * Avoids unnecessary computation
  * Handles infinite data structures
  * Can improve performance by skipping unused results

**Example in Python (generator):**

```python
def squares():
    n = 1
    while True:
        yield n * n
        n += 1

sq = squares()
print(next(sq))  # 1
print(next(sq))  # 4
print(next(sq))  # 9
```

Here, squares are computed **on demand**, not all at once.

✅ Languages like **Haskell** use lazy evaluation by default.
