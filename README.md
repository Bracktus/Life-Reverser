# Life-Reverser
A linear program to find a valid previous state in Conway's Game of Life

# Requirements
- [pulp](https://coin-or.github.io/pulp/index.html)

# Example
```
Input Board - Randomly generated
 .  .  .  .  .  .  .  .  .  .
 .  #  #  #  .  #  .  .  .  .
 .  #  #  #  .  .  .  #  .  .
 .  #  #  .  .  #  .  #  .  .
 .  #  .  .  .  .  #  #  .  .
 .  .  .  #  #  #  .  .  #  .
 .  .  #  .  .  .  #  #  #  .
 .  .  .  #  .  .  #  .  .  .
 .  #  .  .  .  .  .  #  .  .
 .  .  .  .  .  .  .  .  .  .
 
Output board - A valid previous board
 .  #  #  .  .  .  .  .  .  #
 .  .  .  .  #  .  #  .  .  .
 .  #  .  .  #  .  .  .  .  .
 .  #  #  .  .  .  #  .  #  .
 .  .  .  .  .  .  #  .  .  .
 #  .  .  .  #  #  .  .  .  .
 .  .  #  #  .  .  #  #  #  #
 #  .  #  #  .  .  #  .  .  .
 .  #  .  .  .  .  .  #  .  .
 .  .  #  .  #  .  .  .  #  .
 ```
