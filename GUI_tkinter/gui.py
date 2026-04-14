l1=[]
n=int(input("Enter no. ofelements in list :"))
for i in range(0,n):
    ele=int(input())
    l1.append(ele)

print("list ",l1)
l1.extend([2,5,8])
print(l1)
l1.insert(2,10)
print(l1)
l1.sort()
print(l1)

