numbers=int(input("Enter a number:"))
list=list(map(int,input().split()))

positive_number_count=0

for num in list:
    print(num)
    if num>0:
        positive_number_count+=1
print("final count of positive number is "," ",positive_number_count)
