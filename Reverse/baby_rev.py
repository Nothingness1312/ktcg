def p0(): return 49
def p1(): return 50
def p2(): return 51
def p3(): return 52
def p4(): return 53
def p5(): return 54

pw = input("Password: ")

if len(pw) != 6:
    print("Wrong password")
    exit()

pw_check = [p0(), p1(), p2(), p3(), p4(), p5()]

for i in range(6):
    if ord(pw[i]) != pw_check[i]:
        print("Wrong password")
        exit()

print("Access granted")

enc_flag = [
    0x14, 0x42, 0x74, 0x5a,
    0x40, 0x53, 0x12, 0x48,
    0x49, 0x55, 0x60, 0x60
]

flag = "KTCG{"

for b in enc_flag:
    flag += chr((b ^ 0x20) - 1)

flag += "}"

print(flag)
