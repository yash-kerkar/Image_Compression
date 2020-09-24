n = int(input("Enter number of elements : ")) 
   
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 

def subset_size(a):
    a.sort(reverse=True)
    temp = a[0]
    count = 1
    maxim = 0

    if(temp < 4):
       return 2
    else:
       maxim = two_factor(temp)

    for i in range(len(a)-1):
        if((temp | a[i+1]) > temp):
            temp = temp | a[i+1]
            count += 1
        elif(temp == maxim):
            break

    return count


def two_factor(x):
    i = 0
    sum1 = 0
    while(pow(2,i) <= x):
        sum1 += pow(2,i)
        i += 1
    return sum1

print(subset_size(a))


