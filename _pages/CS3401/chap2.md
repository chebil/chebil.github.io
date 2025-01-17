---
title: Algorithm Analysis
layout: single
classes: wide
permalink: /AlgDesign/chap2
author_profile: false
# toc: True
# toc_label: "On this page"
# toc_icon: "cog"
# toc_sticky: False
sidebar:
  nav: "AlgDesign"
---
# Slides
<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">

<iframe src="https://drive.google.com/file/d/177ifLduodyQQXNE8DKNvcugImpUu8NdD/preview" frameborder="0" height="400px" width="80%" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>

# Implementations

## [The maximum subsequence sum algorithm](/MaximumSubSequence)

## [Computing the exponentiation of a number](/exponentiation)

## Recursive Factorial Algorithm
```java
public static long factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
```
## Counting the number of binary digits Recursive Algorithm
```java
public static int countBits(int n) {
    if (n == 0) {
        return 0;
    } else {
        return 1 + countBits(n / 2);
    }
}
```
## The Tower of Hanoi Recursive Algorithm
```java
public static void hanoi(int n, char from, char to, char aux) {
    if (n == 1) {
        System.out.println("Move disk 1 from " + from + " to " + to);
    } else {
        hanoi(n - 1, from, aux, to);
        System.out.println("Move disk " + n + " from " + from + " to " + to);
        hanoi(n - 1, aux, to, from);
    }
}
```

