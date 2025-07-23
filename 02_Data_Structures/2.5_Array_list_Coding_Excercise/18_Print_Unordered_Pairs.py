def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(f"{array[i]}  {array[j]}")
            
printUnorderedPairs([1,2,3,4,5])