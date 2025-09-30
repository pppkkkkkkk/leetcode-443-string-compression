class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        j = 0
        while i<n:
            cnt = 0
            ch = chars[i]
            while i < n and chars[i] == ch:
                cnt += 1
                i += 1
            chars[j] = ch
            j += 1
            if cnt > 1:
                for digit in str(cnt):
                    chars[j] = digit
                    j += 1
            
        return j