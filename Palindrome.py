n = int(input())
d = n
rev = 0
while n!=0:
  rem = int(n%10)
  rev = rev*10+rem
  n=int(n/10)
print(d == rev)  