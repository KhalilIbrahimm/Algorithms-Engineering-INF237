
# Week 3 – Heaps and Sliding Window Techniques

This folder contains competitive programming solutions focusing on **window optimization**, **sequence analysis**, and **efficient heap usage**. 

---

## Problem Overview

### 1. [Tree Shopping](https://uib.kattis.com/courses/INF237/spring25/assignments/wws2t8/problems/treeshopping)  
Given a list of tree heights, find the smallest difference in height between the tallest and shortest tree in any contiguous block of exactly `k` trees.  
The solution uses a dual heap (min/max) combined with a sliding window to efficiently track height extremes.

**Key Concepts:**  
- Sliding window minimum and maximum  
- Min/max heaps (`heapq`)  
- Optimization under fixed-length constraints  

**File:** `treeshopping.py`

---

### 2. [Martian DNA](https://uib.kattis.com/courses/INF237/spring25/assignments/wws2t8/problems/uib.martiandna)  
Given a DNA sequence and a list of base count requirements, find the shortest contiguous subsequence that satisfies all constraints.  
The solution uses an efficient **two-pointer sliding window** approach to maintain and reduce the valid window length.

**Key Concepts:**  
- Sliding window with counters  
- Sequence matching with constraints  
- Dictionary-based pattern tracking  

**File:** `martiandna.py`

---

## Skills Demonstrated

- Efficient use of heap structures and priority queues  
- Real-time frequency tracking in linear time  
- Search space minimization with sliding window algorithms  

---
