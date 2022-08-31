n=int(input("Enter a number to count digit "))
count=0
while n>0:
    count+=1
    n=n//10
print("number of digit in given number is ",count)
