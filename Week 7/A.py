#konversi biner

desimal = int(input())
biner = []

while desimal > 1:
    biner.append(desimal%2)
    desimal = desimal//2

biner.append(desimal)
biner = reversed(biner)
biner = list(map(str,biner))
biner = "".join(biner)
print(biner)


