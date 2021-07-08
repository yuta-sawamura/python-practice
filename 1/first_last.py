# s1 = "spring"
# s2 = s1[0:2] + s1[-2:]
# print(s2)

# s1 = "hello"
# s2 = s1[0:2] + s1[-2:]
# print(s2)

# s1 = "abc"
# s2 = s1[0:2] + s1[-2:]
# print(s2)

# -------

# def first_last(s):
#     ret = s[0:2] + s[-2:]
#     return ret


# s1 = "spring"
# s2 = first_last(s1)
# print(s2)

# s2 = first_last("hello")
# print(s2)

# print(first_last("abc"))


def first_last(s):
    if len(s) <= 1:
        return ""
    else:
        ret = s[0:2] + s[-2:]
        return ret


print(first_last("spring"))
print(first_last("hello"))
print(first_last("a"))
print(first_last("abc"))
