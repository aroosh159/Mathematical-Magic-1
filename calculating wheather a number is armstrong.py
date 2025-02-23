number = int(input("Enter A number:"))
result=0
temp=number
while temp!=0:
    digit=temp%10
    result=result+digit**3
    temp//=10
print(result)
if result==number:
    print(number,"Is a armstrong number")
else:
    print(number,"Is not a armstrong number")