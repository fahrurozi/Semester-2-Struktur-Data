import sys

biner = int(input())
biner = str(biner)
forbid = set("23456789")
if any((f in forbid) for f in biner):
    sys.exit
else:
    if(int(biner,2)>=0 and int(biner,2)<=2147483647):
        biner = "0b"+biner
        sys.stdout.write(str(int(biner,2)))

