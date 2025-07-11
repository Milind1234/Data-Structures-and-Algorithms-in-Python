#O(1) - Constant Time
#The no. of operations do not depend on the size of the input and are always constant.
# For example, let's look at this simple function over here.
def multiply_number(n):
    return n*n

print(multiply_number(5))

# So we have a function called multiply numbers, which is taking "n" as a parameter and it is returning the n multiply n.
# So there is only one operation here that's going to be multiplication.
# So it doesn't matter if the n is 1 or 1 million, the number of operations is going to be always one.
# So that's why this is called constant time complexity.
# Even if we change the input no. from 1 t0 100 and run our code.
# You will see that in this case it's going to return 10,000.
# So this is performing only one operation.
# So it doesn't matter how the input is increasing, the number of operations will remain constant. 
# In the same way if we had a deck of cards and I ask you to remove the first any card at random, 
# you will simply grab a card from the deck without having a search through the entire deck.
# So this is very easy task that takes the constant time, whatever card we grab, that's a constant time complexity.
# So every time if we take the card, it's going to take the same amount of the operation that we are going to do over here.
#      |
#    O |
#    P |
#    E |
#    R |
#    A |
#    T |
#    I |
#    O |
#    N |
#    S |__ __ __ __ __ __ __ __ __ __ __ __  O(1)
#      |__ __ __ __ __ __ __ __ __ __ __ __
#             E L E M E N T S
# So if you look at this complexity in the graph, on the x axis we have number of the elements and on y axis, we have the number of the operations.
# Now, the graph for O(1) time complexity is going to be a flat line across the bottom.
# This is the most efficient, big O time complexity.
# Remember that this will also be referred as a constant time complexity.
# So you will hear O(1) time complexity, or constant time complexity for this complexity.