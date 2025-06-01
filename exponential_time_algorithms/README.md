
# Week 7 – Backtracking: Map Coloring and N-Queens Variants

This week’s problems demonstrate classic backtracking techniques applied to graph coloring and the N-Queens problem with added complexity. These tasks highlight your ability to manage constraints, prune search trees efficiently, and use recursive state tracking.

---

## 🔗 Problem Overview

### 1. [Map Colouring](https://uib.kattis.com/courses/INF237/spring25/assignments/fkq4rp/problems/mapcolouring)  
Given a set of countries and borders, determine the minimum number of colors needed so no two neighboring countries share a color.

The algorithm uses **backtracking** to attempt coloring the graph using 1 to 4 colors and returns `'many'` if no solution exists within that bound.

**Key Concepts:**  
- Graph coloring  
- Constraint satisfaction  
- Recursive backtracking with early pruning

**File:** `mapcolouring.py`

---

### 2. [Holy N Queens Batman](https://uib.kattis.com/courses/INF237/spring25/assignments/fkq4rp/problems/holeynqueensbatman)  
Count how many ways N queens can be placed on an N×N board with forbidden cells ("holes"), such that no two queens attack each other.

A modified **N-Queens backtracking** is used with additional checks for blocked cells and diagonal conflict management.

**Key Concepts:**  
- N-Queens recursion  
- Diagonal tracking  
- Board constraints and conflict avoidance

**File:** `holeynqueensbatman.py`

---
