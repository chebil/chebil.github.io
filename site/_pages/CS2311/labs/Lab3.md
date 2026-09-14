---
title: "Lab 3: List"
layout: single
classes: wide
permalink: /DataStructure/Labs/Lab3
author_profile: false
sidebar:
  nav: "DataStructure"
---
## Defining the Abstract Data Type List
>The first step in implementing a data structure consists in defining the set of operations:

```` 
Create a new file "List.java" which contains the interface below:
````

```java
interface List<E>{
    void addFront(E x); //Add Element at the beginning of the list
    void addEnd(E x); //Add Element at the end of the list
    void addAfter(E val , E x); //Add Element after the value val in the list
    void print(); // print all the elements in the list
    boolean empty();// return true if the list is empty 
    void removeEnd();// remove the last element in the list
    void removeFront();// remove the first element in the list
    void remove(E x);// remove the element x from the list
    void removeAll();// remove all elements in the list
    boolean exist(E x);// check if the element x is in the list
    E getHead();// return the data in the head
}
```
## Linked List implementation

### Defining class Node

> A list contain a head which is a pointer (reference) to the first node. The first step we should define a **Node**

```java
class Node<E>{
    E data;
    Node<E> next;
    public Node(E data){
      this.data = data;
      next = null;
    }
    public String toString(){
      return data+ " ";
    }
  }
```
### The linkedList class

```java
class LinkedList<E> implements List<E> {
  private Node<E> head;

  public LinkedList() {
    head = null;
  }

  public void addFront(E x) {
    Node<E> node = new Node<>(x);
    node.next = head;
    head = node;
  }

  public void addEnd(E x) {
    if (head == null)
      addFront(x);
    else {
      Node<E> node = new Node<>(x);
      Node<E> p = head;
      while (p.next != null) {
        p = p.next;
      }
      p.next = node;
    }
  }

  public void addAfter(E val, E x) {
    if (empty())
      System.out.println("empty list!!!");
    else {
      Node<E> p = head;
      while (p.data != val && p.next != null) {
        p = p.next;
      }
      if (p.data != val) {
        System.out.println("The list don’t contain the value " + val);
      } else {
        Node<E> node = new Node<>(x);
        node.next = p.next;
        p.next = node;
      }
    }
  }
}
```
- Printing all element in the list

```java
public void print() {
//TODO







}
```

- Check if the list is empty or not

```java
public boolean empty() {
//TODO


}
```

- Remove the last element in the list
> 🚩 You have to check if the list is not empty!   
> 🚩 You have to check if the list contains only one element!

```java
public void removeEnd() {
//TODO












}
```
- Remove the first element in the list
> 🚩 You have to check if the list is not empty !  

```java
public void removeFront() {
//TODO





}
```

- Remove an element in the list
> 🚩 You have to check if the list is not empty !   
> 🚩 The pointer should be the predecessor of the node to remove!   

```java
public void remove(E x) {
//TODO











}
```

- Remove all elements in the list 

```java
public void removeAll() {
//TODO



}
```

- Search an element in the list 

```java
public boolean exist(E x) {
//TODO










}
```

- Return the data in the head, null if empty 

```java
public E getHead() {
//TODO










}
```
## Doubly Linked List implementation
### Defining class DNode
> A list contain a head which is a pointer (reference) to the first node and a Tail which is a pointer to the last element in the list. The first step we should define a **DNode**

```java
class DNode<E>{
  E data;
  DNode<E> next;
  DNode<E> previous;
  public DNode(E data){
    this.data = data;
    next = null;
    previous = null;
  }
  public String toString(){
    return data+ " ";
  }
}
```

### The DoublylinkedList class

```java
class DoublyLinkedList<E> implements List<E> {
//TODO








}
```

- Add an element at the front of the list
> 🚩 You have to update the tail if the list is empty! 

```java
public void addFront(E x) {
//TODO








}
```

- Add an element at the end of the list
> 🚩 You have to update the front if the list is empty! 

```java
public void addEnd(E x) {
//TODO










}
```

- Add an element after a value "val" in the list
> 🚩 You have to check the list is not empty! 
> 🚩 You have to check the value "avl" exist!
> 🚩 You have to update the previous of the successor! 
> 🚩 You have to update the next of the predecessor! 

```java
public void addAfter(E val, E x) {
//TODO
















}
```

- Printing all element in the list

```java
public void print() {
//TODO








}
```

- Check if the list is empty or not

```java
public boolean empty() {
//TODO








}
```

- Remove the last element in the list
> 🚩 You have to check if the list is not empty!   
> 🚩 You have to check if the list contains only one element!  
> 🚩 You have to update the next of the new last element to null!

```java
public void removeEnd() {
//TODO








}
```

- Remove the first element in the list
> 🚩 You have to check if the list is not empty !   
> 🚩 You have to update the tail if the list contain one element !   
> 🚩 You have to update the previous of the new head !  

```java
public void removeFront() {
//TODO











}
```

- Remove an element in the list
> 🚩 You have to check if the list is not empty !   
> 🚩 You have to update the previous of the successor! 
> 🚩 You have to update the next of the predecessor!

```java
public void remove(E x) {
//TODO














}
```

- Remove all elements in the list 

```java
public void removeAll() {
//TODO








}
```

- Search an element in the list 

```java
public boolean exist(E x) {
//TODO










}
```
- Return the data in the head, null if empty 

```java
public E getHead() {
//TODO










}
```