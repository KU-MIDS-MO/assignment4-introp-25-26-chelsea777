import numpy as np

def mask_and_classify_scores(arr):
    """
    write your solution here;
    follow the instructions in the README.
    """
 
    if type(arr)is not np.ndarray:
        return None
    if arr.ndim !=2:
        return None
    rows,cols=arr.shape
    if rows!=cols or rows<4:
        return None
    n = rows
    cleaned = arr.copy()
    for i in range(n):
        for j in range(n):
            if cleaned[i,j]<0:
                cleaned[i,j]=0
            else:
                if cleaned[i,j]>100:
                    cleaned[i,j]=100
    levels = np.zeros((n,n),dtype=int)
    for i in range(n):
        for j in range(n):
            value = cleaned[i,j]
            if value <40:
                levels[i,j]=0
            else:
                if value<70:
                    levels[i,j]=1
                else:
                    levels[i,j]=2
    row_pass_counts = np.zeros(n,dtype=int)
    for i in range(n):
        count = 0
        for j in range(n):
            if cleaned[i,j]>=50:
                count +=1
        row_pass_counts[i]=count
    return cleaned,levels,row_pass_counts
    

