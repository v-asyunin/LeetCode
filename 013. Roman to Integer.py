class Solution:
    def romanToInt(self, number: str) -> int:

        digits = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        number.upper()
        prevn = ''

        for n in number:

            # exit if symbol not in dict
            if not digits.get(n, False):
                return -1

            if prevn != '':
                if digits[n] > digits[prevn]:
                    if ((n == 'V' or n == 'X') and prevn == 'I') \
                       or ((n == 'L' or n == 'C') and prevn == 'X') \
                       or ((n == 'D' or n == 'M') and prevn == 'C'):
                        result -= digits[prevn]
                        result += digits[n] - digits[prevn]
                    else:
                        return -1
                else:
                    result += digits[n]
            else:
                result += digits[n]

            prevn = n

        return result

x = Solution()
print(x.romanToInt('II'))

# условие задачи неформализовано, не указано, что может быть несколько вариантов записи числа,
# нет проверки на повторение одного символа более 3х раз
# условие не полное, что затрудняет решение задачи

'''

'III'

'XVI'
'LVIII'

'XIXV'
'MCMXCIV'

'XIXV' ???

'VX' - 

'''
