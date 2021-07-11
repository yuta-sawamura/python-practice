f = open('small.txt', 'r')
list = f.readlines()
pat = "but"
pl = len(pat)
for i in list:
    i1 = i.lower()
    ps = i1.find(pat)
    if ps != -1:
        patx = i[ps:ps+pl]
        print(i)
        ix = i.replace(patx, '***' + patx + '***')
        print(ix)
