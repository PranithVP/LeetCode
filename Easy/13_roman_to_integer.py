def romanToInt(s: str) -> int:
    total = 0
    for i, ch in enumerate(s):
        if ch == 'I':
            if (i < len(s) - 1) and (s[i+1] == 'V' or s[i+1] == 'X'):
                total -= 1
            else:
                total += 1
        elif ch == 'V':
            total += 5
        elif ch == 'X':
            if (i < len(s) - 1) and (s[i+1] == 'L' or s[i+1] == 'C'):
                total -= 10
            else:
                total += 10
        elif ch == 'L':
            total += 50
        elif ch == 'C':
            if (i < len(s) - 1) and (s[i+1] == 'D' or s[i+1] == 'M'):
                total -= 100
            else:
                total += 100
        elif ch == 'D':
            total += 500
        elif ch == 'M':
            total += 1000
    return total

print(romanToInt('IV'))