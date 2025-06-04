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

# from typing import List
# def rotate(nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k == 0: 
#             return 
#         ranged = min(k, len(nums)-1)
#         for i in range(ranged):
#                 if(i<len(nums)):
#                     temp = nums[i]
#                     nums[i] =nums[len(nums)-k+i]  
#                     nums[len(nums)-k+i] = temp
#                     print(nums)
#                 else:
#                      return
#         # print(nums)
#         #then we have to do the bubbling up procedure 
#         # print("after for loop")
#         # print(nums)
#         j = len(nums)-k-1 #index where we want to start bubbling up
#         # print(j)
#         if k < len(nums):
#             while j+1 > k: 
#                 # print(j)
#                 cur = j
#                 for l in range(k):
#                     # print("inside inner for loop") 
#                     temp = nums[j+l]
#                     nums[j+l] = nums[j+l+1]
#                     nums[j+l+1] = temp
#                     #bubble up k times 
#                     # print(nums)
#                 j-=1
#             # print(nums)

# nums = [1,2]
# k=3
# rotate(nums,k)
# print(nums)

#i think im on the wrong track potentially because when i had the input
#[1,2,3] with k = 4 
#my approach really did not scale. As it should have been [3,2,1] and my algorithm basically didn't know what to do I think i'll ask claude for a hint
#prompt: 
##can you give me a small vague hint as to how i could frame this problem better given the things I have tried.
#response: 
"""
Looking at your attempts, you're overcomplicating the swapping logic. Here's a vague hint to reframe your thinking:

Think about the fundamental transformation you need:

Instead of trying to swap elements in complex patterns, consider what the final arrangement actually looks like in terms of reversals
Key insight: The rotation can be achieved by combining simpler operations that you already know how to do efficiently.

Hint: What happens if you reverse different portions of the array in a specific sequence?

For example, with [1,2,3,4,5,6,7] and k=3, think about what reversing the entire array gives you, then what reversing specific subarrays might accomplish.

This approach is much cleaner than the bubbling/swapping logic you've been exploring and naturally works in O(1) space.
"""
#so now im thinking we could reverse the list then do some swapping 
#and if k is greater than the list we can just do some modulus thing 
"""
lets think through this with [1,2,3,4,5,6,7]
if we reverse it we get [7,6,5,4,3,2,1] ah so then if we want k elements reversed then we just reverse the 
other k remaining elements. 
Bro . 
Thtas so much easier. Lets code up an implementation
"""
def rotate(nums, k): 
    def reverseHelper(startIndex,endIndex): 
        for i in range(((endIndex-startIndex)+1)//2):
            temp = nums[startIndex + i]
            nums[startIndex + i] = nums[endIndex-i]
            nums[endIndex-i] = temp 
    #first we want to reverse the whole list
    if k > len(nums): 
        k = k%len(nums)
    reverseHelper(0,len(nums)-1)
    # reverseHelper(0,)
    # print(nums)
    reverseHelper(0,k-1)
    # print(nums)
    reverseHelper(k,len(nums)-1)
    # print(nums)


nums = [-1,-100,3,99]
k = 2
rotate(nums, k)
print(nums)

"""
well, this one was quite the journey and i needed help on it. But i think like really racking my brain on it was 
really healthy, and I'm very glad that I did it, because I thought of a lot of interesting ways of doing it, just 
none of them happened to exactly pan out. i asked claude for the other 2 main ways of solving, and i feel like just
 for documentation sake i'll paste them here: 
 cyclic Replacements: 
 Place each element directly into its final position by following the cycle of moves

 def rotate(nums, k):
    n = len(nums)
    k %= n
    
    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            
            if start == current:
                break
        start += 1
#ah, this is a really interesting solution, and actually quite trivial to implement once you can come up with it. 
it just treats the array like a continuom with the mod operator, and then just places it in its correct spot, and 
saves so that it can continue that. Would definitely need to dig into more to fully understand, but get the basic 
premise 

And then of course the extra array: 
def rotate(nums, k):
    n = len(nums)
    k %= n
    result = [0] * n
    
    for i in range(n):
        result[(i + k) % n] = nums[i]
    
    # Copy back to original array
    for i in range(n):
        nums[i] = result[i]
the way that claude coded this honestly isnt my favorite, and isn't the way that 
i would have implemented it. But all it does is again, treat as a continuom wiht mod, place into the other array. 

I think that the cyclic would have followed had i actually implemented this naive extra array method first 
rather than trying to figure out the O(1) time one of the bat. So maybe this is just proof to always 
implement the naive solution. 
"""