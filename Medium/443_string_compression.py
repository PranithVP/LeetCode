class Solution:
    def compress(self, chars: List[str]) -> int:
        new_length = 0
        i = 0
        j = 0
        while i < len(chars):
            j = i
            count = 0
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
                count += 1
            
            chars[new_length] = chars[i]
            new_length += 1
            if count > 1:
                for ch in str(count):
                    chars[new_length] = ch
                    new_length += 1
            
            i = j
        
        return new_length