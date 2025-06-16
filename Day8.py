#balid palindrome 

"""given a string s, return true if it is a palindrome,, otherwise return false."""


def isPalindrome(s): 
    l = 0
    r = len(s)-1
    # print(l,r)
    while l <= r:
        if not s[l].isalnum(): 
            l += 1
            continue
        if not s[r].isalnum(): 
            r-=1   
            continue 
        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True

print(isPalindrome("Was it a car or a cat I saw"))