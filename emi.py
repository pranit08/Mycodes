
mp =int(input('enter montly SIP value'))
p=int(input('enter fixed principal:'))
r=float(input('enter Monthly rate of intrest:'))
n=int(input('enter no of months:'))
mr=float(input('enter monthly reduction:'))
n2=int(input('enter no. of months for reduction:'))
nci=0
ci=0
z=0
y = (p) * ((100 + r) / 100)
for i in range(1,n+1):
    x=(z+mp)*((100+r)/100)
    if i==1:
        nci=x+y
    else:
        nci=x
    print("compunded monthly value for month {} ".format(i),nci)
    if i<=n2:
        z=nci-mr
        print("value after reduction ",z)
    else:
        z=nci