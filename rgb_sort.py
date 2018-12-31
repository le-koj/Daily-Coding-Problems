def rgb_sort(arr):
    LIMIT = len(arr)-1
    review = 1
    
    while review:
        review = 0 
        for index in range(0, len(arr)):
            if (index < LIMIT) and (arr[index] < arr[index+1]):
                review = 1
                arr[index], arr[index+1] = arr[index+1], arr[index]
                
    print(arr)
    return
    
    
rgb_sort(['G','R','R','B','R','B','G','B','R'])
