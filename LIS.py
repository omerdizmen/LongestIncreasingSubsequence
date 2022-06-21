def LIS(array, n, memo):
    if n < 0:
        return
    
    for k in range(n+1, len(array)):
        if array[k] > array[n]:
            memo[n] = max(memo[n], 1+memo[k])        
    
    print(memo) 
    LIS(array,n-1,memo)
    
    return max(memo)

array = [50,3,10,7,40,80]

memo = [1] * len(array)

print(LIS(array, len(array)-1 ,memo))
