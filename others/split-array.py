"""

"""
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A = sorted(A)
        # calculate the total average
        sum = 0
        for i in range(len(A)):
            sum += A[i]
        avg = sum / len(A)
        print("sum: %s"%(sum))
        s = sorted(A)
        start, end = 0, len(A) - 1
        a = list()
        b = list()
        isA = 1
        print(s)
        sumA = 0
        sumB = 0
        while start < end:
            twoAvg = (A[start] + A[end])/2
            if twoAvg <= avg:
                if len(a) == 0:
                    sumA += (A[start] + A[end])
                    a.append(A[start])
                    a.append(A[end])
                elif len(b) == 0:
                    sumB += (A[start] + A[end])
                    b.append(A[start])
                    b.append(A[end])
                elif len(a) > 0 and sumA/len(a) < avg:
                    sumA += (A[start] + A[end])
                    a.append(A[start])
                    a.append(A[end])
                else:
                    sumB += (A[start] + A[end])
                    b.append(A[start])
                    b.append(A[end])
            start += 1
            end -= 1

        print(a)
        print(b)
        return (len(a) > 0 and len(b) > 0)
if __name__ == "__main__":
    s = Solution()
    s.splitArraySameAverage([5,3,11,19,2])
