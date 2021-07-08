# def reverse(s):
#     return s[::-1]


# orig = "good"
# result = reverse(orig)
# print(result)

def reverse(s):
    reverseStr = s[::-1]
    if s == reverseStr:
        return "** palindrome **"
    else:
        return "reverse = " + reverseStr


orig = input("Type a phrease: ")
result = reverse(orig)
print(result)
