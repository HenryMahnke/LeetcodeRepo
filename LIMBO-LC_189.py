#rotate array 
#given an integer array nums, rotate the array to the right by k steps, where k is non negative 

# i.e input nums = [1,2,3,4,5,6,7], k = 3
# output -> [5,6,7,1,2,3,4]

#inpupt nums = [-1,-100,3,99] k =2 
#output = [3,99,-1,-100]

#do it in place with O(1) extra space. 
#there are at least three different ways to solve this problem 

#brainstorming 
#we know that there are three different wyas
# 
# One idea:  
#without the challenges question of doing it in O(1) extra space. The most obvious is to just do it
#where we would make an array of size k, we'd copy the last k elements, then starting from the n-k-1 element we'd move them over k spots 
#overwriting as we go, then in the first k spots we would copy over from that array. 

#other idea:
#there is definitely some way that we can swap elements 
#take [1,2,3,4,5,6,7] we want [5,6,7,1,2,3,4]
#probably swap the kth value, with end value, and decrement as we go along 
#[5,6,7,4,1,2,3] 
#then we would need to do swapping on this side to get the order back to correct 
#then here the n-k element needs to end up in the k+1th spot so we could maybe just swap between that difference 
#thats really fuzzy 

#5,6,7, n-k = 7-3 = 4th index = 1, we want to swap to the k+1th spot = the 4th spot = 3rd index = 4 
#swap yields 
#5,6,7,1,4,2,3
#then progressing through this loop we increment the n-k+1 ( 7-3 + 1) = 5th index and the k+1 + 1 (really -1 in here) = 4th index 
#5,6,7,1,2,4,3
#then we get 7-3+2 = 6th index = 3 k+3-1 = k+2 = 5 = 5th index = 4
#5,6,7,1,2,3,4 this seems like it works, but the challenge comes with when there is not a single number to swap 

#nums = [1,2,3,4,5,6,7] k = 2 
# initially do the swapping 
#nums = [6,7,3,4,5,1,2] we know that we can do this. 
#i = 0 
#n-k+i = 7-2 = 5th index with (k)+i th index = 2nd index
#swap 1 and 3
#nums = [6,7,1,4,5,3,2] this is where im nervous about the swapping 
# i = 1
#n-k+1 = 6th index with k+1 = 3rd index 
#swap 4 and 2 
#nums = [6,7,1,2,5,3,4]
#i = 2 
#then what here do we just clamp and swap 
#n-k+2 = 7th index, clamped to 6th with k+2 = 4
#swap 5 and 4 
#nums = [6,7,1,2,4,3,5]
#so this algorithm won't work.
#it alsmost seems like isntead of clamping we want to like fold back 
#maybe its better to think of it recursively as swapping k items until we get to a base case 
"""
swap [n-k:n] with [0:k]
then we want to swap [k:n-k] with [n-k:n]
then we do this recursively. This seems quite promising
but i don't know exactly the implementation details if we don't want to be creating new space, 
and indexing in the same array might be difficult, doable i believe, but difficult

lets try that


"""
# from typing import List
# def rotate(nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k == 0: 
#             return 
#         def rotate_helper(nums, start1, start2, k):
#             print(nums)
#             print(start1,start2)
#             # if start1 > start2:
#             #      return
#             for i in range(k):
#                 print(nums)
#                 temp = nums[start1+i]
#                 nums[start1+i] =nums[start2+i]  
#                 nums[start2+i] = temp
#             rotate_helper(nums,start1+k,start2-k-1,k)
#         rotate_helper(nums,0,len(nums)-k,k)

# nums = [1,2,3,4,5,6,7]
# k=3
# rotate(nums,k)
#this is flawed because it assumes that we are always swaping k items
'''
but once we get here:
[5, 6, 7, 4, 1, 2, 3]
that is of course not the case, because here we want to swap 4 with 123
i keep thinking there is a way to just swap one element or somethign, or swap k elements, but then that doesn't reduce the problem size, making 
that seem flawedd because you need to reduce your problem size for the recrusion to terminate. 
its almost like you do the initial swap, then you just have to "bubble up" the [k:n-k] elements
so we just have to push those up 
so starting from the n-k elements, we do k forward swaps
'''

from typing import List
def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0: 
            return 
        for i in range(k):
                print(nums)
                temp = nums[i]
                nums[i] =nums[len(nums)-k+i]  
                nums[len(nums)-k+i] = temp
        #then we have to do the bubbling up procedure 
        # print("after for loop")
        # print(nums)
        j = len(nums)-k-1 #index where we want to start bubbling up
        # print(j)
        while j+1 > k: 
            # print(j)
            cur = j
            for l in range(k):
                # print("inside inner for loop") 
                temp = nums[j+l]
                nums[j+l] = nums[j+l+1]
                nums[j+l+1] = temp
                #bubble up k times 
                # print(nums)
            j-=1
        # print(nums)

nums = [-1,-100,3,99]
k=2
rotate(nums,k)