---
layout: posts
classes: wide
title:  "Generating permutations"
author_profile: true
---

In this post, we will discuss the problem of generating all permutations of a given set of elements. A permutation is an arrangement of elements in a specific order. The table below shows all permutations of the set {1, 2, 3}:

| Permutations {1,2,3}  |
|-----------------------------|
| {1, 2, 3}                   |
| {1, 3, 2}                   |
| {2, 1, 3}                   |
| {2, 3, 1}                   |
| {3, 1, 2}                   |
| {3, 2, 1}                   |
|-----------------------------|

For a set of n elements, there are n! permutations. The problem of generating all permutations of a set of elements is a common problem in computer science and has applications in various fields, such as combinatorial optimization, cryptography, and data analysis.


## 1. The Minimal changes algorithm

To generate all permutations, the minimal changes algorithm start from an empty set and add accordingly the elements one by one till we get the full set.

An example of generating all permutations for 3 elements is shown below:
 > - start with one element: $$\{1\}$$
    - add the second element to $$\{1\}$$ from right to left: $$\{1, 2\}, \{2, 1\}$$  
        - add the third element to $$\{1, 2\}$$ from right to left: $$\{1, 2, 3\}, \{1, 3, 2\}, \{3, 1, 2\}$$
        - add the third element to $$\{2, 1\}$$ from right to left: $$\{2, 1, 3\}, \{2, 3, 1\}, \{3, 2, 1\}$$



## 2. The Johnson-Trotter algorithm

Instead  of generating all permutations starting from an empty set, the Johnson-Trotter algorithm generates permutations by defining a set of rules that determines the next permutation from the current one. 
- A mobile element is an element that is greater than the element it is pointing to.
- A direction is the direction in which an element is pointing. An element can point to the left or right.
- When moving an element, we swap it with the element it is pointing to and change the direction of all elements greater than it.

Lets take the example of generating all permutations for 3 elements using the Johnson-Trotter algorithm:
 > - start with the permutation $$\{ \overleftarrow{1}, \overleftarrow{2}, \overleftarrow{3}\}$$
- find the largest mobile element: $$3$$ (Note that there is two mobile elements: $$3$$ and $$2$$ and we should take the largest one)
- swap $$3$$ with the element it is pointing to: $$\{ \overleftarrow{1}, \overleftarrow{3}, \overleftarrow{2}\}$$
- change the direction of all elements greater than $$3$$: No change since there is no element greater than $$3$$
- Repeat the process until there is no mobile element.

 The following table summarizes the steps of the Johnson-Trotter algorithm for generating all permutations of 3 elements:

 |Permutation|Mobile element|Direction change|
    |:----------------:|:----------------:|:------|------------------:|
    |$$\{ \overleftarrow{1}, \overleftarrow{2}, \overleftarrow{3}\}$$|$$3$$|No change|
    |$$\{ \overleftarrow{1}, \overleftarrow{3}, \overleftarrow{2}\}$$|$$3$$|No change|
    |$$\{ \overleftarrow{3}, \overleftarrow{1}, \overleftarrow{2}\}$$|$$2$$|$$\{ \overrightarrow{3}\}$$|
    |$$\{ \overrightarrow{3}, \overleftarrow{2}, \overleftarrow{1}\}$$|$$3$$|No change|
    |$$\{ \overleftarrow{2}, \overrightarrow{3}, \overleftarrow{1}\}$$|$$3$$|No change|
    |$$\{ \overleftarrow{2}, \overleftarrow{1}, \overrightarrow{3}\}$$|No mobile||
    |-|-|-|



