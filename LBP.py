# Run via: lbpc(image matrix, width of matrix, height of matrix)

def get_pixel(img, center, x, y):
    new_value = 0
    try:
        if img[x][y] >= center:
            new_value = 1
    except:
        pass
    return new_value

def lbpc(img, x, y):
    '''

     64 | 128 |   1
    ----------------
     32 |   0 |   2
    ----------------
     16 |   8 |   4    
     
mat1 =  np.array([[1, 1, 0, 0, 0], 
                  [0, 1, 0, 0, 1], 
                  [1, 0, 0, 1, 1], 
                  [0, 0, 0, 0, 0], 
                  [1, 0, 1, 0, 1]]) 

mat2 =  np.array([[1, 1, 1, 1, 0], 
                  [1, 1, 0, 1, 0], 
                  [1, 1, 0, 0, 0], 
                  [0, 0, 0, 0, 0]]) 

mat3 =  np.array([[1, 1, 0, 1, 1], 
                  [1, 1, 0, 1, 0], 
                  [0, 0, 0, 0, 1], 
                  [0, 0, 0, 1, 1]]) 


    '''    
    center = img[x][y]
    val_ar = []
    val_ar.append(get_pixel(img, center, x-1, y+1))     # top_right
    val_ar.append(get_pixel(img, center, x, y+1))       # right
    val_ar.append(get_pixel(img, center, x+1, y+1))     # bottom_right
    val_ar.append(get_pixel(img, center, x+1, y))       # bottom
    val_ar.append(get_pixel(img, center, x+1, y-1))     # bottom_left
    val_ar.append(get_pixel(img, center, x, y-1))       # left
    val_ar.append(get_pixel(img, center, x-1, y-1))     # top_left
    val_ar.append(get_pixel(img, center, x-1, y))       # top
    
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
    return val    

