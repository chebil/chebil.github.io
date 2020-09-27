---
marp: true
permalink: /problemsolving/
title: "Problem Solving"
header: '![image](https://www.psau.edu.sa/themes/psau/logo.png)'
footer: College of Computer Engineering and Sciences  - September 2020
---

 # <!-- fit --> IEEEXTREME Competition Training 

## Dr. khalil Chebil 
---
# Content
- Problem Solving Challenge
- Solving Techniques
- Practice Problems
    - Maximum Subsequence Problem
---
# Problem Solving Challenge
- Hard to design algorithms that are 
    - Correct 
    - Efficient 
    - Implementable
- Need to know about
    - Design and modeling techniques
    - Resources - don't reinvent the wheel

----
# Maximum Subsequence Problem
```java
int maxSubSum(int[]a){
    int maxSum = 0; 
    for( int i = 0; i < a.length; i++ ) 
        for( int j = i; j < a.length; j++ ) 
        { 
            int thisSum = 0; 
            for( int k = i; k <= j; k++ ) 
                thisSum += a[ k ]; 
            if( thisSum > maxSum )
                maxSum = thisSum; 
        } 
    return maxSum; 
  }
````