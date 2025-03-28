# Backtracking Patterns

#### References:
- [LeetCode Pattern - Backtracking](https://blog.algomaster.io/p/81d42ca2-600c-4252-aa33-a56462090048)
- [Problem-list Leetcode (Backtracking)](https://leetcode.com/problem-list/backtracking/)

## Introduction: 
  > [!IMPORTANT]
  > - Backtracking is a depth-first search (DFS) algorithm that builds solutions incrementally.
  > - It involves choosing a candidate, exploring further by recursively calling the function, and backtracking if the candidate leads to a dead end.
  > - This technique is often used for problems involving permutations, combinations, and subsets.

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

   - [x] [89. Gray Code](https://leetcode.com/problems/gray-code/description/)
