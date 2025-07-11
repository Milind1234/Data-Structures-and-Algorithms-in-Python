def print_items(n):                       #|
    for i in range(n):                    #|...................O(N)    |                            | 
                                          #|                           | n x n = n^2 ......O(n^2)   |
        for j in range(n):                #|...................O(N)    |                            |O(n^2 + n)  = O(n^2)
            print(f"( {i} , {j} )")       #|                                                        |
                                          #|                                                        |
    for k in range(n):                    #|...................O(N)    | n                          |
        print(k)                          #|
                                          #|
print_items(10)                           #|

# Here is the explaination
# You will see that for the first loop, which is nested loop, it is starting from 0,0 and it continues until 9,9.
# So we have performed this one 100 times. So this means that this is going to be O(n⌃2) time complexity, because we have passed ten, 
# it is performing 100 operations and for the second loop we have passed ten.
# Actually, this should be like this and it is performing only ten operations, which is going to be
# O(n) time complexity, because over here n is 10 and it is performing 10 operations and this is going to be O(n) time complexity.
# Now when it comes to the total complexity of this function, it is going to be O(n⌃2+n) time complexity.
# Now, in terms of big O, we can go ahead and simplify this. So we are going to remove the non-dominant terms.
# So the one which is going to be high is going to be dominant term and the one which is low is going to be the non-dominant term.
# So we know that O(n⌃2) is greater than n, so that's why it's going to be O(n⌃2) time complexity.
# So we can easily drop n over here. So if you think about this in terms of if n was 100 or n squared is going to be 10,000 and where the
# single n is going to add only over here 100. So this is not going to affect the number of operations seriously.
# So that's why, as we did in case of dropping the constant, we can drop the 100 from over here and write it like O(n⌃2) time complexity.
# So whenever you see that you have non-dominant terms in your time complexity, 
# you can just go ahead and remove or drop that and you can simplify your time complexity like this.
# So that's how we are dropping the non-dominant terms in case of Big O.