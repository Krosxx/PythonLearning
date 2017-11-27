

def quickSort(list,low,high):
    i=low
    j=high

    if i >= j:
        return list

    key=list[i]
    while i<j:
        while i<j and list[j]>=key:
            j-=1
        list[i] = list[j]

        while i<j and (list[i]<key):
            i+=1
        list[j]=list[i]
    list[i]=key
    quickSort(list,low,i-1)
    quickSort(list,j+1,high)
    return list


list=[5,4,4,1,4,9,3,1,34,3,6,74]
import time
begin=time.time()
quickSort(list,0,len(list)-1)
end=time.time()
print(list)
print(end-begin)
