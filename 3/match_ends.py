def match_ends(li):
    count = 0

    for v in li:
        if len(v) >= 2 and v[0] == v[-1]:
            count += 1

    return count


print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))
