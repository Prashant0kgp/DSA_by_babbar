n=int(input('enter a number: '))
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(n-j+1 ,end=' ')
        j+=1
    i+=1
    print('\r')
'''OUTPUT
4 3 2 1 
4 3 2 1
4 3 2 1
4 3 2 1
'''

i=1
Count=1
while(i<=n):
    j=1
    while(j<=n):
        print(Count, end=' ')
        Count+=1
        j+=1
    print("\r")
    i+=1
'''OUTPUT
1 2 3 
4 5 6
7 8 9
'''

row=1
count=1
while(row<=n):
    col=1
    while(col<=row):
        print(count,end=" ")
        count+=1
        col+=1
    print('\r')
    row+=1
'''OUTPUT
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

i=1
while (i<=n):
    j=1
    value=i
    while(j<=i):
        print(value,end=' ')
        value+=1
        j+=1
    print('\r')
    i+=1
'''OUTPUT
1 
2 3
3 4 5
4 5 6 7
5 6 7 8 9
'''

i=1
while(i<=n):
    j=1
    while(j<=i):
        print(i-j+1,end=' ')
        j+=1
    print('\r')
    i+=1
'''OUTPUT
1 
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

print(chr(65+n))
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(chr(65+j-1),end=" ")
        j+=1
    print("\r")
    i+=1
'''OUTPUT
A B C D 
A B C D
A B C D
A B C D
'''

i=1
while(i<=n):
    j=1
    while(j<=i):
        print(chr(65+i-1),end=" ")
        j+=1
    print("\r")
    i+=1
'''OUTPUT
A 
B B
C C C
D D D D
'''

i=1
while(i<=n):
    j=1
    k=(65+n-i)
    while(j<=i):
        print(chr(k),end=" ")
        k+=1
        j+=1
    print("\r")
    i+=1
'''OUTPUT
E 
D E
C D E
B C D E
A B C D E
'''

i=1
while(i<=n):
    j=1
    k=(65+n-i)
    while(j<=i):
        print(chr(k),end=" ")
        k+=1
        j+=1
    print("\r")
    i+=1
'''OUTPUT
E 
D E
C D E
B C D E
A B C D E
'''


i=1
while(i<=n):
    j=1
    space=n-i
    while(space):
        print(' ',end=" ")
        space=space-1
    j=1
    while(j<=i):
        print('*',end=" ")
        j+=1
    print("\r")
    i+=1
'''OUTPUT
      * 
    * * 
  * * * 
* * * * 
'''

i=1
while(i<=n):
    j=1
    while(j<=n-i+1):
        print('*',end=" ")
        j+=1
    print("\r")
    i+=1
'''OUTPUT
* * * * 
* * *
* *
*
'''

i=1
while(i<=n):
    space=n-i+1
    j=1
    while(j<=space):
        print('*',end=" ")
        j+=1
    print("\r")
    i+=1
'''OUTPUT
* * * * 
* * *
* *
*
'''