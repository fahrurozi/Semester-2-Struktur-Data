# C Tumpukan buku

jml_aksi = int(input())
aksi = []
stack = []
while jml_aksi > 0:
    aksi.append(input().split())
    jml_aksi-=1

for i in aksi:
    temp = []
    if(i[0] == "T"):
        temp.append(i[1])
        temp.append(i[2])
        stack.append(temp)
    else:
        if(len(stack) != 0):
            stack.pop()
    
stack = reversed(stack)
for i in stack:
    print(" ".join(i))