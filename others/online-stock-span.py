"""
901. Online Stock Span

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].



Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation:
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.


Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

-----
The hint says stack

Similar:
https://leetcode.com/problems/online-stock-span/discuss/168311/C%2B%2BJavaPython-O(1)
"""
# class BSTNode:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.count = 0
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

class StackNode:
    def __init__(self, val, days):
        self.val = val
        self.days = days

class StockSpanner(Tester):

    def __init__(self):
        self.stack = []

    # def next(self, price):
    #     """
    #     :type price: int
    #     :rtype: int
    #     """
    #     days = 1
    #     second_stack = []
    #     while self.stack and self.stack[-1].val <= price:
    #         if self.stack[-1].val == price:
    #             days += self.stack[-1].count
    #             self.stack[-1].count += 1
    #         else:
    #             days += 1
    #         stackE = self.stack.pop()
    #         second_stack.append(stackE)
    #
    #     while second_stack:
    #         self.stack.append(second_stack.pop())
    #     self.stack.append(StackNode(price))
    #
    #     return days

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        days = 1
        while self.stack and self.stack[-1].val <= price:
            days += self.stack[-1].days
            _ = self.stack.pop()
        self.stack.append(StackNode(price, days))
        return days
    """
    Faster solution
    """
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        days = 1
        while self.stack and self.stack[-1][0] <= price:
            days += self.stack[-1][1]
            _ = self.stack.pop()
        self.stack.append((price, days))
        return days

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
if __name__=='__main__':
    S = StockSpanner()
    # print(S.next(28))
    # print(S.next(14))
    # print(S.next(28))
    # print(S.next(35))
    # print(S.next(46))
    # print(S.next(53))
    # print(S.next(66))
    # print(S.next(80))
    # print(S.next(87))
    # print(S.next(88))
    # print(S.next(100))
    # print(S.next(80))
    # print(S.next(60))
    # print(S.next(70))
    # print(S.next(60))
    # print(S.next(75))
    # print(S.next(85))

    input = [[24],[5],[33],[80],[97],[11],[88],[5],[72],[3],[43],[88],[40],[93],[72],[61],[17],[35],[42],[60],[100],[29],[51],[94],[35],[63],[77],[64],[76],[20],[96],[18],[59],[30],[64],[30],[44],[69],[27],[73],[35],[14],[62],[17],[44],[40],[8],[72],[69],[78],[55],[56],[17],[21],[23],[53],[82],[36],[89],[74],[72],[34],[12],[97],[86],[41],[87],[90],[35],[51],[34],[70],[92],[99],[75],[31],[89],[100],[35],[95],[52],[97],[100],[82],[69],[16],[1],[60],[71],[94],[52],[70],[65],[21],[65],[99],[12],[69],[62],[38]]
    for i, e in enumerate(input):
        print("i: "+ str(i) + " e: " + str(e[0]) + ": " + str(S.next(e[0])))
