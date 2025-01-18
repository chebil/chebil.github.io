---
title: Recursion
layout: single
classes: wide
permalink: /DataStructure/chap2
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
<iframe height="400px" width="100%" src="https://drive.google.com/file/d/15gJnvedgc2QgS4mRMyRbAl6yh2mpOJrp/preview" frameborder="0" allowfullscreen="true"></iframe>
</details>

## Some Recursion exercises

### Exercise 1: Searching for an element in an array

Write a recursive function that searches for an element in an array. The function should return the index of the element if it is found, and -1 otherwise.

Solution:
```java
int search(int[] arr, int x) {
    return search(arr, 0, x);
}
int search(int[] arr, int i, int x) {
    if (i == arr.length) {
        return -1;
    }
    if (arr[i] == x) {
        return i;
    }
    return search(arr, i + 1, x);
}
```
### Exercise 2: Compute the exponentiation of a number

Write a recursive function that computes the exponentiation of a number. The function should take two integers, $$x$$ and $$n$$, and return $$x^n$$.

Solution:
```java
int power(int x, int n) {
    if (n == 0) {
        return 1;
    }
    return x * power(x, n - 1);
}
```
### Exercise 3: Computing the number of occurrences of a character in a string

Write a recursive function that computes the number of occurrences of a character in a string. The function should take a string and a character, and return the number of occurrences of the character in the string.

Solution:
```java
int count(String s, char c) {
    return count(s, c, 0);
}
int count(String s, char c, int i) {
    if (i == s.length()) {
        return 0;
    }
    return (s.charAt(i) == c ? 1 : 0) + count(s, c, i + 1);
}
```
