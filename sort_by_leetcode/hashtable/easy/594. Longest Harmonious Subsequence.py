"""

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

"""
"""使用一个字典计录元素出现的次数，随后遍历字典，找到两个差距为1的元素，这两个元素出现的次数都大于0而且相加出现的次数最大"""
import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict(collections.Counter(nums))
        max = 0
        for i in dic:
            if dic.get(i,0) > 0 and dic.get(i+1,0) > 0 and dic.get(i,0)+dic.get(i+1,0) > max:
                max = dic.get(i,0) + dic.get(i+1,0)
        return max