from multiprocessing.sharedctypes import Value
import numpy as NP
import ReducedEchelon as RE
import copy
def nullspace(A_in, variables) :
    A = copy.deepcopy(A_in)
    # test if already in reduced echelon form
    m,n = A.shape
    if n < 2 or m < 2:
        print("not a reallly nice matrix you provided, aye?")
        raise ValueError
    if not n == len(variables):
        print("number of variables and matrix dimensions are inconsistent")
        raise ValueError
    
    A, jb = RE.rref(A)

    # rank of matrix A
    rank = len(jb)

    if rank == 0:
        print('nullspace is of rank 0, returning empty array')
        A_ns = [[]]
        return A_ns


    # determine independent Vectors
    id_var_independent = [('empty' , -1)] * rank
    A_in = NP.identity(rank)
    # counter for independent vectors
    vcount = 0

    for i in range(n):
        if vcount == rank:
            break

        col_vec = A[:, i]
        if NP.count_nonzero(col_vec) == 1 and vcount < rank:
            pos = (col_vec != 0).nonzero()[0].item()
            if col_vec[pos] == 1:
                tuple_loc = id_var_independent[pos]
                if not tuple_loc[0] == 'empty':
                    continue

                id_var_independent[pos] = (variables[i][0], i)
                vcount += 1
    
    # determine nullspace

    # allocating nullspace of A
    A_ns = NP.zeros((n, n-rank))

    ccount = 0
    for i in range(n):
        is_independent = False
        for v in id_var_independent:
            if v[1] == i:
                is_independent = True
                break

        if is_independent:
            continue

        A_ns[i, ccount] = 1
        for v in id_var_independent:
            A_ns[v[1], ccount] = -A[id_var_independent.index(v), i]

        ccount += 1

    return A_ns
