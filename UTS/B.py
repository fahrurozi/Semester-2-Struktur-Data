#B Antri SPP

n = int(input())
data = []
antri = []
for i in range(n):
    temp = input().split()
    data.append(temp)
nim = input()

if(nim == data[0][0]):
    print("langsung bayar")
else:
    for i in data:
        if(nim == i[0]):
            break
        else:
            antri.append(i[1])
for j in reversed(antri):
    print(j)