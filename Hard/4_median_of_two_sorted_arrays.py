class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        a, b = -1, len(A) - 1
        half = (len(A) + len(B)) // 2

        while a <= b:
            i = (a + b) // 2
            j = half - (i + 1) - 1

            left1 = A[i] if i >= 0 else float('-inf')
            right1 = A[i+1] if i+1 < len(A) else float('inf')
            left2 = B[j] if j >= 0 else float('-inf')
            right2 = B[j+1] if j+1 < len(B) else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (len(A) + len(B)) % 2 == 1:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                b = i - 1
            elif left2 > right1:
                a = i + 1