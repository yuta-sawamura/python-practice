def fb(n):
    result = ""

    if n % 3 == 0:
        result = "Fizz"
    if n % 5 == 0:
        result += "Buzz"

    return result


i = 1
while i <= 20:
    print(i, fb(i))
    i += 1
