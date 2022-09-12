---
title: "Lab 1: The Efficiency of Algorithms"
layout: single
classes: wide
permalink: /DataStructure/Labs/Lab1
author_profile: false
sidebar:
  nav: "DataStructure"
---
## Timing algorithms
How do you determine the running time of an algorithm? 
>Java includes methods for determining the current time to a high precision.
Lets try to compute the runnig time of a method containning two nested loops For (Modify the number of iterations in each loop and see the effect on the running time)


```Java
long start_time; // The time the algorithm started
long end_time;   // The time the algorithm ended
Random rd = new Random();
start_time = System.currentTimeMillis();
int s=0;
for(int i=0; i<100000000;i++)
        s+=rd.nextInt(100)*rd.nextInt(100);
end_time = System.currentTimeMillis();
System.out.println("The algorithm took " + (end_time-start_time) + 
                " milliseconds.");
```

    The algorithm took 6750 milliseconds.


## Problems with wall-clock timing
>- Timing is highly dependent on the machine being used. 
- The same program can run much faster or much slower depending on the machine it is running on.
- The same program may run at different speeds on the same computer (Some system related tasks are running in the background).
## Does this mean that you shouldn't use wall-clock timing? 
>Certainly not. It is a valuable tool in your toolbox. 
- If you are careful about your timing (e.g., you do your best to time only what you want to time, and you run all of your timing tests on the same computer with the same load), then it can give you useful results. 
- As you develop larger programs, you may find it useful to use wall-clock timing to identify parts of your program that need to be improved.

## Computing the GCD of two numbers
### Consecutive integer checking algorithm: gcd(m,n)
>- Step 1  Assign the value of min{m,n} to t
- Step 2  Divide m by t.  If the remainder is 0, go to Step 3;        otherwise, go to Step 4
- Step 3  Divide n by t.  If the remainder is 0, return t and stop;        otherwise, go to Step 4
- Step 4  Decrease t by 1 and go to Step 2

```Java
int gcd1(int m, int n){
    if(m==0)
        return n;
    if(n==0)
        return m;
    int t = (m<n)? m:n;
    while (m%t !=0 || n%t != 0){
        t--;
    }
    return t;
}
gcd1(6,0);
```
    6

### Euclid’s algorithm: 
>- Step 1  If n = 0, return m and stop; otherwise go to Step 2
- Step 2  Divide m by n and assign the value for the remainder to r
- Step 3  Assign the value of n to m and the value of r to n.  Go to        Step 1.

```Java
int gcd2(int m, int n){
  if(m==0)
    return n;
  if(n==0)
    return m;
  int r ;
  while(m % n !=0){
    r= m % n;
    m=n;
    n=r;
  }
  return n;
}
```

### Comparing the execution time of the two algorithms


```Java
long start_time; // The time the algorithm started
long end_time;   // The time the algorithm ended
start_time = System.currentTimeMillis();
gcd1(5000,14800);
end_time = System.currentTimeMillis();
System.out.println("The algorithm 1 took " + (end_time-start_time) + 
                " milliseconds.");
start_time = System.currentTimeMillis();
gcd2(5000,14800);
end_time = System.currentTimeMillis();
System.out.println("The algorithm 2 took " + (end_time-start_time) + 
                " milliseconds.")
```
    The algorithm 1 took 41 milliseconds.
    The algorithm 2 took 39 milliseconds.
    

## Counting steps
> Instead of measuring wall-clock time, we can augment our methods to count the number of steps they do. Obviously, counting every line executed in a program is difficult. Therefore, you will typically count the number of basic operations executed.


```Java
int gcd1(int m, int n){
    int count=0;
    if(m==0)
        return n;
    if(n==0)
        return m;
    int t = (m<n)? m:n;
    while (m%t !=0 || n%t != 0){
        count++;
        t--;
    }
    System.out.println("The number of divisions is : "+ count);
    return t;
}
int gcd2(int m, int n){
    int count=0;
    if(m==0)
      return n;
    if(n==0)
      return m;
    int r ;
    while(m % n !=0){
      count++;
      r= m % n;
      m=n;
      n=r;
    }
    System.out.println("The number of divisions is : "+ count);
    return n;
  }
  gcd1(5000,14800);
  gcd2(5000,14800);
```

    The number of divisions is : 4800
    The number of divisions is : 3
    200


 
