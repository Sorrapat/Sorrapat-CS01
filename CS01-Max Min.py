Num = int(input('Enter Your Loop: '))
NumTotal=[]
for i in range(Num):
    data = int(input('Enter Your Data: '))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()
print(NumTotal)
print(NumTotal[0])
nvm = len(NumTotal)
print(NumTotal[nvm-1])





