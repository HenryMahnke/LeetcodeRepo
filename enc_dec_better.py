def encode(strs):
    outputStr = ""
    for curStr in strs:
        outputStr += str(len(curStr))
        outputStr += ":"
        outputStr += curStr
    print(outputStr)
    return outputStr


def decode(s):
    i = 0
    output = []
    while i < len(s):
        print(i)
        curString = ""
        lenStr = ""
        while s[i] != ":":
            lenStr += s[i]
            i += 1
        i += 1
        length = int(lenStr)
        print("length", length)
        print("rest of s", s[i:])
        # print("cur value", s[i])
        for j in range(length):
            print("cur value", s[i])
            curString += s[i]
            i += 1
        output.append(curString)
        print(output)
    return output


# strs = [
#     "",
#     "   ",
#     "!@#$%^&*()_+",
#     "LongStringWithNoSpaces",
#     "Another, String With, Commas",
# ]
strs = [""]
s = encode(strs)
print(s)
print(decode(s))
