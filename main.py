import numpy as np

# enter name of the file containing the dataset
fname = "TestCase1.txt"  
# degree of polynomial
polysize = 3

# load the data from the file
dataFromFile = np.loadtxt(fname, dtype = 'float', delimiter = '\t')

def power_sum(arr, var, power):
    # slicing the x values from the array
    xVals = arr[:,0]
    # we do not dot with the y elements
    if var == 0:
        return np.sum(xVals**power)
    else:
        # raising each x element to the power
        xVals = xVals**power
        # dot the x values with the y values
        xVals *= arr[:,1]
        return np.sum(xVals)

def regression(data, size):
    # generate placeholder matrices
    A = np.zeros([size, size]) # A is the matrix
    B = np.zeros([size, 1]) # B is the vector

    # generating all the diagonal columns of the matrix
    for i in range(1, size+1):
        for j in range(1, i+1):
            A[j-1][i-j] = power_sum(data, 0, 2*(size-1)-i+1)
            # if not the main diagonal (leftwards)
            if i != size:
                A[j+size-i-1][-j+size] = power_sum(data, 0, i-1)

    # generate the vector, B
    for i in range(0, size):
        # the power we raise the xs to is size-1-i
        B[i][0] = power_sum(data, 1, size-1-i)

    # invert the A matrix
    AInverse = np.linalg.inv(A)
    # return the solution
    return(np.matmul(AInverse, B))

# perform the regression
out = regression(dataFromFile, polysize+1)
print(out)

# formate output nicely
formatted = ""
for i in range(0, polysize+1):
    formatted += str(round(out[i][0], 5))
    if i < polysize:
        formatted += " x"
    if i < polysize-1:
        formatted += "^" + str(polysize-i) 
    if i < polysize:
        formatted += " + "

print(formatted)

