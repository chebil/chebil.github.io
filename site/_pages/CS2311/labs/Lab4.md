---
title: "Lab 4: Stack"
layout: single
classes: wide
permalink: /DataStructure/Labs/Lab4
author_profile: false
sidebar:
  nav: "DataStructure"
---
## Defining the Abstract Data Type Stack
>The first step in implementing a data structure consists in defining the set of operations:
Create a new file "StackADT.java" which contains the interface below:


```java
interface StackADT<E>{
  void push(E x);
  E pop();
  E top();
  boolean isEmpty();
}
```
## Stack based LinkedList implementation
1. Go to the List interface and add a method to get the value of the head
> You should also add the implementation of the method the the LinkedList and DoublyLinkedList classes. 
```java
public E getHead(){
    if(! empty())
        return head.data;
    return null;
}
```
2. The Stack class
```java
class Stack<E> implements StackADT<E> {
  //ToDo
    ...
}
```

## Implementing the checkBalance method
> Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.
```java
static boolean checkBalance(String expr) {
    //ToDo
    ...
  }
```