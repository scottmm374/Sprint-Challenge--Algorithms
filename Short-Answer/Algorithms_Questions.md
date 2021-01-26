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

linear approach Time Complexity O(n)- worst case every floor is visited once.

def broken_eggs(num_of_stories):

start at first floor
drop egg
if egg != broken:
start + 1 (move up a floor)
if egg broken:
start - 1  
 return current floor

<!-- binary approach:  NOT FINISHED... BROKEN EGGS ARE CONFUSING.

bottom_floor = 0
top_floor = num_of_stories

def broken_eggs(num_of_stories, top_floor, bottom_floor, unbroken_egg):

  if num_of_stories == 0:
      return -1

  middle_floor = (top_floor + bottom_floor) // 2

    start at middle_floor
      drop unbroken_egg
      if egg not broken:
        top_floor == middle_floor
        return broken_eggs(num_of_stories, top_floor, bottome_floor, eggs)

      if egg Broken:
        bottom_floor == middle_floor
        return broken_eggs(num_of_stories, top_floor, bottome_floor, eggs) -->
