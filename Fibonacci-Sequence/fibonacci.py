# Provide the first two values in the Fibonnaci sequence - 0 and 1
fibo = [0,1]

# function to 
def fibonacci(inputval):
    # set fibolen to the number of items in the fibo list
    fibolen = fibo.__len__()
    
    # while the last value in the list is less than value entered by user
    while (fibo[fibolen-1]) < inputval:
        # calculate new fibonacci value based on last two values in the list
        fibonew = fibo[fibolen-1] + fibo[fibolen-2]
        # add the new value to the end of the list
        fibo.append(fibonew)
        # update the fibolen value with the current length
        fibolen = fibo.__len__()
    
    # since the while loop adds in an additional number to the sequence above the entered value
    # remove the last value from the list
    fibo.pop(fibolen-1)

# Request a value from the user to calculate up to
inputval = input('Enter the value to calculate the Fibonacci Sequence up to:- ')

# Call the fibonacci function and pass the value entered by the user
fibonacci(int(inputval))

# Print out the sequence
print(fibo)
