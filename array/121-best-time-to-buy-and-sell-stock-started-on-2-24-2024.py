"""
clarify:
choose one day to buy and one day (in future) to sell

input:
prices - price of stock on ith day

output:
maximum profit or 0 if you cannot achieve profit

edge case:
all descending

strategy:
really, you want to find the greatest distance between two numbers where x < y and x precedes y in the array
so basically the smallest number and the largest number where the smallest precedes the largest
so maybe we have variables smal and lar for smallest and alargest
examples
1 2 3 4
4 3 2 1
8 2 1 9
one thing you might do is at each point as you iterate, take the minimum number (either the smallest or the smallest so far enocountered. or, that is, take it to use for next iteration). then on an iteratigon, you could also subtract the current value minues the current smallest encountered value. at the end, either return the largest non-zero answer or return 0 since no profit can be maded

test:
8 2 1 9
s = 8
s = 2
prof = -6
s = 1
prof = -1
prof = 8
return 8

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float("inf")
        profit = 0 # max profit
        for p in prices:
            if p - smallest > profit:
                profit = p - smallest # it is faster to do this and the line above than do the following commented code because subtracting is much faster than writing a variable to disk each time, even when you don't need to: max(profit, p - smallest)
            # for next iteration
            smallest = min(smallest,p)
        return profit if profit >= 0 else 0
