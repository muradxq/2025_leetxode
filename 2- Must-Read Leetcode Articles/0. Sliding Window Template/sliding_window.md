# Sliding Window

#### References:
- [Maximum Sliding Window Cheatsheet Template!](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)


#### Template: Sliding Window (Shrinkable)
  The key idea is to keep the window valid at the end of each outer for-loop.
  > [!IMPORTANT]
  > #### How to define the state:
  > - which data structure?
  > - how to update it with nums[j]?
  > - how to update it with nums[i]?
  > - what is a vaild state? 

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


#### Examples:

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



#### Questions that follow this patterns:
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
- [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)
- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/)
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)
- [487. Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/description/)
- [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/description/)
- [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/description/)
- [1208. Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/description/)
- [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/)
- [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/description/)
- [1838. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/)
- [2009. Minimum Number of Operations to Make Array Continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/)
- [2024. Maximize the Confusion of an Exam](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/)

#### The following problems are also solvable using the shrinkable template with the [At Most to Equal trick](https://leetcode.com/problems/count-vowel-substrings-of-a-string/solutions/1563765/c-on-time-sliding-window/comments/1141941/)

- [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/description/)
- [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/description/)
- [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/description/)
- [2062. Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/)

