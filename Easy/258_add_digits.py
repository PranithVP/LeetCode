def addDigits(num: int) -> int:
    while len(str(num)) > 1: num = sum(int(ch) for ch in str(num))
    return num