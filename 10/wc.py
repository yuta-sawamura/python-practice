import sys
import re
import urllib.request
import subprocess


def wc(file):
    try:
        if file[:5] == "http:":
            f = urllib.request.urlopen(file)
        else:
            f = open(file, "rb")
    except:
        sys.exit("{}: file error: {}".format(sys.argv[0], file))

    s = f.read()
    f.close()
    p = subprocess.Popen(['wc', '-w'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (out, err) = p.communicate(s)
    ret = pat.search(str(out))
    return int(ret.group())


if len(sys.argv) < 2:
    sys.exit("usage: python {} [files]".format(sys.argv[0]))

sum = 0
s1 = s2 = ""
pat = re.compile(r'\d+')

for file in sys.argv[1:]:
    count = wc(file)
    sum += count
    s1 += "{:d} + ".format(count)
    s2 += "{:7d} {}\n".format(count, file)

print("Total: {} = {}".format(sum, s1[:-3]))
print(s2, end='')
