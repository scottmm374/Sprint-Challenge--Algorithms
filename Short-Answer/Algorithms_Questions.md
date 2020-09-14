# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

create a function that takes the number of stories as a parameter

def broken_eggs(num_of_stories):

start at first floor, drop and egg and see if it breaks:
if egg != broken:
start + 1 (move up a floor)
if egg broken:
start - 1, and return current floor

      to save time divide stories in half to start:
        start =  num_of_stories / 2
        if egg dropped
        while egg dropped == broken:
              start - 1

        return start
