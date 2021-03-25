#B power stack

def push(S, data):
    S.append(data)
    
def pop(S):
    global cond
    if len(S)>0:
        S.pop()
    else:
        print("ERROR: STACK KOSONG")
        cond = True
        

def powpush(S, jumlah, data):
    for i in range(jumlah):
        S.append(data)

def powpop(S, jumlah):
    global cond
    for i in range(jumlah):
        if len(S)>0:
            S.pop()
        else:
            print("ERROR: STACK KOSONG")
            cond = True
            break
            
            
jml_aksi = int(input())
aksi = []
stack = []
while jml_aksi > 0:
    aksi.append(input().split())
    jml_aksi-=1
    

for i in aksi:
    temp = []
    global cond
    cond = False
    if(i[0] == "PUSH"):
        push(stack,i[1])
    elif(i[0] == "POP"):
        pop(stack)
    elif(i[0] == "POWPUSH"):
        powpush(stack,int(i[1]),i[2])
    elif(i[0] == "POWPOP"):
        powpop(stack,int(i[1]))
    
    if(cond == False):
        print("[ " + " ".join(stack)+" ]")
    #if(len(stack) != 0):
     #   print(stack)
    

