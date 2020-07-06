# The-Great-Island-Count-Question
Amazon and many other companies use the Island Count Question in their coding interviews. Generally it's not that difficult. Yet, when the condition of not including diagonal connections is added, things get tricky. This repository shows how to solve both ways.


### How many islands are there? And, how many islands are there when diagonal land connections are invalid? ###
<p align="center">
  <img width="500" height="260" src="https://github.com/MattLondon101/Images/blob/master/Islands.png"
</p>


#### Depth-first search (DFS) and Breadth-first search can easily solve the first question. Yet, it is not so easy when tackling the second ####
<p align="center"> <img width="800" height="400" src="https://github.com/MattLondon101/Images/blob/master/DFS_BFS.png" </p>
  
By converting the matrix, which typically comrpises 0 = water, 1 = land, to a set, then traversing each index in such a way the indices diagnonal to the current index are skipped. The traversal method is also implemented in local binary pattern algorithms, which are commonly used in image classification for computer vision. The file LBP.py generated a standardized value for a 3x3 kernel in a matrix.

<p align="center"> <img width="850" height="3550" src="https://github.com/MattLondon101/Images/blob/master/LBP.png" </p>
