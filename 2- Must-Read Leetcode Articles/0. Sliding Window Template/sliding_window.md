# Sliding Window

#### References:
- [Maximum Sliding Window Cheatsheet Template!](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)


#### Template 1: Sliding Window (Shrinkable)

Essentially, we want tokeep the window validat the end of each outer for-loop.

```
i=0
ans=0
for j in range(0, N):
  # CODE: use A[j] to update state which might make the window invalid
  # When invalid, keep shrinking the left edge until it's valid again
  for (; invalid(); ++i):
    # CODE: update state using A[i]
  # The window [i, j] is the maximum window we've found thus far
  ans = max(ans, j - i + 1);
return ans
```
