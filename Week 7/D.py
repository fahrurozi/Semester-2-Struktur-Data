#D Nilai Mahasiswa

n = int(input())
if(n > 0 ):
    data = list(map(int,input().split()))
    nilai = []

    for i in data:
        if(i>=0 and i<=100):
            nilai.append(i)

    for j in reversed(nilai):
        print(j)