"""
You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps.
Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element,
and the last element is backward next to the first element. Determine if there is a loop in this array.
A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
"""
import time
class Tester:
    def test(self, fn, expected, *args):
        print("Testing with args: " + str(args))
        start = time.clock()
        actual = fn(*args)
        end = time.clock()
        print("Function took %s seconds"%(str(end-start)))
        print ("Expected: " + str(expected) + ", Actual: " + str(actual))
        assert expected == actual


class Solution(Tester):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        done = -1 * len(nums)
        l = len(nums)
        isLoop = False
        i = 0
        while True:
            print("setting %s to %s"%(i, done))
            if nums[i] == done:
                isLoop = True
                break

            nextI = i + nums[i]
            nums[i] = done
            if nextI > l -1:
                i = l - nextI + 1
            elif nextI < 0:
                i = -1 * nextI
            else:
                i = nextI
            print("setting i to %s"%(i))
            print(nums)
        return isLoop

if __name__ == '__main__':
    s = Solution()
    print(s.circularArrayLoop([2, -1, 1, 2, 2]))
    print(s.circularArrayLoop([-1, 2]))
    # s.test(s.divide, 3, *(10, 3))
    # s.test(s.divide, 10, *(10, 1))
    # s.test(s.divide, -10, *(10, -1))





"""
This one was a bit of a challenge. Note that since nums is a circular array all
elements of it are part of a valid or a invalid loop.
We are basically checking if there is a reachable valid loop from index 0.
Let's call the elements of nums jump since they basically tell us how many steps
we need to jump forward or backward to land on the next element.
Since we know that no jump is zero, start by marking the self-loops with 0. 
You can do that by replacing each jump by j mod n, where j is jump and n is the
length of the list, if it is positive, or -j mod n -1, if it is negative.
Then the fun begins! We have to go through all integers that are not zero and
look for a loop. We do this by using the two-pointer technique.
If the two pointers meet at index i, we found the loop! However,
if one the jumps that the pointers point to is negative and the other one is
positive, this means the jump we started at is not part of a valid loop,
so we mark this jump and all other jumps reachable from this jump with zero so
that we don't get in this invalid loop again.

Time : For each jump is visited maximum 4 times O(4n) = O(n)
Space : O(1)

class Solution(object):
  def circularArrayLoop(self, nums):
    N = len(nums)
    for i, jump in enumerate(nums):
      nums[i] = jump % N if jump > 0 else -jump % N * -1

    def nextindex(i):
      jump = nums[i]
      if   jump > 0: return ( i + jump) % N
      elif jump < 0: return (-i - jump) % N * -1
      else         : return 0

    for i, jump in enumerate(nums):
      if jump != 0:
        slow = fast = i
        slow, fast = nextindex(slow), nextindex(nextindex(fast))
        while nums[slow] * nums[fast] > 0:
          if slow == fast: return True
          slow, fast = nextindex(slow), nextindex(nextindex(fast))
        slow = i
        while nums[slow]:
          nums[slow] = 0
          slow = nextindex(slow)
    return False
"""
