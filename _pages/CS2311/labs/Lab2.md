---
title: "Lab 2: Recursion"
layout: single
classes: wide
permalink: /DataStructure/Labs/Lab2
author_profile: false
sidebar:
  nav: "DataStructure"
---
## Task 1

>Complete the implementation below to print an array recursively

```java
void print(int[] A, int start){
    //toDo
}
```
## Task 2

>Complete the implementation below to print an array in reverse order recursively
example: int A[] ={1,2,3,4};
print_Reverse(A,0) ==> 4 3 2 1

```java
void print_Reverse(int[] A, int start){
    //toDo
}
```

## Task 3

>Implement a recursive method that convert a decimal number to a base b

```java
void convert (int n, int b){
   //toDo
}
```
## Task 4

>If a string reversed value is equal to the original string then this string is PALINDROME, implement a recursive method to check if a string given as parameter is palindrome or not:

```java
boolean palindrome(String s)
{   
    //toDo
}
```
## Task 5

>Implement a recursive method that reverse a string:

```java
String reverse(String s)
{   
    //toDo
}
```
## Task 6

>We have n reversible tokens, aligned. Each token has one side marked 1 and one side marked 0. Initially only the 0 sides of the n tokens are visible. The goal of the game is to turn over the different tokens so that the only visible faces are the 1s.
- No. Jeton 123………….n
- Initial configuration 000………….0
- Final configuration   111………….1


>Flipping tokens obeys to the following rules:
1. You can always flip the first token (the leftmost one)
2. The I<sup>th</sup> token can be turned over if the (i-2) first tokens are in the 0 side and the (I-1)<sup>th</sup> token is in side 1.

```java
// print all tokens state
void print(int[] tokens){
    for (int i=1; i<tokens.length; i++)
       System.out.print("| "+tokens[i]);
    System.out.println("|");
}
void ReverseTo_1(int[] tokens, int k){
    //toDo
}
void ReverseTo_0(int[] tokens, int k){
    //toDo
}
//Testing the method
public static void main(String[] args){
    int n=4;
    int[] tokens= new int[n+1];
    for(int i=1;i<=n;i++)
    tokens[i]=0;
    print(tokens);
    ReverseTo_1(tokens,n);  
}

//the output should be 
| 0| 0| 0| 0|
| 1| 0| 0| 0|
| 1| 1| 0| 0|
| 0| 1| 0| 0|
| 0| 1| 1| 0|
| 1| 1| 1| 0|
| 1| 1| 1| 0|
| 1| 0| 1| 0|
| 0| 0| 1| 0|
| 0| 0| 1| 1|
| 1| 0| 1| 1|
| 1| 1| 1| 1|
```