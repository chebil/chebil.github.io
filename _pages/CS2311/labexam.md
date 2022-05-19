---
title: Lab exam second Term 1443
layout: single
classes: wide
permalink: /labexam
author_profile: false
---

## Complete the missing fragments code in the following MaxHeap methods, then create a main class to test your implementation.

```java
import java.util.*;
 class MaxHeap{
  private int[] heap;
  private int heapsize;//Number of elements in the heap
  public MaxHeap(int capacity){
    heap = new int[capacity +1];
    heapsize=0;
  }
  public MaxHeap(int[] input){
    heap = new int[100];
    heapsize=input.length;
    for(int i = 1 ; i<=heapsize; i++)
      heap[i] = input[i-1];
    heapify();
  }
  private void heapify(){
    for( int i = lastParent(); i>0; i--)
      percolateDown(i);  }

  public boolean isEmpty(){
    ……………………………………………………………….…
  }
  public boolean isFull(){
    ……………………………………………………………….…
  }
  public void print(){
    ……………………………………………………………….…
    ………………………………………………………………….
    ………………………………………………………………….
  }



  //The index of the parent of a node i
  private int parent(int i){
    ……………………………………………………………….
  }
  // The index of the left child of node i
  private int leftChild(int i){
    ………………………………………………………………..
  }
  // The index of the right child of node i
  private int rightChild(int i){
    ………………………………………………………………..
  }
  // The index of the last parent
  private int lastParent(){
    ………………………………………………………………..
  }
  private void percolateUp(int i){
    int temp = heap[i];
    while(………………………………………………….){
      ………………………………………………………………
      ………………………………………………………………   
    }
    ………………………………………………………………..
  }
  public void insert(int x){
    if (isFull()){
      ……………………………………………………………….
    }else{
     …………………………………………………………………
     …………………………………………………………………
    }
  }
  private int maxChild(int i){
    return ………………………………………………………………
  }

  private void percolateDown(int i){
    int child;
    int temp = heap[i];
    while(……………………………………………){
      ………………………………………………………………
      ………………………………………………………………
    }
     …………………………………………………………………
     …………………………………………………………………
     …………………………………………………………………
     …………………………………………………………………
     …………………………………………………………………
     …………………………………………………………………
     …………………………………………………………………
     …………………………………………………………………
  }

  public void delete(){
    if(!isEmpty()){
     …………………………………………………………………
     …………………………………………………………………
    }
  }
  public int max(){
    if(!isEmpty())
     ………………………………………………………………
     ………………………………………………………………
  }
  public static int[] sort(int [] input){
     ………………………………………………………………
     ………………………………………………………………
     ………………………………………………………………
     ………………………………………………………………
     ………………………………………………………………
     ………………………………………………………………
     ………………………………………………………………
     ………………………………………………………………
  }
public class MainHeap {
  public static void main(String[] args) {
    MaxHeap m = new MaxHeap(50);
    m.insert(10);
    m.insert(12);
    m.insert(1);
    m.insert(14);
    m.insert(6);
    m.insert(5);
    m.insert(8);
    m.insert(15);
    m.insert(3);
    m.insert(9);
    m.insert(7);
    m.insert(4);
    m.insert(11);
    m.insert(13);
    m.insert(2);
    m.print();
    System.out.println("Linear Method");
    int [] input={10,12,1,14,6,5,8,15,3,9,7,4,11,13,2};
    MaxHeap m2 = new MaxHeap(input);
    m2.print();
    System.out.println(Arrays.toString(MaxHeap.sort(input)));
  }
}
```

## Use the link below to send your response:
(Male section)[notyet.com]

(Female section)[https://docs.google.com/forms/d/e/1FAIpQLSejf6TCIJ5RDND-wDSjsD8bPdQd5guFfi0l_p_wxU9lb8-_VQ/viewform]