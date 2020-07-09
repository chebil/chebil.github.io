---
layout: archive
permalink: /optimization/LinearProgramming
title: "Linear Programming"
author_profile: true
---
- [I. Introduction](#i-introduction)
- [II. Modeling a problem](#ii-modeling-a-problem)
  - [II.1 The telephone production Problem](#ii1-the-telephone-production-problem)
    - [Using DOcplex to formulate the mathematical model in Python](#using-docplex-to-formulate-the-mathematical-model-in-python)
    - [Solving Graphically the model](#solving-graphically-the-model)
  - [II.2 The Diet Problem](#ii2-the-diet-problem)

# I. Introduction

<p>Linear programming is a mathematical method that is used to determine the best possible outcome or solution from a given set of parameters or list of requirements, which are represented in the form of linear relationships. It is most often used in computer modeling or simulation in order to find the best solution in allocating finite resources such as money, energy, manpower, machine resources, time, space and many other variables. In most cases, the "best outcome" needed from linear programming is maximum profit or lowest cost.</p>

The basic components of linear programming are as follows:

 - Decision variables : These are the quantities to be determined.

 - Objective function : This represents how each decision variable would affect the cost, or, simply, the value that needs to be optimized.

 - Constraints : These represent how each decision variable would use limited amounts of resources.

 - Data : These quantify the relationships between the objective function and the constraints.


 <h6>from: https://www.techopedia.com/definition/20403/linear-programming-lp</h6>
 

 # II. Modeling a problem
 

## II.1 The telephone production Problem
 
 A telephone company produces and sells two kinds of telephones, namely desk phones and cellular phones. 

Each type of phone is assembled and painted by the company. The objective is to maximize profit, and the company has to produce at least 100 of each type of phone.

There are limits in terms of the company’s production capacity, and the company has to calculate the optimal number of each type of phone to produce, while not exceeding the capacity of the plant.
$
maximize:\\
\ \ 12\ desk + 20\ cell\\
subject\ to: \\
\ \   desk >= 100 \\
\ \   cell >= 100 \\
\ \   0.2\ desk + 0.4\ cell <= 400 \\
\ \   0.5\ desk + 0.4\ cell <= 490 \\
$

### Using DOcplex to formulate the mathematical model in Python



```python
import docplex.mp
from docplex.mp.model import Model
m= Model(name='Telephone Production Problem')
x1=m.continuous_var(name='desk')
x2=m.continuous_var(name='cell')
m.maximize(12*x1+20*x2)
m.add_constraint(x1  >= 100)
m.add_constraint(x2  >= 100)
m.add_constraint(0.2*x1 + 0.4*x2 <= 400)
m.add_constraint(0.5*x1 + 0.4*x2 <= 490)
m.print_information()
m.solve()
m.print_solution()
```

    Model: Telephone Production Problem
     - number of variables: 2
       - binary=0, integer=0, continuous=2
     - number of constraints: 4
       - linear=4
     - parameters: defaults
     - problem type is: LP
    objective: 20600.000
      desk=300.000
      cell=850.000
    

### Solving Graphically the model


```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# plot the lines defining the constraints
x = np.linspace(100, 1000)
# y >= 100
y1 = (x*0) + 100
# 0.4y <= 400 - 0.2x
y2 = (400-0.2*x)/0.4
# 0.4y <= 490 -0.5x 
y4 = (490 - 0.5 * x)/0.4
plt.plot(x,y1, label=r'$cell>=100$')
plt.plot(y1, x, label=r'$desk>=100$')
plt.plot(x, y2, label=r'$0.2*desk + 0.4*cell <= 400$')
plt.plot(x, y4, label=r'$0.5*desk + 0.4*cell <= 490$')
plt.xlim(0,1000)
plt.ylim(0,1000)
plt.xlabel(r'$desk$')
plt.ylabel(r'$cell$')
# Fill feasible region
y6=np.minimum(y2,y4)
plt.fill_between(x, y1, y6, where=y1<y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
```




    <matplotlib.legend.Legend at 0x171fa19bdc8>




![svg](/images/output_4_1.svg)


## II.2 The Diet Problem
 
 <p>Assume that there are two products, cereal and milk, for breakfast and assume that a person must consume at least 60 units of iron and at least 70 units of protein to stay alive. Assume that one unit of cereal costs $20 and contains 30 units of iron and 5 units of protein and one unit of milk costs $10 and contains 17 units of iron and 9 units of protein. The goal is to nd the cheapest diet which will satisfy the minimum daily requirement.</p>

 Let x1 represents the number of units of cereal that the person consumes a day and x2 represents the number of units of milk consumed.

For the diet to meet the minimum requirements, we must have 
 - Iron Requirement : 30x1 + 17x2 >= 60;
 - Protein Requirement : 5x1 + 9x2 >= 70; 
 - where x1 and x2 >= 0;

The cost of the diet is: 20x1 + 10x2

Hence, the diet problem is:

| minimize | $20\ x_1\ +\ 10\ x_2$ |
| --- | --- |
| subject to | |
| | $30\ x_1\  + \ 17\ x_2\  >=\  60$ |
| | $5\ x_1\  +\ 9\ x_2\  >=\  70$ |
| | $x_1,\  x_2\ >=\  0$ |




```python
import docplex.mp
from docplex.mp.model import Model
m= Model(name='Diet Problem')
x1=m.continuous_var(name='X1')
x2=m.continuous_var(name='X2')
m.minimize(20*x1+10*x2)
m.add_constraint(30*x1 + 17*x2 >= 60)
m.add_constraint(5*x1 + 9*x2 >= 70)
m.print_information()
m.solve()
m.print_solution()
```

    Model: Diet Problem
     - number of variables: 2
       - binary=0, integer=0, continuous=2
     - number of constraints: 2
       - linear=2
     - parameters: defaults
     - problem type is: LP
    objective: 77.778
      X2=7.778