#B
T = int(input())
for x in range(T):
    inp = input().strip().replace('calculate ', '')
    ans = float(eval(inp))
    print(f"{ans:.6f}")
