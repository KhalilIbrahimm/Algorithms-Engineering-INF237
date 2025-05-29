
# Week 5 – Graph Theory: Prim's Algorithm and Grid-based Flood Simulation

This week’s focus is on real-world applications of **graph traversal** and **priority-based search algorithms**. The two problems in this folder explore minimum spanning trees (MST) and flood-fill logic using heap-based exploration, both relevant in network optimization and simulation tasks.

---

## Problem Overview

### 1. [Nature Reserve](https://uib.kattis.com/courses/INF237/spring25/assignments/e9ruyx/problems/naturereserve)  
Given a network of base stations, determine the minimum energy required to install a program across all stations. Already-installed nodes can broadcast, and others are connected via energy-costly links.

The solution uses **Prim’s Algorithm** with a **min-heap** to incrementally build a **Minimum Spanning Tree**, while tracking the number of program transfers to compute total energy.

**Key Concepts:**  
- MST construction with partial node coverage  
- Energy cost modeling: link activation + transfer  
- Efficient heap management

**File:** `naturereserve.py`

---

### 2. [Emptying the Baltic](https://uib.kattis.com/courses/INF237/spring25/assignments/e9ruyx/problems/emptyingbaltic)  
Given a topographic grid with water levels (negative values), simulate draining the Baltic Sea from a given start cell. Each cell can drain only to cells it can reach through water and only down to the **highest reachable bottom**.

The approach resembles **Dijkstra’s Algorithm**, but adapted to grid-based BFS with **relaxation on maximum elevation**.

**Key Concepts:**  
- Elevation-based propagation using heap  
- 8-directional movement on a grid  
- BFS with drainage-level tracking

**File:** `emptyingbaltic.py`

---

## Technical Strengths Demonstrated

- Heap-based MST (Prim’s) and flood algorithms
- Efficient modeling of dynamic costs (energy, water)
- Robust use of **priority queues**, **relaxation**, and **state memoization**
- Adaptation of standard algorithms to grid and graph contexts

---
