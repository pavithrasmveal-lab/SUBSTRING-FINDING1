a=input("Enter a long sequence:")
b=input("Enter string to find:")
count1=0
count2=0
count3=0
for chr in a:
    count1+=1
for chr in b:
    count2+=1
for i in range(count1):
    if b in a[i:i+count2]:
        count3+=1
print("The number of occurance is:",count3)
