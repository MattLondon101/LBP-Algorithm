'''
DFS Island Counter:
This algorithm uses Depth-First-Search (DFS) to count islands.
It is accurate, except it will include diagonal land connections as
valid connections.
'''

# Time Complexity: O(m*n)
import numpy as np
mat1 =  np.array([[1, 1, 1, 1, 0], 
                  [1, 1, 0, 1, 0], 
                  [1, 1, 0, 0, 0], 
                  [0, 0, 0, 0, 0]]) 

mat2 =  np.array([[1, 1, 0, 1, 1], 
                  [1, 1, 0, 1, 0], 
                  [0, 0, 0, 0, 1], 
                  [0, 0, 0, 1, 1]]) 

# Refer to island_count(mat) at bottom to enter the specifice matrix


def dfs(mat, visited, i, j):
    # ensure index has not been visited and is not 0
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or visited[i][j] \
        is True or mat[i][j] == 0:        
        return 0
    # label index as True if not 0 and not visited
    visited[i][j] = True
    cnt = 1
    '''this traversal included diagonal and will not distinguish
    horizontal and vertical connections from diagonal'''
    for r in range(i-1, i+2, 1):
        for c in range(j-1, j+2, 1):
            if (r, c) != (i, j):
                cnt += dfs(mat, visited, r, c)
    return cnt

def island_count(mat):
    clusters=list()
    islands=0
    row=len(mat)
    col=len(mat[0])
    # create a matrix of all False values to keep track of visited indexes
    visited=[[False for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            # if index is 1 and it has not been visited, then it is added to counts
            if mat[i][j] == 1 and visited[i][j] is False:
                islands += 1
                h = dfs(mat, visited, i, j)
                clusters.append(h)
    # clusters shows the count of 1 in each cluster
    # you can see for mat2 that diagonal connection is included
    print ('clusters: ',clusters)
    print ('islands: ',islands)
     
island_count(mat2)
# mat2 will output 2 islands
