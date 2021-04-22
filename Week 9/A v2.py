#fibonaacci v2

x = int(input())
fib = [1,1]

while len(fib) != x:
  fib.append(fib[-1]+fib[-2])

print(fib[-1])