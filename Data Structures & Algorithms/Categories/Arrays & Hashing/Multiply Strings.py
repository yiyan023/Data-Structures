class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"

        res, m_1 = 0, 1
        for i in range(len(num2)-1,-1,-1):
            digit_1 = int(num2[i])
            carry_over = 0
            m_2 = 1

            for j in range(len(num1)-1,-1,-1):
                digit_2 = int(num1[j])
                product = digit_1 * digit_2 + carry_over
                carry_over = product // 10
                digit = product % 10
                res += digit * m_1 * m_2
                m_2 *= 10
            
            res += carry_over * m_2 * m_1
            m_1 *= 10

        return str(res)
