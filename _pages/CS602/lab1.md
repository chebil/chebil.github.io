---
title:  Lab 1
layout: single
classes: wide
permalink: /ProbSolvers/lab1
author_profile: false
# toc: True
# toc_label: "On this page"
# toc_icon: "cog"
# toc_sticky: False
sidebar:
  nav: "ProbSolvers"
---
# Exercice 1: Kinship

Given the set of the following kinship knowledge:
- Alice is Bob's sister.
- Carol is Mark's mother.
- Emily is the daughter of Alice.
- Frank is the father of Carol.
- Helen is the wife of Frank.
- George is the son of Helen and the father of Sam.
- Sam is the husband of Alice
- Michael is the son of Helen.
- Bob is Carol's son.
- Mark is Emily's uncle.

1 From the previous knowledge set, give the set of symbols:  

```python



```  

2 Draw the tree-based representation of the kinship knowledge.  

```python



```  

3 Using the defined symbols, the binary predicate parent and the unary predicates male and female, create a dataset that contains the maximum of extracted knowledge.

```python



```
4 Write two different queries to compute the number of person in the dataset.

```python



```
5 Write a query to compute the number of female in the dataset.

```python



```
6 Write a query to compute the number of childless person in the dataset.

```python



```
7 Write two different queries to display all person in the dataset.

```python



```
8 Write a query to find the father and mother of George.

```python



```
9 Write a query to find the wife of Sam.

```python



```
10 Write a query to find all siblings.

```python



```
11 Write a query to find all grandmothers and their grandchildren.

```python




```
12 Write a query to find all grandfathers and their granddaughters.

```python



```
13 Write a query to find every person with at least one child.

```python



```

14 Write a query to find every person with at least two children.

```python



```
15 Write a query to find every person with at least three children.

```python



```
16 Write a query to find every person with exactly three children.

```python



```
17 Write a query to find every mother with at least one son.

```python



```
18 Write a query to find every father with exactly one daughter.

```python



```
19 Write a query to find all grandparents of Emily.

```python



```
20 Write a query to find all uncles of Emily.

```python



```

# Exercice 2: Puzzles

 For each of the following problems, write a query to solve the problem. Values should include just the digits 8, 1, 4, 7, 3 and each digit should be used at most once in the solution of each puzzle.  
 Your query should express the problem as stated, i.e., you should not first solve the problem yourself and then have the query simply return the answer.  
 
 1 The product of a 1-digit number and a 2-digit number is 284

```python



```
 2 The product of two 2-digit numbers plus a 1-digit number is 3,355.

```python



```
 3 The product of a 3-digit number and a 1-digit number minus a 1 digit number is 1,137.

```python



```
 4 The product of a 2-digit number and a 3-digit number is between 13,000 and 14,000.

```python



```
 5 When a 3-digit number is divided by a 2-digit number the result is between 4 and 6.

```python



```

# Exercice 3: SEND + MORE = MONEY

The equation "SEND + MORE = MONEY" is a classic example of a cryptarithmetic puzzle, where each letter represents a digit, and we need to find a unique digit for each letter such that the equation holds true.  
In this case, we are trying to find values for S,E,N,D,M,O,R,Y such that the sum of SEND and MORE equals MONEY.
![send+more](/assets/images/sendmoremoney.png)  
Here’s one possible solution S = 9,E = 5,N = 6,D = 7,M = 1,O = 0,R = 8,Y = 2 where the equation holds true:
 ![sendsol](/assets/images/sol.png)  
 The equation is satisfied with these values, and each letter represents a unique digit. Cryptarithmetic puzzles like this one can be solved using various techniques, including logic programming or more systematic approaches like constraint satisfaction algorithms   
  - Given the following dataset, write a query to solve this puzzle.  
 >{digit(1), digit(2), digit(3), digit(4), digit(5), digit(6), digit(7), digit(8), digit(9), digit(0)}  


 Hint: use the 8 variables S,E,N,D,M,O,R, and Y in the goal where each variable should receive a distinct digit.