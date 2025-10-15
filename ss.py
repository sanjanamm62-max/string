
# n=5
# for i in range(n,0,n-1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

n=int(input(" n num"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()