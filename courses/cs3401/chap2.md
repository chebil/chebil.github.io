---
title: 2. Algorithm Analysis
---

# Slides
<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">

<iframe src="https://cdn.jsdelivr.net/gh/chebil/cs3401@master/ch02_analysis.pdf" frameborder="0" height="400px" width="80%" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</div>

# Implementations

## [The maximum subsequence sum algorithm](https://chebil.github.io/MaximumSubSequence)

## [Computing the exponentiation of a number](https://chebil.github.io/exponentiation)

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
