
# Week 2 – Graph Theory and Search Algorithms

This folder contains solutions to algorithmic problems from the Kattis online judge, focused on **graph theory**, **search algorithms**, and **connectivity properties**. All problems were solved as part of a structured programming course using competitive problem-solving to build algorithmic fluency.

The problems simulate real-world system modeling scenarios such as resource partitioning and network connectivity validation – useful skills in fields like logistics, system architecture, and distributed systems.

## Problem Overview

### 1. [Breaking Bad](https://open.kattis.com/problems/breakingbad)
**Problem type:** Bipartite graph checking (conflict-free grouping)

> Given a set of suspicious items and relationships between them, determine whether it’s possible to divide them into two groups such that no connected items end up in the same group.  
>  
> The solution uses **Breadth-First Search (BFS)** to verify if the graph is bipartite, and partitions nodes accordingly.

**Key Concepts:**  
- Graph construction using adjacency lists  
- BFS traversal  
- Bipartite detection and coloring  
- Robust handling of disconnected components

**File:** `breakingbad.py`

---

### 2. [Reversing Roads](https://open.kattis.com/contests/z25ng5/problems/reversingroads)
**Problem type:** Strongly Connected Components (SCC), Graph reversal simulation

> You are given a directed graph. Check if it is strongly connected. If not, test whether reversing exactly one edge could make the graph strongly connected.  
>  
> The solution applies **Depth-First Search (DFS)** and graph transposition logic, emulating edge reversal one by one with minimal recomputation.

**Key Concepts:**  
- DFS reachability check  
- Reverse graph construction (transposition)  
- Simulation of single-edge reversal  

**File:** `reversingroads.py`
