class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        def helper(needs_local):
            if any(num < 0 for num in needs_local):
                return float('inf')
            if all(num == 0 for num in needs_local):
                return 0
            if tuple(needs_local) in self.memo:
                return self.memo[tuple(needs_local)]
            min_value = float('inf')
            for i, cost in enumerate(price):
                needs_local[i] -= 1
                min_value = min(min_value, helper(needs_local) + cost)
                needs_local[i] += 1
            for *quantities, cost in special:
                for i, quantity in enumerate(quantities):
                    needs_local[i] -= quantity
                min_value = min(min_value, helper(needs_local) + cost)
                for i, quantity in enumerate(quantities):
                    needs_local[i] += quantity
            self.memo[tuple(needs_local)] = min_value
            return min_value

        self.memo = {}
        return helper(needs)
