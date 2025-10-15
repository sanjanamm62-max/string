# print("haii")


# n=4
# for i in range(1,n+1):
#     print(str(i)*(2*(n-i)+1))
# for i in range(n-1,0,-1):
#     print(str(i)*(2*(n-i)*1))


#Hourglass Pattern
n=5
for i in range(n,0,-1):
    print(''*(n-i)+'*'*i)
for i in range(2,n+1):
    print(''*(n-i)+'*'*i)
#
a=[9,0,2]
b=[2,0]

b_set = set(b)
result = [x for x in a if x not in b_set]
print(*result)