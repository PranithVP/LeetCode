class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(map(lambda x: f"{x:b}", [int(elem) for elem in date.split('-')]))