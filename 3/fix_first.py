def fix_first(s):
    firstString = s[0]
    target = s[1:]
    replacedTarget = target.replace(firstString, '*')
    return firstString + replacedTarget


print(fix_first("babble"))
print(fix_first("google"))
print(fix_first("apple"))
print(fix_first("orange"))
