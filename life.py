class GameOfLife:
    def __init__(self):
        self.grid = [[0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],    
                     [0,0,0,0,0,0],    
                     [0,0,0,0,0,0],    
                     [0,0,0,0,0,0]    
                    ]

    def check_neigbours(self,x,y):
     
        left_pos  = self.grid[x][y-1]
        right_pos = self.grid[x][y+1]
        top_pos   = self.grid[x-1][y]
        bot_pos   = self.grid[x+1][y]
        bot_left  = self.grid[x+1][y-1]
        bot_right = self.grid[x+1][y+1]
        top_left  = self.grid[x-1][y-1]
        top_right = self.grid[x-1][y+1]

        neighbours = [left_pos, right_pos, top_pos, bot_left,
            bot_right,bot_pos,top_left,top_right] 
        
        for neighbour in neighbours:
            return neighbour

    def examine_survival(self,x,y):
        neighbours = self.check_neigbours(x,y)
        num_neighbours = sum(neighbours)
        
        if neighbours and num_neighbours in (1,2,4):
            return 0
        elif num_neighbours == 3:
            return 1
 
    def generation(self):

        for i in  self.grid:
            for j in i:
                new_grid = self.examine_survival(i,j)
        return new_grid        
