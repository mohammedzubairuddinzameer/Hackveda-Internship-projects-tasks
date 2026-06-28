# 🚀 CodeOptimizeX Performance Optimization using cProfile & Snakeviz

## 📌 Overview

This project demonstrates how to identify and optimize performance bottlenecks in Python applications using:

* **cProfile** → for runtime profiling
* **Snakeviz** → for interactive visualization

The goal is to analyze execution flow, detect inefficiencies, and improve performance in the **CodeOptimizeX workflow**.

---

## 🔴 Problem Statement

The CodeOptimizeX workflow experienced delays while processing large datasets.
The objective was to:

* Identify performance bottlenecks
* Analyze function-level execution time
* Optimize inefficient operations

---

## 🔧 Profiling Setup

A reusable profiling utility was implemented using `cProfile`.

### Example Integration

```python
from profiler.profiler import run_with_profiler

if __name__ == "__main__":
    run_with_profiler(workflow)
```

---

## 🧪 Workflow Under Analysis

```python
def workflow():
    data = ["for i in range(1000): pass"] * 100000

    print("[Workflow] Starting analysis...")
    a = analyze_code(data)

    print("[Workflow] Optimizing...")
    b = optimize_code(a)

    return b
```

---

## 📊 Profiling Results

```
400006 function calls in 0.116 seconds

Top contributors:
- optimize_code → 0.064 sec
- analyze_code  → 0.052 sec
- replace()     → high frequency
- append()      → high frequency
- strip()       → moderate usage
```

### 🔍 Key Insight

The performance bottleneck is not a single function, but the **cumulative cost of repeated operations**.

---

## 📈 Visualization with Snakeviz

### Run Command:

```bash
snakeviz outputs/profiles/workflow_*.prof
```

### Insights from Visualization:

* Execution time is split between `analyze_code` and `optimize_code`
* `optimize_code` slightly dominates
* Heavy usage of:

  * `str.replace()`
  * `list.append()`
  * `str.strip()`

---

## 🧠 Bottleneck Analysis

The main performance issues were:

* Repeated string operations (`replace`, `strip`)
* High-frequency list operations (`append`)
* Multiple iterations over large datasets

---

## ⚡ Optimization

### ❌ Before

```python
optimized = []
for line in code_lines:
    optimized.append(line.replace(" ", ""))
```

---

### ✅ After (Optimized)

```python
optimized = [line.replace(" ", "") for line in code_lines]
```

---

### 🚀 Further Optimization

```python
optimized = [line.replace(" ", "") for line in code_lines if " " in line]
```

---

## 📉 Performance Comparison

| Version | Execution Time |
| ------- | -------------- |
| Before  | 0.116 sec      |
| After   | ~0.08 sec      |

### ✅ Improvement:

~25–30% faster execution

---

## 🎥 Demo

The demo includes:

1. Running the workflow
2. Profiling using cProfile
3. Visualizing with Snakeviz
4. Identifying bottlenecks
5. Applying optimizations

---

## 🧩 Project Structure

```
CodeOptimizeX/
│
├── profiler/
│   └── profiler.py
│
├── outputs/
│   └── profiles/
│
├── code_optimizer.py
├── main.py
└── README.md
```

---

## 💡 Future Improvements

* Parallel processing for large datasets
* Caching repeated computations
* Using optimized data structures
* Integrating memory profiling (`tracemalloc`)

---

## ✅ Conclusion

Using **cProfile** and **Snakeviz**, we:

* Identified performance bottlenecks
* Visualized execution flow
* Optimized inefficient operations
* Improved overall execution time

This approach demonstrates a practical and scalable method for **performance tuning in Python applications**.

---

## 🛠️ Requirements

```bash
pip install snakeviz
```

---

## ▶️ How to Run

```bash
python main.py
snakeviz outputs/profiles/workflow_*.prof
```

---

## 📌 Author

Developed as part of internship task for performance optimization in **CodeOptimizeX**.
