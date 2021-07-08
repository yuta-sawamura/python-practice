def verb_ing(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            result = s + "ly"
        else:
            result = s + "ing"
    else:
        result = s
    return result


print(verb_ing("hail"))
print(verb_ing("swimming"))
print(verb_ing("do"))
