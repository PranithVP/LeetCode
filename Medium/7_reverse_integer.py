
def reverse(x: int) -> int:
    s = str(x)[::-1]
    if '-' in s:
        s = '-' + s[:-1]
    
    if (-2)**(31) <= int(s) <= (2)**31 - 1:
        return int(s)
    return 0