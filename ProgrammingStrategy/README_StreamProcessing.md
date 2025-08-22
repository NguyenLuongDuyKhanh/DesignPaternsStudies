# Stream Processing

* **Definition**: A way of handling **data sequences (streams)** by processing elements **as they arrive**, instead of waiting for the whole dataset.
* **Key idea**: *Process data in motion, often continuously*.
* Common in **real-time systems**, **big data pipelines**, and **event-driven apps**.
* **Advantages**:

  * Lower memory usage (don’t need to load all data at once)
  * Can handle infinite/unbounded streams (e.g., live sensor data, logs, Kafka events)
  * Real-time processing possible

**Example in Python:**

```python
def process(stream):
    for event in stream:
        print(f"Processed: {event}")

data = (x for x in range(1, 6))  # generator = stream
process(data)
```

Here, elements are consumed like a data stream.

✅ Frameworks: **Apache Kafka, Apache Flink, Spark Streaming, RxPy** (ReactiveX in Python).

---

## ✅ Key Difference

| Feature           | Lazy Evaluation                         | Stream Processing                               |
| ----------------- | --------------------------------------- | ----------------------------------------------- |
| **When computed** | Only when result is needed              | As data flows in (often real-time)              |
| **Focus**         | Avoid unnecessary work                  | Continuous processing of data                   |
| **Typical use**   | Infinite lists, delayed computation     | Real-time event/log/IoT data pipelines          |
| **Example**       | Generator that yields values when asked | Kafka consumer that processes incoming messages |

---

🔎 **Analogy**:

* **Lazy evaluation** = "I’ll cook a dish only when you order it."
* **Stream processing** = "I’ll cook dishes one by one as customers arrive, without waiting for everyone to order first."

---

👉 Do you want me to also show how **Python’s generators** combine *both* lazy evaluation and stream processing? That’s often where the two meet.
