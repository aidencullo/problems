class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        k_list = list(map(int, list(str(k))))
        carry = 0
        result = []
        while num and k_list:
            digit = k_list.pop() + num.pop() + carry
            carry = digit // 10
            result.append(digit % 10)
        while num:
            digit = num.pop() + carry
            carry = digit // 10
            result.append(digit % 10)
        while k_list:
            digit = k_list.pop() + carry
            carry = digit // 10
            result.append(digit % 10)
        return result[::-1] if carry == 0 else [carry] + result[::-1]
