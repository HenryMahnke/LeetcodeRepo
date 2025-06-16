#encode and decode strings 
"""design an algorithm to encode a list of strings to a single string. The encoded string is then 
decoded back to the original list of strings. 
input: ["neet", "code", "love", "you"]
output: ["eet","code","love","you"]"""

"""O(m) time for each encode() and decode() call and O(m+n) space, where m is the sum of lengths of all strings 
and n is the number of strings."""

"""this question is so vague, i am wondering if there is some common way that i should be encoding and decoding, 
but it literally doesn't say.... 

we know that you can't decrept a hash, so you couldn't just hash the strings then undo it 
we could just store all letters as the upper case number value, and decode could do the opposite 

well, i kinda spoiled the solutin for myself, it seems like i could just use some delimter in the front
and it seems like the most common is to use length delimiting
"""

def encode(strs):
    # in python the way to get the character is the ord function
    #i wonder if i can just shift all the things
    outputStr = 0
    for curString in strs:
        print(curString)
        for char in curString: 
            print(char)
            ascii_val = ord(char)
            print(ascii_val)
            outputStr = outputStr << 8 #each asii char is 256 bit
            outputStr += ascii_val
            print(outputStr)

def decode(s):
    output = 0 


    return output


strs = ["neet"]
s = encode(strs)
decode(s)