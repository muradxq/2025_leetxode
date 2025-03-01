# Modified Binary Search

#### References:
- [Powerful Ultimate Binary Search Template. Solved many problems!](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)

### Introduction
Binary Search is quite easy to understand conceptually. Basically, it splits the search space into two halves and only keep the half that probably has the search target and throw away the other half that would not possibly have the answer. 

In this manner, we reduce the search space to half the size at every step, until we find the target. Binary Search helps us reduce the search time from linear `O(n)` to logarithmic `O(log n)`. **But when it comes to implementation, it's rather difficult to write a bug-free code in just a few minutes**. 

Some of the most common problems include:
- When to exit the loop? Should we use `left < right` or `left <= right` as the while loop condition?
- How to initialize the boundary variable `left` and `right`?
- How to update the boundary?
- How to choose the appropriate combination from `left = mid`, `left = mid + 1` and `right = mid`, `right = mid - 1`?

A rather common misunderstanding of binary search is that people often think this technique could only be used in simple scenario like "Given a sorted array, find a specific value in it". As a matter of fact, it can be applied to much more complicated situations.

### Template: Most Generalized Binary Search

Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascending order. For most tasks, we can transform the requirement into the following generalized form:

The following code is the most generalized binary search template:

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

For most of the binary search problems, we only need to modify three parts in this template, and never need to worry about corner cases and bugs in code any more:

- Correctly initialize the boundary variables `left` and `right` to specify search space. Only one rule: set up the boundary to include all possible elements.
- Decide return value. Is it return `left` or return `left - 1`? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function.
- Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

### Easy Problems: 
- [x] [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/)
- [x] [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/description/)
- [x] [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)

### More advanced Problems: 

The above problems are quite easy to solve, because they already give us the array to be searched. We'd know that we should use binary search to solve them at first glance. **However, more often are the situations where the search space and search target are not so readily available.** Sometimes we won't even realize that the problem should be solved with binary search -- we might just turn to dynamic programming or DFS and get stuck for a very long time.

As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.

- [x] [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/)
- [ ] [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)
- [ ] [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/)

- [ ] [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/)
- [ ] [1201. Ugly Number III](https://leetcode.com/problems/ugly-number-iii/description/)
- [ ] [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/)
- [ ] [1201. Ugly Number III](https://leetcode.com/problems/ugly-number-iii/description/)
- [ ] [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/description/)
- [ ] [668. Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/)


---------------------------------

- [ ] [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/)



  ```python
    # Can w use binary search?
    # Is the search space for the answer has a specific range?
    # left = max(weights) the minimum capacity should be max(weight) otheriwse we will not be able to ship the item.
    # right = sum(weights) because if the capacity is sum(weights), we can ship them all in one day.
    # The monotonic condition; If capacity = x fit in n dayas. that means any capacity > x will also fit.
    # The goal of the binary seach is to find the minimum fesiable capacity.
  
    def isfesiable(capacity):
      # is capacity is enough to ship in n days.
      total = 0
      nDays = 1
  
    for w in weights:
      total += w
      if total > capacity:
        nDays+=1
        total = w
    if nDays > days:
      return False
    else:
      return True                    
  
    l = max(weights)
    r = sum(weights)
    while l < r:
      mid = l + (r - l) // 2
      if (isfesiable(mid)):
        r = mid
      else:
        l = mid +1
    return l
  ```
