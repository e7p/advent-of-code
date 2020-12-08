# parse data
data = [(i, int(a)) for i, a in [line.split() for line in open("input")]]

def emulate(code):
    a = 0
    pc = 0
    visited = set()
    while pc not in visited:
        if pc == len(code):
            return a, True
        visited.add(pc)
        if code[pc][0] == "acc":
            a += code[pc][1]
        pc += code[pc][1] if code[pc][0] == "jmp" else 1
    return a, False

result1, _ = emulate(data)
print(f"part 1: {result1}")

result2 = []
for i in range(len(data)):
    code = data[:]
    if code[i][0] == "nop":
        code[i] = ("jmp", code[i][1])
    elif code[i][0] == "jmp":
        code[i] = ("nop",)
    else:
        continue
    a, terminates = emulate(code)
    if terminates:
        result2.append(a)
print(f"part 2: {result2}")