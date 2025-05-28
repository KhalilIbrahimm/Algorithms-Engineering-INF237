
# Week 4 – Dynamic Programming and Layout Optimization

This folder includes Python implementations for algorithmic problems solved as part of a structured training in dynamic programming and layout optimization. These problems were selected for their focus on **decision tracking**, **subproblem memoization**, and **sequence formatting under constraints**.

---

## Problem Overview

### 1. [Nikola](https://uib.kattis.com/courses/INF237/spring25/assignments/v5hbjk/problems/nikola)  
Nikola must jump across a path of tiles, minimizing the total cost of his journey while obeying specific jumping rules.  

The solution applies **recursive dynamic programming with memoization** to handle branching jump paths efficiently.

**Key Concepts:**  
- Top-down memoization  
- State modeling with `(position, jump_length)`  
- Forward/backward movement simulation  

**File:** `nikola.py`

---

### 2. [Word Clouds](https://uib.kattis.com/courses/INF237/spring25/assignments/v5hbjk/problems/wordclouds)  
Given a set of words with defined width and height, compute the minimal height needed to arrange all words in lines constrained by maximum row width.  

The solution uses **bottom-up dynamic programming**, optimizing each suffix layout by testing all valid row breaks.

**Key Concepts:**  
- Sliding subrange optimization  
- Minimal layout generation  
- Text-wrapping under height constraints  

**File:** `wordclouds.py`

---

## What You’ll See in This Code

- **Efficient Recursive Thinking:** Both problems simulate decision paths with bounded choices (jump forward/back, wrap line or not)
- **Optimal Substructure Usage:** Memoization and DP table show clear subproblem definitions
- **Readable, Modular Code:** Each function serves a single purpose, with clear variable naming and separation of concerns
