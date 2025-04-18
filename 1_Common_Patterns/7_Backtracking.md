# Backtracking Patterns

#### References:
- [LeetCode Pattern - Backtracking](https://blog.algomaster.io/p/81d42ca2-600c-4252-aa33-a56462090048)
- [Problem-list Leetcode (Backtracking)](https://leetcode.com/problem-list/backtracking/)
- [(6.0) Introduction to Backtracking](https://www.youtube.com/watch?v=DKCbsiDBN6c)
- [(6.1) N-Queens Problem](https://www.youtube.com/watch?v=xFv_Hl4B83A)
- [(6.2) Sum Of Subsets Problem](https://www.youtube.com/watch?v=kyLxTdsT8ws)
- [(6.3) Graph Coloring Problem](https://www.youtube.com/watch?v=052VkKhIaQ4)
- [(6.4) Hamiltonian Cycle](https://www.youtube.com/watch?v=dQr4wZCiJJ4)

## Introduction: 
  > [!IMPORTANT]
  > - Backtracking is a depth-first search (DFS) algorithm that builds solutions incrementally.
  > - It involves choosing a candidate, exploring further by recursively calling the function, and backtracking if the candidate leads to a dead end.
  > - This technique is often used for problems involving permutations, combinations, and subsets.

  > [!IMPORTANT]  
  > - Brute Force approach finds all the possible solutions and selects desired solution per given the constraints.
  > - Dynamic Programming also uses Brute Force approach to find the OPTIMUM solution, either maximum or minimum.
  > - Solutions to the Backtracking problems can be represented as State-Space Tree (edge is the candidate).
  > - The constrained applied to find the solution is called Bounding function.
  > - Backtracking follows DFS.
  > - Branch and Bound follows BFS.

### Basic Operations in Backtracking:
- The backtracking algorithm typically follows this pattern:
  - **Choose**: Select a candidate from the set of possible options.
  - **Constraint**: Check if the choice satisfies all constraints.
  - **Goal**: Check if the current state is a valid solution.
  - **Recurse**: If the constraints are satisfied but the goal isn't reached, make a recursive call.
  - **Backtrack**: Remove the last chosen candidate if it leads to a dead end and try another candidate.

### Implementing Backtracking
```python
def backtrack(candidate):
  if find_solution(candidate):
    output(candidate)
    return
  for next_candidate in list_of_candidates:
    if is_valid(next_candidate):
      # try this partial candidate solution
      place(next_candidate)
      # given the candidate explore further
      backtrack(next_candidate)
      # backtrack
      remove(next_candidate)
```

### Examples: 
#### [1. Subsets](https://leetcode.com/problems/subsets/description/?envType=problem-list-v2&envId=backtracking):
- Given an integer array nums of unique elements, return all possible subsets.
```python
def subsets(self, nums):
  res = []
  def backtrack(start, curr):
    res.append(curr[:])
    for i in range(start, len(nums)):
      curr.append(nums[i])
      backtrack(i+1, curr)
      curr.pop()

  backtrack(0, [])
  return res
``` 
#### [2. Permutations](https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=backtracking):
- Given an array nums of distinct integers, return all the possible permutations. 
```python
def Permutate(self, nums):
  res = []
  def backtrack(start):
    if start == len(nums):
      res.append(nums[:])
    for i in range(start, len(nums)):
      nums[start], nums[i] = nums[i], nums[start]
      backtrack(start+1)
      nums[start], nums[i] = nums[i], nums[start]
  backtrack(0)
  return res
```
#### [3. Combination Sum](https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=backtracking):
-  Given an array of distinct integers candidates and a target integer target, return all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may be used an unlimited number of times.
```python
def combination_sum(candidate, target):
  res = []
  def backtrack(start, path, remaining):
    if remaining == 0:
      res.append(path[:])
      return
    for i in range(start, len(candidate)):
      if candidate[i] > remaining:
          continue
      path.append(candidate[i])
      backtrack(start+1, path, remaining)
      path.pop()
  backtrack(0, [])
  return res
``` 
