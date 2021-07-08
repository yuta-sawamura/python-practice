# def goal(count: int):
#     return print("Number of goals: " + str(count))


# count = 4
# goal(count)

# count = 9
# goal(count)

# goal(11)
# goal(99)


def goal(count):
    if count >= 10:
        return "many"
    else:
        return "Number of goals: " + str(count)


print(goal(4))
print(goal(9))
print(goal(10))
print(goal(99))
