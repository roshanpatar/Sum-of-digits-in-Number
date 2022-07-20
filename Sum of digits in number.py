t=int(input("Enter no of test cases"))
for _ in range(t):
    num=int(input("Enter a Number to find sum of digits"))
    sum=0
    while (num>0):
        r=num%10
        num=num//10
        sum=sum+r
    print(sum)    
