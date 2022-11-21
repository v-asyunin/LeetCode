
class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M': 1000}
        position = 0
        len_ = len(s)
        S = s.upper()
        isValidStr = True
        while position < len_ and position < 100:
            number = dict_.get(S[position])
            symbol = S[position]
            if number is not None:
                if position + 3 < len_ \
                        and S[position]==S[position+1] \
                        and S[position]==S[position+2] \
                        and S[position]==S[position+3]:
                    isValidStr = False
                    print('String is not valid')
                    break

                    #XIX XIV XV XVI LXIX LXVIII
                    #XIIV XV XVIV

                if position-2 >= 0 and dict_.get(s[position-2]) < number:
                    isValidStr = False
                    print('String is not valid')
                    break

                print(number)
            else:
                isValidStr = False

            position+=1

x = Solution()
x.romanToInt('XXXX')
