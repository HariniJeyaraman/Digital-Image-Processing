import random
m=int(input("Enter number of rows of matrix"))
n=int(input("Enter number of columns of matrix"))
matrix=[]
li=[]
print("Enter the values")
for i in range(m):
    a=[]
    for j in range(n):
        a.append(random.randint(0,9))
    
    matrix.append(a)
#storing the matrix in a single list
for i in range(m):
        for j in range(n):
            li.append(matrix[i][j])
li.sort()

#calculating the sum
def find_sum(data):
    sum=0
    for i in range(m):
        for j in range(n):
            sum=sum+matrix[i][j]
    print(sum)
    return sum

def find_max(data):
    max=matrix[0][0]
    for i in range(m):
        for j in range(n):
            if(max<matrix[i][j]):
                max=matrix[i][j]
    print(int(max))

def find_mean(data):
    x=find_sum(li)
    mean=float(x/25.0)
    print(mean)
    return mean

def find_median(data):
    if n % 2 == 0: 
        median1 = li[len(li)//2] 
        median2 = li[len(li)//2 - 1] 
        median = (median1 + median2)/2
    else: 
        median=li[len(li)//2] #division(floor)
    print(median)

#finding freq of each element of the ordered list     
def frequencyDistribution(data):
    freq={i: data.count(i) for i in data}   
    print(freq)
    return freq

def find_mode(data):
    stats=frequencyDistribution(li)
    val=max(stats, key=stats.get)
    print(val)

def std_dev(data):
    mean=find_mean(li)
    var=sum(pow(x-mean,2) for x in li)/len(li)
    std=var**(1.0/2)
    print(std)

print("1. Sum\t2. Maximum\t3. Mean\t4. Median\t5. Mode\t6. Std Deviation\t7.Freq Distribution\t8. Exit\n")
while(True):
    ch=int(input("Enter your choice :"))
    if(ch==1):
        print("The sum of matrix is : ")
        find_sum(li)
    elif(ch==2):
        print("The Max element of the matrix is : ")
        find_max(li)
    elif(ch==3):
        print("Mean is : ")
        find_mean(li)
    elif(ch==4):
        print("Median is : ")
        find_median(li)
    elif(ch==5):
        print("Mode is : ")
        find_mode(li)
    elif(ch==6):
        print("Std Deviation : ")
        std_dev(li)
    elif(ch==7):
        print("Freq Distribution is : ")
        frequencyDistribution(li)
    elif(ch==8):
        break
    else:
        print("Enter valid input")

