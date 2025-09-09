class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2 
        if len(B) < len(A):
            A,B = B,A
        l1 =0 
        r1= len(A)-1
        m = len(A) 
        n = len(B)
        #m < n
        total = m + n 
        half = (m + n)//2
        isOdd = bool((m+n) & 0x01)
        while True: 
            midA = (r1 + l1)//2 
            midB = half - midA -2

            Aright = A[midA +1] if midA+1 < len(A) else float('inf')
            Aleft = A[midA] if midA >= 0 else float("-inf")
            Bright = B[midB +1] if midB+1 < len(B) else float('inf')
            Bleft = B[midB] if midB >= 0 else float("-inf")

            if Aleft <= Bright and Bleft <= Aright:
                if isOdd: 
                    return min(Aright, Bright) 
                else: 
                    return (min(Aright, Bright) + max(Aleft,Bleft) )/2
            elif Aleft > Bright:
                r1 = midA-1
            else: 
                l1 = midA+1 
        return -1