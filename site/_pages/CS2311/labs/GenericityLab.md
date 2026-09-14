---
title: "Generic class in java"
layout: single
classes: wide
permalink: /DataStructure/Labs/Generic
author_profile: false
sidebar:
  nav: "DataStructure"
---
## What is a generic class?
A generic class is a class that can operate on a specific data type specified by the user. In this way, a generic class allows you to create a class that can be used with any data type, rather than having to create a separate class for each data type.

## Using the Object class

Let for example implement a simple Box class as follows:

```Java
public class Box {
    private Object object;
    public void set(Object object) { this.object = object; }
    public Object get() { return object; }
}
```
As you can see, the Box class uses the Object class to store the object. This means that you can store any type of object in the Box class. However, when you retrieve the object from the Box class, you will need to cast it to the appropriate type. For example:

```Java
Box box = new Box();
b.set(5);
System.out.println(b.get());
b.set("hello");
System.out.println(b.get());
String s = (String) b.get(); // Need to cast to String
```
The user of the Box class must remember to cast the object to the appropriate type when retrieving it. This can be error-prone and can lead to runtime errors if the user forgets to cast the object to the appropriate type or casts it to the wrong type.

## Using a generic class

To avoid the need for casting, you can use a generic class. A generic class allows you to specify the type of object that the class will operate on. For example, you can create a generic Box class as follows:

```Java
public class Box<T> {
    private T object;
    public void set(T object) { this.object = object; }
    public T get() { return object; }
}
```
In this example, the Box class is a generic class that can operate on any type T. When you create an instance of the Box class, you specify the type of object that the Box class will operate on. For example:

```Java
Box<Integer> intBox = new Box<>();
intBox.set(5);
System.out.println(intBox.get());
Box<String> stringBox = new Box<>();
stringBox.set("hello");
System.out.println(stringBox.get());
String s = stringBox.get(); // No need to cast
```
>**<span style="color:red">The type T refers to any non-primitive data type: classes, interfaces, arrays, etc. You cannot use primitive data types like int, char, etc. with generics.</span>**

## Using multiple type parameters

You can also use multiple type parameters in a generic class. For example, you can create a Pair class that stores a pair of objects of different types:

```Java
public class Pair<T, U> {
    private T key;
    private U value;
    public Pair(T key, U value) {
        this.key = key;
        this.value = value;
    }
    public T getKey() { return key; }
    public U getValue() { return value; }
}
```
In this example, the Pair class has two type parameters T and U. When you create an instance of the Pair class, you specify the types of the key and value objects. For example:

```Java
Pair<String, Integer> pair = new Pair<>("one", 1);
System.out.println(pair.getKey() + ": " + pair.getValue());
Pair<String, String> pair2 = new Pair<>("hello", "world");
```
You can also substitute a type parameter with a parameterized type (List, ArrayList etc.). For example:

```Java
Pair<String, List<Integer>> pair = new Pair<>("one", new ArrayList<>());
pair.getValue().add(1);
pair.getValue().add(2);
```
In this example, the Pair class has a type parameter U that is a List of Integers. This allows you to store a list of integers as the value in the Pair class.

## Using bounded type parameters

You can also use bounded type parameters in a generic class. Bounded type parameters allow you to restrict the types that can be used with the generic class. For example, you can create a Box class that only accepts objects that implement the Comparable interface:

```Java
public class Box<T extends Comparable<T>> {
    private T object;
    public void set(T object) { this.object = object; }
    public T get() { return object; }
}
```
In this example, the Box class has a bounded type parameter T that specifies that T must implement the Comparable interface. This means that you can only use the Box class with objects that implement the Comparable interface. For example:

```Java
Box<Integer> intBox = new Box<>();
intBox.set(5);
Box<String> stringBox = new Box<>(); // Compile-time error
```
In this example, you can create a Box object with an Integer type because Integer implements the Comparable interface. However, you cannot create a Box object with a String type because String does not implement the Comparable interface.

## Using wildcards

You can also use wildcards in a generic class to specify an unknown type. Wildcards are useful when you want to operate on a generic class without knowing the exact type of the objects. For example, you can create a Box class that accepts any type of object:

```Java
public class Box<T> {
    private T object;
    public void set(T object) { this.object = object; }
    public T get() { return object; }
    public void print(Box<?> box) {
        System.out.println(box.get());
    }
}
```
In this example, the Box class has a print method that accepts a Box object with an unknown type. This allows you to print the object without knowing the exact type of the object. For example:

```Java
Box<Integer> intBox = new Box<>();
intBox.set(5);
Box<String> stringBox = new Box<>();
stringBox.set("hello");
intBox.print(intBox);
stringBox.print(stringBox);
```
In this example, the print method accepts a Box object with an unknown type using the wildcard ?. This allows you to print the object without knowing the exact type of the object.

