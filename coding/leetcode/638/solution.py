class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        def helper(needs, value):
            if any(num < 0 for num in needs):
                return
            if all(num == 0 for num in needs):            
                self.min = min(self.min, value)
                return
            for i, p in enumerate(price):
                needs[i] -= 1
                helper(needs, value + p)
                needs[i] += 1
            for *quantities, p in special:
                for i, quantity in enumerate(quantities):
                    needs[i] -= quantity
                helper(needs, value + p)
                for i, quantity in enumerate(quantities):
                    needs[i] += quantity
                
        self.min = float('inf')
        helper(needs, 0)
        return self.min
        
        
