
# Week 6 – Segment Trees and Simulation Problems

This week is focused on **range queries and updates** using **segment trees**, solving two classic simulation problems from competitive programming.
---

## Segment Tree
- A segment tree is a binary tree data structure used to perform efficient range queries and point updates on an array.
- It is ideal when you need to repeatedly:
    - Query information over a subrange (e.g., sum, min, max)
    - Update a value in the array, and reflect that change in queries

### Key Properties
- Time complexity:
    - Query: O(log n)
    - Update: O(log n)
- Space complexity:
    - Typically $2 * 2^ceil(log₂(n))$ = around $4n$ 


## Problem Overview

### 1. [Turbo Sort](https://uib.kattis.com/courses/INF237/spring25/assignments/uze6xy/problems/turbo)  
Simulate a custom sorting process by iteratively removing the smallest or largest element and counting how many swaps it would take to reach its final position.

The solution uses a **segment tree** to efficiently track the number of active positions and support range queries in O(log n) time.

**Key Concepts:**  
- Custom sorting simulation  
- Range sum queries  
- Segment tree for active index tracking

**File:** `turbo.py`

---

### 2. [Movie Collection](https://uib.kattis.com/courses/INF237/spring25/assignments/uze6xy/problems/moviecollection)  
Simulate a stack of movies. For each request, report how many movies are above the one requested and move the movie to the top.

This problem is solved using a **segment tree**, where each index indicates whether a position in the stack is occupied.

**Key Concepts:**  
- Stack reordering simulation  
- Range sum queries for element counting  
- Dynamic tree updates after each operation

**File:** `moviecollection.py`

---

## What These Problems Demonstrate

- Full understanding and practical implementation of **segment trees**
- Real-time updates of array state and cumulative properties
- Efficient simulations that scale with large input sizes
- Application of data structures to complex interaction models

---
