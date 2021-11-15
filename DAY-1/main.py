'''find the factorial of n'''

n=int(input("enter your number "))
fac=1
if n==0:
    print(1)
for i in range(1,n+1):
    fac=fac*i
    # i+=1
print(fac)

'''check number is prime or not'''

num=int(input('Enter your number'))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("not ptime")
            break
    else:
        print("prime")
else:
    print("not prime")

'''print odd number 1 to N'''

N=int(input("enter your number"))
if N>1:
    for i in range(N+1):
        if i%2!=0:
            print(i)
else:
    print('-ve number')
    