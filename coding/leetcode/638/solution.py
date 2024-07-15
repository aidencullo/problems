class Solution:
    def shoppingOffers(self, prices: list[int], special: list[list[int]], needs: list[int]) -> int:
        def helper(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            if any(num < 0 for num in needs):
                memo[tuple(needs)] = float('inf')
                return float('inf')
            if all(num == 0 for num in needs):
                memo[tuple(needs)] = 0
                return 0
            min_value = sum(need * price for need, price in zip(needs, prices))
            for *quantities, cost in special:
                for i, quantity in enumerate(quantities):
                    needs[i] -= quantity
                min_value = min(min_value, helper(needs) + cost)
                for i, quantity in enumerate(quantities):
                    needs[i] += quantity
            memo[tuple(needs)] = min_value
            return min_value

        memo = {}
        return helper(needs)
