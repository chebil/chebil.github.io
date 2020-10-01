---
title: "Car Fueling Problem"
categories:
  - Problem Solving
tags:
  - Algorithms
---
# Problem Introduction
You are going to travel to another city that is located 𝑑 miles away from your home city. Your car can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances $stop_1, stop_2,..., stop_𝑛$ from your home city. What is the minimum number of refills needed?
# Problem Description
## Input Format 
The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line specifies an integer 𝑛. Finally, the last line contains integers $stop_1, stop_2,..., stop_𝑛$.
## Output Format 
Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles on a full tank, and there are gas stations at distances $stop_1, stop_2,..., stop_𝑛$ along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.
## Constraints 
1 ≤ 𝑑 ≤ 105. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < ... < stop𝑛 < 𝑑.
### Sample 1
Input:
>950
<br>400
<br>4
<br>200 375 550 750

Output:
>2

The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices
to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill
one would only be able to travel at most 800 miles.

### Sample 2
Input:
>10
<br>3
<br>4
<br>1 2 5 9

Output:
>-1

One cannot reach the gas station at point 9 as the previous gas station is too far away.

### Sample 3
Input:
>200
<br>250
<br>2
<br>100
<br>150

Output:
>0

There is no need to refill the tank as the car starts with a full tank and can travel for 250 miles
whereas the distance to the destination point is 200 miles.