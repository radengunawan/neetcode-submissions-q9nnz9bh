class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if (len(nums1) < len (nums2)):
            A, B = nums1, nums2
        else:
            B, A = nums1, nums2
        
        total_length = len(A) + len(B)
        half_length = total_length//2
        median = 0
        L, R = 0, len(A) - 1

        while True:
            #mid index of array A
            i = L + (R - L)//2

            #impacted index on array B
            j = half_length - (i + 1) - 1

            A_left =  A[i] if i >=0 else float("-infinity")
            B_left =  B[j] if j >=0 else float ("-infinity")
            A_right = A[i+1] if (i+1) < len(A) else float ("infinity")
            B_right = B[j+1] if (j+1) < len(B) else float ("infinity")

            if (A_left <= B_right and B_left <= A_right):
                # we are in the correct partition
                if (total_length % 2 !=0):
                    median = min(A_right, B_right)
                else:
                    median = (max(A_left, B_left) + min(A_right, B_right))/2
                return median
            elif (A_left > B_right):
                # A is too high, need to decrease
                R = i - 1
            elif (B_left > A_right):
                # A is too small, need to increase
                L = i + 1

        #return median