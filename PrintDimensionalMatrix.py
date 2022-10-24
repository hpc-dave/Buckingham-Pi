import numpy as np
def Print(A, variables, dimensions, digits = 1):
    list_var = list(variables.keys())
    m, n = A.shape

    print('\t', end = "")
    for v in list_var:
        print(v, end = '\t')
    print("")
    for i in range(0, m):
        print(dimensions[i], end = '\t')
        for j in range(0, n):
            print(round(A[i][j], digits), end='\t')
        print("")
        
    print("")
