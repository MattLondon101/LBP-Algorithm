'''
Islander: 
This algorithm converts grid to set, then conducts horizontal and vertical index traversal.
This is more efficient than DFS and it will not classify diagonal land connections at valid connections
'''
# Time Complexity: O(n)
from textwrap import dedent # dedent to remove possible whitespace

grid1 = dedent("""\
    11110
    11010
    11000
    00000""")

grid2 = dedent("""\
    11011
    11010
    00001
    00011""")

grid=grid2 # set grid variable and run it with 'if __name__ == '__main__':' at bottom

class Islander(object):
    def numIslands(self, grid):
        # Convert the grid to a set that contains only land
        self.lands = {
            (row, col)
            for row, line in enumerate(grid)
            for col, land in enumerate(line)
            if land == '1'
        }

        island_counter = 0
        # Remove islands from the set one by one
        while self.lands:
            island_seed = next(iter(self.lands))  # choose a random land
            island_counter += 1
            self.remove_island(island_seed)

        return island_counter
    
    '''remove_island ensures islands are classified only
    if connected horizonally and vertically'''
    def remove_island(self, coordinates):
        try:
            self.lands.remove(coordinates)
        except KeyError:
            return

        x, y = coordinates
        # traverse horizontal and vertical
        self.remove_island((x - 1, y))
        self.remove_island((x + 1, y))
        self.remove_island((x, y - 1))
        self.remove_island((x, y + 1))

if __name__ == '__main__':
    grid = [list(line) for line in grid.splitlines()]
    print(Islander().numIslands(grid))
    
'''grid2 will output 3 islands, which is correct when
excluding diagnonal connections'''
