#python program armstrong number or not

n=int(input("enter the number:"))

s=0
temp=n

while temp > 0:
    digit=temp%10
    s+= digit **3
    temp//=10

if n==s:
    print('it is armstong number')

else:
    print('it is not armstong number')