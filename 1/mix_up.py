def mix_up(a, b):

    ret = a.replace(a[:2], b[:2]) + " " + b.replace(b[:2], a[:2])
    return ret


print(mix_up("mix", "pop"))
print(mix_up("apple", "orange"))
print(mix_up("google", "yahoo"))
print(mix_up("soccer", "goal"))
