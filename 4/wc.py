import sys

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("wc: No such file or directory: " + sys.argv[1])
else:
    sys.exit("usage: wc [file]")

s = f.read()

s = s.lower()
s = s.replace(',', ' ')
s = s.replace('.', ' ')
s = s.replace('-', ' ')
s = s.replace('_', ' ')
s = s.replace(';', ' ')
s = s.replace(':', ' ')
s = s.replace('"', ' ')
s = s.replace("'", ' ')
s = s.replace('?', ' ')
s = s.replace('!', ' ')
s = s.replace('(', ' ')
s = s.replace(')', ' ')
s = s.replace('/', ' ')
words = s.split()

freqs = {}

for w in words:
    if w in freqs:
        freqs[w] += 1
    else:
        freqs[w] = 1

sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

print("Number of words:", len(words))
print("Top 20 frequent words:")

i = 0
for (k, v) in sorted_freqs:
    if i == 20:
        break
    print(" {}: {}".format(k, v))
    i += 1
