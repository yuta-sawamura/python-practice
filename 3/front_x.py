def front_x(x):
    xLi = []
    notXLi = []
    for v in x:
        if v[0] == 'x':
            xLi.append(v)
        else:
            notXLi.append(v)

    return sorted(xLi) + sorted(notXLi)


print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
