a=[2,4,6,8,9,7,-1,0]
b=[2,3,4,56,7,7,8]
maxi=0
mini=0
for i in range(len(a)):
    if maxi<a[i]:
        maxi=a[i]
# print(a)
print(maxi)
for i in range(len(a)):
    if mini>a[i]:
        mini=a[i]
print(mini)
l=0
r=len(a)-1
while(l<=r):
    temp = b[l]
    b[l] = b[r]
    b[r] = temp
    l+=1
    r-=1
print(a)
