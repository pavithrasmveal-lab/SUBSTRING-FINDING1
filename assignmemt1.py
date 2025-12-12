a=input("Enter a long genome sequence:")
b=input("Enter sub sequence to find:")
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
print("The number of occurance of subsequence in genomesequence is:",count3)

