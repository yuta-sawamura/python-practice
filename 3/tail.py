f = open('./small.txt', 'r')
reverseTxt = []
for line in f:
    reverseTxt.insert(0, line)
f.close()

for line in reverseTxt:
    print(line)
