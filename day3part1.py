with open("3input.txt") as f: sample = "".join(list(map(lambda x: x if x in "0123456789.\n" else "#", f.read()))).replace("\n", ".\n").strip().split("\n")

x, y, i, sm = 0, 0, "", 0

while y < len(sample):
    x, y, i, sm = (x + max(1, (lambda f,s:f(f,s))((lambda f,s:0 if s[:1]!="." else f(f,s[1:])+1),sample[y][x:]))) % len(sample[y]), y + (x + max(1, (lambda f,s:f(f,s))((lambda f,s:0 if s[:1]!="." else f(f,s[1:])+1),sample[y][x:]))) // len(sample[y]), i + sample[y][x] if sample[y][x].isnumeric() else "", sm + int(i) if len(i) > 0 and not sample[y][x].isnumeric() and "#" in sample[max(y - 1, 0)][max(0, x - (1 + len(i))):(x+1)] + sample[y][max(0, x - (1 + len(i))):(x+1)] + sample[min(y + 1, len(sample) - 1)][max(0, x - (1 + len(i))):(x + 1)] else sm

print(sm)

#print((lambda f, x, y, i, sm: f(f, x, y, i, sm))(lambda self, x, y, i, sm: self(self, (x + max(1, (lambda f,s:f(f,s))((lambda f,s:0 if s[:1]!="." else f(f,s[1:])+1),sample[y][x:]))) % len(sample[y]), y + (x + max(1, (lambda f,s:f(f,s))((lambda f,s:0 if s[:1]!="." else f(f,s[1:])+1),sample[y][x:]))) // len(sample[y]), i + sample[y][x] if sample[y][x].isnumeric() else "", sm + int(i) if len(i) > 0 and not sample[y][x].isnumeric() and "#" in sample[max(y - 1, 0)][max(0, x - (1 + len(i))):(x+1)] + sample[y][max(0, x - (1 + len(i))):(x+1)] + sample[min(y + 1, len(sample) - 1)][max(0, x - (1 + len(i))):(x + 1)] else sm) if y < len(sample) else sm, 0, 0, "", 0))