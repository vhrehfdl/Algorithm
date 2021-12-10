def solution(A):
    A = sorted(A)
    
    for i in range(0, len(A)-2):
        if ((A[i] + A[i+1]) > A[i+2]) and ((A[i+1] + A[i+2]) > A[i]) and ((A[i+2]+A[i]) > A[i+1]):
            return 1
    
    return 0
