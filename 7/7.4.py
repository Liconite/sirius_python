f = "0 0 0 0 0 0 0"
s = "1 1 1 0 0 0 0"
t = "1 1 1 1 1 1 1"

f = list(map(int, f.split()))
s = list(map(int, s.split()))
t = list(map(int, t.split()))

print(f[0] + f[1] + f[2] - f[3] + f[4] + f[5] - f[6])
print(s[0] + s[1] + s[2] - s[3] + s[4] + s[5] - s[6])
print(t[0] + t[1] + t[2] - (t[3] + t[4] + t[5] - t[6]))
