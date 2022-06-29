
# Python3 program to swap first
# and last element of a lista))

def swaplist(newlist):
    size=len(newlist)

    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp

    return newlist


newlist=[10,20,30]
print(swaplist(newlist))