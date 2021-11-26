'''decimal to binary'''
n=int(input("enter your number: "))
ans=0
i=0
while(n!=0):
	bit=n&1
	ans=(bit*pow(10,i))+ans
	n=n>>1
	i+=1
print(ans)
'''binary to decimal'''
ans=0
i=0
while(n!=0):
	bit=n%10
	if (bit==1):
		ans=ans+pow(2,i)
	n=n/10
	i+=1
print(ans)
'''there was an mistake but i don't understand'''
