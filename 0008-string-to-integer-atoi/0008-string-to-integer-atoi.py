class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        is_start = False
        is_naigetive  = None
        for i in s:
            if i == "+" and is_start == False:
                is_start = True
                is_naigetive = False
            elif i == "-" and is_start == False:
                is_start = True
                is_naigetive = True
            elif i == " " and is_start == False:
                continue
            elif 48<=ord(i)<=57:
                result += str(i)
                is_start = True
            else:
                break
        if result == "":
            return 0
        else:
            if is_naigetive == True:
                result = -(int(result))
            result = int(result)
        if result > 0:
            return min(result,2147483647)
        else:
            return max(result,-2147483648 )