"""
Given a set of intervals, for each of the interval i,
check if there exists an interval j whose start point is bigger than or equal to
the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index,
which means that the interval j has the minimum start point to build the "right"
relationship for interval i. If the interval j doesn't exist, store -1 for the
interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

----------
I thought i would need to sort but i ended up looking for the hint of binary search
1. Sort by start points since we are searching on them
2. We also need to store the index since that is what needs to be returned
3. Search the end point of the interval in a loop using binary search.
4. The key thing is to store the index if the start point is bigger than or equal to
5.
This condition works:
    high = len(sortedIntervals) - 1
    low <= high
This doesnt
    high = len(sortedIntervals)
    low < high
"""
import math
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
            def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        intWithI = []
        for i, interval in enumerate(intervals):
            intWithI.append((interval.start, i))
        sortedIntervals = sorted(intWithI, key=lambda interval: interval[0])

        pos = [-1] * len(intervals)
        for i, interval in enumerate(intervals):
            low = 0
            high = len(sortedIntervals) - 1
            s = interval.end
            while low <= high:
                mid = int(low + (high - low) / 2)
                if s == sortedIntervals[mid][0]:
                    pos[i] = sortedIntervals[mid][1]
                    break
                elif s < sortedIntervals[mid][0]:
                    pos[i] = sortedIntervals[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1

        return pos
if __name__== "__main__":
    s = Solution()
    # [[1,2],[2,3],[0,1],[3,4]]
    s.findRightInterval([Interval(4,5), Interval(2,3), Interval(1,2)])
    # 0,1 1,2 2,3 3,4
