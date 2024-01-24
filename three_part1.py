# Get user input and convert it to an integer.
n = int(input("Input: "))

def countup(n):
    """ Called when n is a negative number. It recursively calls itself adding 1 to n till n gets to zero."""
    # Basecase
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

def countdown(n):
     """ Called when n is zero or greater. It recursively calls itself deducting 1 from n till n gets to zero.""" 
     # Basecase
     if n <= 0: 
          print('Blastoff!') 
     else: 
          print(n) 
          countdown(n-1)
# Conditionally calling the functions 
if n >= 0:
     countdown(n)
elif n < 0:
     countup(n)
