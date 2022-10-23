---
title: "Lab 4: Queue"
layout: single
classes: wide
permalink: /DataStructure/Labs/Lab5
author_profile: false
sidebar:
  nav: "DataStructure"
---
## How do we implement a circular array
>Create an array of size 10 and fill it with numbers from 1 to 10
```java
//ToDo
```
> insert values in the array T from 1 to 3214 in a circular way beginning from index 0.
```java
//ToDo
```
> what is the content of the array T ?
```java
//ToDo
```

## Queue based Array implementation
>The abstract data type Queue


```java
//ToDo
```

>The Queue class
```java
import java.lang.reflect.Array;
public class Queue<E> implements QueueADT<E>{
  private int size, front, rear;
  private E data[];
  public Queue(Class<E> element,int size){
    this.size=size+1;
    data = (E[])Array.newInstance(element,this.size);
    front = 1;
    rear= 0;
  }
  public boolean isEmpty(){
    //ToDo
  }
  private boolean full(){
    //ToDo
  }
  public void enqueue(E x){
    //ToDo
  }
  public E dequeue(){
    //ToDo
  }
}
```

>Testing 

```java 
Queue<Integer> Q = new Queue<>(Integer.class,9);
System.out.println(Q.isEmpty());
for(int i=1; i<9; i++){
  Q.enqueue(i);
  if(i%3==0)
    Q.dequeue();
}
while(!Q.isEmpty()){
  System.out.println(Q.dequeue());
}
``` 

The output should be: 

``` java
//ToDo
```

## Reverse a queue

>How to reverse the content of a queue using a stack


```java 
Queue<Integer> Q = new Queue<>(Integer.class,9);
Stack<Integer> S = new Stack<>();
for(int i=1; i<=9; i++){
  Q.enqueue(i);
}
//Reversing the queue
//ToDo
```
