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

# def encode(strs):
#     # in python the way to get the character is the ord function
#     #i wonder if i can just shift all the things
#     outputStr = 0
#     for curString in strs:
#         print(curString)
#         for char in curString: 
#             print(char)
#             ascii_val = ord(char)
#             print(ascii_val)
#             outputStr = outputStr << 8 #each asii char is 256 bit
#             outputStr += ascii_val
#             print(outputStr)

# def decode(s):
#     output = 0 


#     return output


# strs = ["neet"]
# s = encode(strs)
# decode(s)

#we want to encode a list of strings into a single string. Then decode it back to the og list
def encode(strs): 
    # could come up with a ticker for how many time it wraps when shifting - but then youre doing a delimter anyway 
    #so a asmarter way of doing it is to make the delimtiter to start,a nd then just block off 8 byte chunks of digits, or use underscores or something 
    outputStr = ""
    for curStr in strs:
        lenOfStr = len(curStr)
        outputStr += f"-{lenOfStr}-"
        for curChar in curStr:
            valOfChar = ord(curChar)
            outputStr += str(valOfChar)
            outputStr += "_"
        print(outputStr)
            
    print(outputStr)
    return outputStr


def decode(s):
    output = []
    i = 0
    while i < len(s)-1:
        curChar = s[i]
        if curChar == "-":
            #know that we need to then read the delimter
            #only read the delimiter
            i+=1 
            lengthToReadStr = "" 
            while s[i] != "-":
                lengthToReadStr += s[i]
                i+=1
            lengthToRead = int(lengthToReadStr)
            if int(lengthToRead) == 0:
                print(s[i:])
                i+=1
                output.append("")
                continue
            print(curChar)

            print("length_to_read", lengthToRead)

            #this is the delimiter
            curChar = s[i]
            print(curChar)
            #clears the next dash 
            #this is the start of the string
            i+=1
            curChar = s[i]
            print(curChar)
            curString = ""
            while curChar != "-" and i < len(s)-1:
                # sub reading expression 
                print("remaining bit of String", s[i:])
                print("entering sub expression")
                outChar = ""
                while curChar != "_" and i <len(s)-1:
                    print("curChar" , curChar)
                    outChar += s[i]
                    i+=1
                    curChar = s[i]
                #this is now a value of int that we want to turn into string/char
                print("outchar", outChar)
                curString+=chr(int(outChar))
                if not (i == len(s)-1):
                    i+=1
                    curChar = s[i]
            
            output.append(curString)
            print(curString)
            print("end of string curChar", curChar)
        print(output)
    return output 


strs = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
# strs = [""]
s = encode(strs)
print(s)
print(decode(s))

"""-4-110_101_101_116_
-4-110_101_101_116_-4-99_111_100_101_
-4-110_101_101_116_-4-99_111_100_101_-4-108_111_118_101_
-4-110_101_101_116_-4-99_111_100_101_-4-108_111_118_101_-3-121_111_117_
-4-110_101_101_116_-4-99_111_100_101_-4-108_111_118_101_-3-121_111_117_
-4-110_101_101_116_-4-99_111_100_101_-4-108_111_118_101_-3-121_111_117_
-
length_to_read 4
-
1
entering sub expression
1
1
0
outchar 110
entering sub expression
1
0
1
outchar 101
entering sub expression
1
0
1
outchar 101
entering sub expression
1
1
6
outchar 116
neet
end of string curChar -
['neet']
-
length_to_read 4
-
9
entering sub expression
9
9
outchar 99
entering sub expression
1
1
1
outchar 111
entering sub expression
1
0
0
outchar 100
entering sub expression
1
0
1
outchar 101
code
end of string curChar -
['neet', 'code']
-
length_to_read 4
-
1
entering sub expression
1
0
8
outchar 108
entering sub expression
1
1
1
outchar 111
entering sub expression
1
1
8
outchar 118
entering sub expression
1
0
1
outchar 101
love
end of string curChar -
['neet', 'code', 'love']
-
length_to_read 3
-
1
entering sub expression
1
2
1
outchar 121
entering sub expression
1
1
1
outchar 111
entering sub expression
1
1
7
outchar 117
you
end of string curChar _
['neet', 'code', 'love', 'you']
['neet', 'code', 'love', 'you']
"""

#this technically worked, but god was it every jank as hell