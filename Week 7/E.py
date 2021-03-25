def push(S, data):
    #addTail => topnya adalah tail,
    #addHead => topnya adalah head,
    S.append(data)
    
def pop(S):
    #removeTail => topnya adalah tail,
    #removeHead => topnya adalah head,
    if len(S)>0:
        S.pop()

def enqueue(S, data):
    #addTail
    S.insert(0,data)
    
def dequeue(S):
    #removeHead
    if len(S)>0:
        S.pop(0)

jml_aksi = int(input())
aksi = []
stack = []
while jml_aksi > 0:
    aksi.append(input().split())
    jml_aksi-=1

for i in aksi:
    temp = []
    if(i[0] == "0"):
        enqueue(stack,i[1])
    elif(i[0] == "1"):
        push(stack, i[1])
    elif(i[0] == "2"):
        dequeue(stack)
    elif(i[0] == "3"):
        pop(stack)
    
stack = list(map(int,stack))
print(sum(stack))