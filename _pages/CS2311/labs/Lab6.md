---
title: "Lab 6: Binary Search Tree"
layout: single
classes: wide
permalink: /DataStructure/Labs/Lab6
author_profile: false
sidebar:
  nav: "DataStructure"
---

> Define the class Node

```java
class Node{
  int data;
  Node left;
  Node right;
  public Node(int data){
    this.data=data;
    left = null;
    right = null;
  }
  public String toString(){
    return data+" ";
  }
}
```

>Define the class BST

```java
public class Bst {
  Node root;

  public Bst() {
    root = null;
  }
}
```
## Task 1
>Complete the iterative implementation below to insert a key in a BST:

```java
public void insert(int x) {
    //ToDo
  }
```

## Task 2
>Complete the recursive implementation below to insert a key in a BST:

```java
private Node insertR(Node start, int x){
    //ToDo
}
public void insertRec(int x){
    root = insertR(root,x);
}
```

## Task 3
>Complete the implementation below to search for the minimum in a BST:

```java
private int minimum(Node root){ 
//ToDo
} 
```

## Task 4
>Complete the implementation below to delete an element in a BST:

```java
private Node delete_Recursive(Node start, int key){
    //ToDo
}
void delete(int key) { 
    root = delete_Recursive(root, key); 
}
```
