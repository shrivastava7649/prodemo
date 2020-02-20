''''
import random
x=input('enter your brand name ')
x=x.upper()

p=x.split()
length_of_name=len(p)
if length_of_name ==4:
    f=str()
    for i in p:
        f=f+i[0]
    final_name=f[0:2]
    final_name=final_name+'0'+str(random.randint(1111,9999))
    print(final_name)
elif length_of_name >=5:
    f=str()
    for i in p:
        f=f+i[0]
    final_name=f[0:2]
    final_name=final_name+str(random.randint(11111,99999))
    print(final_name)
else:
    final_name=p[0]
    final_name=final_name[0:3]
    final_name=final_name+str(random.randint(11111,99999))
    print(final_name)
    '''''
'''

p=1
l=[0,1,2,0,3]
print('running project ....')
x=10
def xy():
    try:
        print('we are from try')
        p=1
        x/2
        p=22
        print('we are from try 1')
    except:
        pass
    if p==22:
        print(' p val is 22')
    else:
        print(' p val is 1')

xy()
'''
a=input()


len(a)

l=[]
for i in range(len(a)):
    if i==0:
        l.append(a[i])
    elif i==(len(a)-1):

        l.append(a[i])
    elif i==(len(a)-2):
        l.append(a[i])
    else:
        l.append('x')
        print(i)

print(l)


































