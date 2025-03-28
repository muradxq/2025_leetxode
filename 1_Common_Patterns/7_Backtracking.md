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
  1 - **Choose**: Select a candidate from the set of possible options.
  2 - **Constraint**: Check if the choice satisfies all constraints.
  3 - **Goal**: Check if the current state is a valid solution.
  - **Recurse**: If the constraints are satisfied but the goal isn't reached, make a recursive call.
  - **Backtrack**: Remove the last chosen candidate if it leads to a dead end and try another candidate.

```python
 
```

   - [x] [89. Gray Code](https://leetcode.com/problems/gray-code/description/)
