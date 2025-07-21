import numpy as np

myarr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def linear_search(array,target):
    for idx, i in enumerate(len(array)):
        if target == i:
            print(f"element {target} found at {idx} ")
        else:
            print(f"element not present inside the array")

linear_search(myarr,14)