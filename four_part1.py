'''You work as a software developer in a company that creates custom software solutions for various clients.
Your company has been approached by an educational client who wants to develop a function that calculates
the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.
Your manager has instructed you to use incremental development to create the necessary function
and document each stage of the development process. After completing the final stage of development,
you have to test the function with different arguments and record the outputs in your Learning Journal. '''

import math

def compute_hypotenuse(adjacent, opposite):
    '''
    Calculates and returns the length of hypotenuse of a right triangle.
    Takes lengths of adjacent and opposite sides as arguments.
    '''
    # Square adjacent and opposite and add the values
    squared_adj_opp = adjacent ** 2 + opposite ** 2
    
    # Compute square root of the sum and return the value as the length of hypotenuse
    hypotenuse = math.sqrt(squared_adj_opp)
    
    return hypotenuse
print(compute_hypotenuse(3, 4)) # Should print 5.0
print(compute_hypotenuse(5, 12)) # Should print 13.0
print(compute_hypotenuse(7, 24)) # Should print 25.0