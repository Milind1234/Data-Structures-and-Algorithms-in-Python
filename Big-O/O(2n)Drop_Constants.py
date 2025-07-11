def print_items(n):
    for i in range(n):   #|
        print(i)         #|
                         #|  here n + n = 2n
    for j in range(n):   #|
        print(j)         #| 

print_items(10)

# Dropping constants means that we can easily eliminate constant values from the asymptotic analysis.
# Big O has several ways in which we can simplify the notation, and it makes things easier.
# So the first thing that we are going to loop at drop constants or you will see it is referred as remove constants.
# So to explain this, I put the code that we had in our O(n).py for the O(n) time complexity.
# So I'm going to add the second loop that is identical to the loop that we have over here.
# So in the first loop we are running from i until n, and in the second loop we are running from j to n,
# so both of them are identical, except we have used i and j over here.
# So here we have to change it to j and run our code.
# You will see that for the first loop, it is starting from zero until nine.So it's coming over here till nine.
# Then for the second loopalso it's starting from zero until nine.
# So this means that both of these loops over here takes O(n) time complexity.
# Now if we sum up them, it's going to take n plus n which is equal to 2n time complexity.
# So we can write it like this.
# Now, this is where that simplification comes in.
# It doesn't matter if the n is 2 or 100,
# if there is a constant, we can easily go ahead and drop that constant.
# And we say that this code is O of N and our first rule for simplifying our big O notation, dropping the constants.