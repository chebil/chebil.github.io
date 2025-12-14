---
layout: posts
classes: wide
title:  "Exponentiation"
author_profile: true
tags:
  - Algorithms
  - Complexity Analysis
  - Recursion
---

Computing the exponentiation of a number is a classic problem in computer science. The problem is to find the value of a number raised to the power of another number. The algorithm has a number of different implementations with different time complexities. The following are some of the most common implementations of the algorithm and an analysis of their time complexity.



## Table of Contents
1. [Linear implementation](#linear-implementation)
2. [Logarithmic implementation](#logarithmic-implementation)

## Linear implementation
There is many ways to implement the exponentiation algorithm. The most common way is to use a loop to multiply the base number by itself the number of times specified by the exponent. This implementation has a time complexity of $$O(n)$$ where $$n$$ is the exponent.

```java
public static long power(int x, int n) {
    long result = 1;
    for (int i = 0; i < n; i++) {
        result *= x;
    }
    return result;
}
```
Another way to implement the exponentiation algorithm is to use recursion according to the following formula: $$ x^n = x \times x^{n-1}$$. This implementation has a time complexity of $$O(n)$$ where $$n$$ is the exponent.

```java
public static long power(int x, int n) {
    if (n == 0) {
        return 1;
    } else {
        return x * power(x, n - 1);
    }
}
``` 
We can also follow the following formula: $$ x^n = x^{n/2} \times x^{n/2}$$ if $$n$$ is even and $$ x^n = x \times x^{n/2} \times x^{n/2}$$ if $$n$$ is odd. This implementation has a time complexity of $$O(n)$$ where $$n$$ is the exponent because it has to calculate the power of $$x$$ for each half of the exponent.

```java
public static long power(int x, int n) {
    if (n == 0) {
        return 1;
    } else {
        if (n % 2 == 0) {
            return  power(x, n / 2) * power(x, n / 2);
        } else {
            return x * power(x, n / 2) * power(x, n / 2);
        }
    }
}
``` 
## Logarithmic implementation
The recursive implementation can be optimized by using the following formula: $$ x^n = (x^{n/2})^2$$ if $$n$$ is even and $$ x^n = x \times (x^{n/2})^2$$ if $$n$$ is odd. This implementation has a time complexity of $$O(logn)$$ where $$n$$ is the exponent.

```java
public static long power(int x, int n) {
    if (n == 0) {
        return 1;
    } else {
        long temp = power(x, n / 2);
        if (n % 2 == 0) {
            return temp * temp;
        } else {
            return x * temp * temp;
        }
    }
}
```
Or we can write the above implementation in a more concise way as follows:

```java
public static long power(int x, int n) {
    if (n == 0) {
        return 1;
    } else {
        return n % 2 == 0 ? power(x*x, n / 2): x * power(x*x, n / 2);
    }
}
```
