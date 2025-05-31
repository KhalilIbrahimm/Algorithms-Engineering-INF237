
This repository contains solutions to geometry-themed programming problems. Each problem involves geometric reasoning, such as point-in-triangle tests or circle coverage. Solutions are written in Python and thoroughly commented.

---

## [Mosquitoes](https://uib.kattis.com/courses/INF237/spring25/assignments/j35uir/problems/mosquitoes)

**Problem Summary:**  
You are given the positions of several mosquitoes on a 2D plane and a bowl with a fixed diameter. The goal is to find the maximum number of mosquitoes that can be caught within a single placement of the bowl.

**Approach:**  
- Try each mosquito as a potential center of the bowl.
- Also check centers derived from pairs of mosquitoes that can be enclosed together.
- For each candidate center, count how many mosquitoes lie within or on the bowl's boundary.

**File:** `mosquitoes.py`

---

## [Jabuke](https://uib.kattis.com/courses/INF237/spring25/assignments/j35uir/problems/jabuke)

**Problem Summary:**  
You are given the coordinates of a triangle and a list of apple trees. Your task is to calculate the area of the triangle and count how many trees lie strictly inside or on its edges.

**Approach:**  
- Use the determinant method to compute the triangle's area.
- For each apple tree, compare the total area of sub-triangles formed with the point to the triangle's area.
- If the sum matches, the point lies inside or on the triangle.

**File:** `jabuke.py`

---
