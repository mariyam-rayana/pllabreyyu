n=int(input("enter a number:"))
factors=[i for i in range(1,n+1) if n%i==0]
print("factors:",factors)