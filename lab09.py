# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline:
    #   Restate: find the two indices i < j whose values add up to target.
    #   Example: [2, 7, 11, 15], target 9 -> 2 + 7, so [0, 1].
    #   Approach: walk the list once. For each number, the partner we still need is
    #   target - number. Remember numbers we have already seen (value -> index).
    #   If the partner is already in that map, we have the pair. Otherwise store
    #   the current number and keep going. Exactly one answer is guaranteed.
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


def max_profit(prices):
    # Outline:
    #   Restate: buy on one day, sell on a later day, maximize sell - buy. 0 if no gain.
    #   Example: [7, 1, 5, 3, 6, 4] -> buy at 1, sell at 6, profit 5.
    #   Approach: keep the cheapest price seen so far. At each later day, the best
    #   sale using that cheap buy is price - cheapest. Track the largest of those.
    #   A falling list never beats 0, so we start profit at 0.
    if not prices:
        return 0
    cheapest = prices[0]
    best = 0
    for price in prices[1:]:
        if price < cheapest:
            cheapest = price
        else:
            profit = price - cheapest
            if profit > best:
                best = profit
    return best


def max_subarray(nums):
    # Outline:
    #   Restate: the biggest sum of numbers that sit next to each other.
    #   Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 4 + -1 + 2 + 1 = 6.
    #   Approach (Kadane): walk left to right. At each position, either start a new
    #   block here, or extend the block that ends just before. Keep the larger of
    #   those two as the best block ending here, and remember the best ever seen.
    #   All-negative lists still work: the answer is the largest single number.
    best_ending_here = nums[0]
    best = nums[0]
    for num in nums[1:]:
        best_ending_here = max(num, best_ending_here + num)
        if best_ending_here > best:
            best = best_ending_here
    return best


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   Restate: every opening bracket has a matching closer, in the right order.
    #   Example: "{[]}" is fine; "([)]" is not, because ] closes before (.
    #   Approach: use a list as a stack. Push opening brackets. On a closer, the
    #   stack's top must be the matching opener — pop it. An empty stack at the
    #   end means every opener was closed. A leftover opener or a closer with no
    #   match means unbalanced. An empty string is balanced.
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
