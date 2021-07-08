s1 = "The quick brown fox jumps over the lazy dog."
s2 = s1[0:3]
print(s2)

s3 = s1[16:19]
print(s3)

s4 = s1[4:9] + " " + s1[-4:-1]
print(s4)

s4 = s2 + " " + s1[35:39] + " " + s1[10:15] + " " + s3 + s1[-1]
print(s4)
