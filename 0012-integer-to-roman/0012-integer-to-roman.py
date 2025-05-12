class Solution:
    def intToRoman(self, num: int) -> str:
        bb = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        aa = {"4":{"1":"M"},"3":{"5":"D","1":"C"},"2":{"5":"L","1":"X"},"1":{"5":"V","1":"I"}}
        length = len(str(num))
        list_str = str(num)
        result = ""
        idx = length
        for i in list_str:
            if idx ==4:
                result += aa[str(idx)]["1"] * int(i)
            else:
                if i == "0":
                    pass
                elif 1<=int(i)<=3:
                    result += aa[str(idx)]["1"] * int(i)
                elif int(i) <=5:
                    result += ( aa[str(idx)]["1"] * (5-int(i)) )
                    result += aa[str(idx)]["5"]
                elif int(i) <= 8:
                    result += aa[str(idx)]["5"]
                    result += ( aa[str(idx)]["1"] * (int(i)-5) )
                else:
                    result += ( aa[str(idx)]["1"] * (10-int(i)) )
                    result += aa[str(idx+1)]["1"]
            idx -= 1
        return result