def remove_adjacent(li):
    one_before = ''

    for i, v in enumerate(li):
        if v == one_before:
            del li[i]
        one_before = v

    return li


print(remove_adjacent([1, 2, 2, 3]))
print(remove_adjacent([2, 2, 3, 3, 3]))
print(remove_adjacent([]))
