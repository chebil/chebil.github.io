---
title: Algorithm Analysis
layout: single
classes: wide
permalink: /DataStructure/chap1
author_profile: false
# toc: True
# toc_label: "On this page"
# toc_icon: "cog"
# toc_sticky: False
sidebar:
  nav: "DataStructure"
---
<details>
<summary>Slides</summary>
<iframe height="400px" width="100%" src="https://drive.google.com/file/d/1b1DoqbC_EIIZVTqqDvAU1Hg4ePAIBNzv/preview" frameborder="0" allowfullscreen="true"></iframe>
</details>

# What is an Algorithm?
An algorithm is a step-by-step procedure for solving a problem. It is a sequence of well-defined instructions that takes some value, or set of values, as input and produces some value, or set of values, as output. It must be correct, efficient, and easy to understand.

An algorithm need data structures to store and manipulate data. A **data structure** is a way of organizing and storing data so that it can be accessed and modified efficiently. 
# Algorithm Analysis
Algorithm analysis is an important part of computational complexity theory. It is the process of determining the amount of resources (such as time and storage) necessary to execute an algorithm. It helps us compare different algorithms for the same problem and choose the best one. To analyze an algorithm, we need to consider the following factors:
- **Time complexity**: It is the amount of time an algorithm takes to complete. It is usually expressed as a function of the input size.
- **Space complexity**: It is the amount of memory an algorithm uses to complete. It is usually expressed as a function of the input size.
- **Best-case complexity**: It is the minimum amount of resources an algorithm needs to complete.
- **Worst-case complexity**: It is the maximum amount of resources an algorithm needs to complete.
- **Average-case complexity**: It is the average amount of resources an algorithm needs to complete.

# Measuring the Efficiency of Algorithms
The efficiency of an algorithm can be measured in two ways:
- **Empirical analysis**: It is the process of measuring the efficiency of an algorithm by running it on a computer and measuring the time and space it takes to complete. 
- **Analytical analysis**: It is the process of measuring the efficiency of an algorithm by analyzing the algorithm's code and determining the time and space complexity.

## Example: Computing the Greatest Common Divisor
The greatest common divisor (gcd) of two integers is the largest integer that divides each of them without remainder.

There is many algorithms to compute the gcd of two integers:
- By consecutive integer checking: 
> The general idea is to start from the smaller of the two numbers and check whether it divides both m and n. If it does, we return this number as the gcd. Otherwise, we check the next smaller number. We continue checking until we find a number that divides both m and n or until we reach 1.
```java
int gcd(int m, int n) {
    int t = Math.min(m, n);
    while (m % t != 0 || n % t != 0) {
        t--;
    }
    return t;
}
```

- Using Euclid's algorithm
> The key to Euclid's algorithm is the observation that if rem is the remainder when a is divided by b, then the common divisors of a and b are precisely the same as the common divisors of b and rem. Moreover, gcd(a, b) = gcd(b, rem) where rem = a % b.
```java
int gcd(int m, int n) {
    while (n != 0) {
        int rem = m % n;
        m = n;
        n = rem;
    }
    return m;
}
```

Lets consider the case where m =14800 and n = 5000.

GCD(14800, 5000) = 200 

Lets see how many iterations each algorithm takes to compute the gcd.
- Consecutive integer checking: 4800 iterations
- Euclid's algorithm: 3 iterations

## Example: Searching
Searching is the process of looking for a particular value in an array of values. If the value is found, the search is successful; otherwise, it is unsuccessful. There are many algorithms to search for a value in an array. Two of the most common search algorithms are sequential search and binary search. 
### Sequential Search
Sequential search is the simplest search algorithm. It works by examining each element in the array in order until a match is found or the whole array has been searched. 
```java
int sequentialSearch(int[] arr, int x) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}
```
To search for a value in an array of $$n$$ elements, the sequential search algorithm may need to examine all $$n$$ elements if the value being searched is not in the array (called worst-case which is $$O(n)$$). Or it may need to examine only one element if the value being searched is the first element in the array (called best-case which is $$O(1)$$). The average-case is the average number of elements that need to be examined to find the value being searched. The average-case is $$(n+1)/2$$.
### Binary Search
Binary search works on sorted arrays. It starts by examining the middle element of the array. If the middle element is equal to the value being searched, the search is successful. If the value being searched is less than the middle element, the search continues in the lower half of the array. If the value being searched is greater than the middle element, the search continues in the upper half of the array. 
```java
int binarySearch(int[] arr, int x) {
    int low = 0;
    int high = arr.length - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] < x) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```
To search for a value in an array of $$n$$ elements, the binary search algorithm may need to examine $$\log_2 n$$ elements if the value being searched is not in the array (called worst-case which is $$O(\log n)$$). Or it may need to examine only one element if the value being searched is the middle element in the array (called best-case which is $$O(1)$$). The average-case is the average number of elements that need to be examined to find the value being searched. The average-case is $$\log_2 n$$.
