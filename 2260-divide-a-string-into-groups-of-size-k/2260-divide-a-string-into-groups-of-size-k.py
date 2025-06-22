class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        count = len(s)//k
        extra = len(s)%k
        if extra >0:
            count += 1
        result = []
        for i in range(count):
            first_idx = i*k
            if extra >0 and i == count-1:
                result.append(s[first_idx:first_idx +k]+fill*(k-extra))
                continue
            result.append(s[first_idx:first_idx+k])
        return result