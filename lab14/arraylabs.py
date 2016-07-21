ar=[5,4,3,4,6,8,7,5,9,10,12,15]
ar2=[1,0,2,0,3,0,4,0,5,1,6,2,7,3]
DECREASE=0
INCREASE=1
UNSET=2

def cornerDetect(dists):
    prev=UNSET
    switchCount=0

    dataSize=dists.__len__()
    for x in range(dataSize-1):
        difference=dists[x]-dists[x+1]
        if difference>= 0:
            print("Decrease")
            if prev==INCREASE:
                switchCount=switchCount+1
            prev=DECREASE

        elif difference<= 0:
            print("Increase")
            if prev==DECREASE:
                switchCount=switchCount+1
            prev=INCREASE
        else:
            print("None")

    print (switchCount)
    if switchCount ==3:
        return True
    else:
        return False
print(cornerDetect(ar))
