#python program to reverse an integer

number=1234
reversed_num=0

while number != 0:
    digit = number % 10
    reversed_num = reversed_num * 10 +digit
    number //= 10
    print("reversed number:"+str(reversed_num))