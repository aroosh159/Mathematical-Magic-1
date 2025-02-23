Number = int(input("Enter a number"))
print(f"All the possible factors of {Number} are:")
for i in range(1,Number+1):
    if Number%i==0:
     print(i)