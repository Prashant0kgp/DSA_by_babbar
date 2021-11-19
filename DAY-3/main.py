'''if else statement check conditional'''

print('enter integer value')
n1=int(input('enter your 1st number: '))
n2=int(input('enter your 2nd number: '))
if n1>n2:
    print(n1,'greater number')
else:
    print(n2,'greater number')
# output (greater number)
'''Homework'''
# Q-1
a=9
if (a==9):
    print('NINEY')
if(a>0):
    print('POSITIVE')
else:
    print("NEGATIVE")
#  output niney positive
# Q-2
a=2
b=a+1
if ((a==3)==b):
    print(a)
else:
    print(a+1)
# output 3

# Q-3
a=24
if(a>20):
    print("love")
else:
    if (a==24):
        print("lovely")
    else:
        print('babbar')
    print(a)
# output love
'''python program to find type of
input character check number, alphabet or Special Character'''
lst=input('enter your input: ')
if int(ord(lst))>=65 and int(ord(lst))<=90:
    print("upper case Alphabet")
elif int(ord(lst))>=97 and int(ord(lst))<=122:
    print("Lower case alphabet")
elif int(ord(lst))>48 and int(ord(lst))<=57:
    print('input are Digit ')
else:
    print('Special Character')

'''While loop'''
n=int(input('Enter a number '))
i=2
sm=0
while i<=n:
    sm+=i
    # print(sm)
    i+=2
print(sm)
'''F to C converstion'''
F=int(input("enter Fahrenheit: "))
C=(F-32)*(5/9)
print("your celsius value is: ", C)