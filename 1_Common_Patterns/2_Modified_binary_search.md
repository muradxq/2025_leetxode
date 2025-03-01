# Modified Binary Search

#### References:
- [Powerful Ultimate Binary Search Template. Solved many problems!](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)

Binary Search is quite easy to understand conceptually. Basically, it splits the search space into two halves and only keep the half that probably has the search target and throw away the other half that would not possibly have the answer. 
In this manner, we reduce the search space to half the size at every step, until we find the target. Binary Search helps us reduce the search time from linear O(n) to logarithmic O(log n). But when it comes to implementation, it's rather difficult to write a bug-free code in just a few minutes. Some of the most common problems include:

### Template: Most Generalized Binary Search

  ```python
  def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
  ```
#### Questions that follow this patterns:
- [x]
