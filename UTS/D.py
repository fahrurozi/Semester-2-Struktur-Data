#D

n = int(input())
data = list(map(int,input().split()))
Tlist = []
for i in data:
    if(len(Tlist)==0):
        Tlist.append(i)
    elif(len(Tlist)%2==0):
        Tlist.insert(len(Tlist)//2,i)
    else:
        Tlist.insert(len(Tlist)//2,i)
hasil = " ".join(list(map(str,Tlist)))
hasil = hasil.rstrip()
print(hasil+" ")

#OK