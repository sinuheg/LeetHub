class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        curr = len(digits)-1
        while curr >= 0 and carry > 0:
            digit = digits[curr]
            result = digit + carry
            digits[curr] = result % 10
            carry = result // 10
            curr -= 1
        if carry > 0:
            digits.insert(0,carry)
        return digits