#  O(n) time complexity is also called as linear time complexity.
#  Here, time complexity will grow in direct proportion to the size of input data.
def print_items(n):
    for i in range(n):
        print(i)            

print_items(10)
# So here we have our function.
# Then I'm going to call this function for number ten.
# Now, if I run this, you will see that it's going to print out to the console from zero until nine.
# So this is going to be O(n) time complexity, because we have passed over here ten and it is performing this operation ten times.
# Now, if I just change it to five and run our code, you will see that it's going to perform five times.
# Now, if I just go ahead and change it to 100, you will see that it's going to perform it from 0 to 99.
# So this means that as the input grows, the number of the operations that is performing is going to also grow.
# So this is going to be O(n) time complexity. So to put it in another way, we pass the function the number n and the function runs n times.
# So when we pass ten, it runs ten times. When we pass 100, it runs 100 times. So that is what O of N is.

#  Now let's look at this one in the graph that we have created before.
# 
#      |                                    / O(n)
#    O |                                 /
#    P |                              /
#    E |                           /
#    R |                        /
#    A |                     /
#    T |                  /
#    I |              /
#    O |          /
#    N |       /
#    S |__ / __ __ __ __ __ __ __ __ __ __  O(1)
#      |/__ __ __ __ __ __ __ __ __ __ __ __
#             E L E M E N T S
# 
# Now the O(n) time complexity is going to be the proportional straight line.
# So the number of operations is going to be the proportional to the whatever n is.
# So as we mentioned before, on x axis we have elements and on y axis we have operations.
# So as you can see, as the number of the elements increases, the number of operations increases linearly.
# So this is called O(n) time complexity.
