air = int(input())
penuh = 0

for i in range(6):
    if(air>=1500):
        penuh+=1
        air -= 1500
if(penuh == 6 and air >= 600):
    for i in range(7):
        if(air>=600):
            penuh+=1
            air -= 600
if(penuh == 13 and air >= 200):
    for i in range(9):
        if(air>=200):
            penuh +=1
            air -= 200

print(penuh)
        

#OK