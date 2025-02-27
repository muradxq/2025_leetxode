# Sliding Window

#### References:
- [Maximum Sliding Window Cheatsheet Template!](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)


#### Template 1: Sliding Window (Shrinkable)
  The key idea is to keep the window valid at the end of each outer for-loop.
  
  ```python
  i=0
  ans=0
  for j in range(0, N):
    #[1] Update the state using nums[j] which might make the window invalid.
    #[2] Iterate while the window is invalid, keep shrinking the left edge until it's valid again,
    while(invalid()):
      #[3] Update state using nums[i]
      i+=1
    #[4] The window [i, j] is vaild here. Update the maximum window we've found thus far.
    ans = max(ans, j - i + 1);
  return ans
  ```

##### Examples:

- ##### 1493. Longest Subarray of 1's After Deleting One Element
- https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

  ```python
  class Solution(object):
      def longestSubarray(self, nums):
          ans = 0
          i = 0
          sumv =0
          for j in range(len(nums)):
              # update the state by nums[j]
              sumv += nums[j]
              # update i, while not vaild
              while ((sumv+1) < (j-i+1)): 
                  sumv -= nums[i]
                  i+=1
              # here I have a vaild window [i,j]
              ans = max(ans, (j-i))
          return ans
  ```




- (Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
     
159. Longest Substring with At Most Two Distinct Characters (Medium)
340. Longest Substring with At Most K Distinct Characters
424. Longest Repeating Character Replacement
487. Max Consecutive Ones II
713. Subarray Product Less Than K
1004. Max Consecutive Ones III
1208. Get Equal Substrings Within Budget (Medium)
1493. Longest Subarray of 1's After Deleting One Element
1695. Maximum Erasure Value
1838. Frequency of the Most Frequent Element
2009. Minimum Number of Operations to Make Array Continuous
2024. Maximize the Confusion of an Exam 

930. Binary Subarrays With Sum (Medium)
992. Subarrays with K Different Integers
1248. Count Number of Nice Subarrays (Medium)
2062. Count Vowel Substrings of a String (Easy)
2063. 
