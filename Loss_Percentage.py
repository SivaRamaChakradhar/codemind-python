x, y = map(int, input().split())
loss = x-y
z = (loss/x)*100
print(f"{z:.2f}")