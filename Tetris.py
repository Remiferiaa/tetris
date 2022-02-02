import pygame , sys , random
from constants import *

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


class Blocks:
    def __init__(self,shape,colour,x,y):
        self.shape = shape
        self.colour = colour
        self.x = x
        self.y = y
        self.rotate = random.randint(0,3)
    
    def downwards(self):
        self.y += 1


def blshape(): 
    box = random.choice(shapes)    
    box_col = random.choice(shapes_colour)
    spawnP = 3
    piece = Blocks(box,box_col, spawnP, 0)
    return piece 


def bldraw(piece):
    for i in range(4):
      for j in range(4):
        if piece.shape[piece.rotate][i][j] !=0:
            pygame.draw.rect(screen, piece.colour, (100 + piece.x * brick  + brick * j,100 +  piece.y * brick   + brick *i, brick, brick), 0)

               
def get_grid():
    grid = [[0 for x in range(10)] for x in range(20)]             
    return grid


def draw_grid(grid): 
    for i in range(len(grid)):
       for j in range(len(grid[i])):
              if grid[i][j] == 0:
                  pygame.draw.rect(screen,white, (100 + j * brick, 100 + i * brick, brick, brick), 1)     
              elif grid[i][j] == 1:
                  pygame.draw.rect(screen,(150,150,150), (100 + j * brick, 100 + i * brick, brick, brick), 100)
                  pygame.draw.rect(screen,white, (100 + j * brick, 100 + i * brick, brick, brick), 1)  
    pygame.draw.rect(screen,blue,(100,100,200,400),3)


def validity(current_piece, grid,x_change,y_change, rot):
    validity = True
    for i in range(len(current_piece.shape[rot])):
       for j in range(len(current_piece.shape[rot][i])):
              if current_piece.shape[rot][i][j] != 0:
                     next_x = current_piece.x + j + x_change
                     next_y = current_piece.y + i + y_change
                     if next_x < 0 or next_x >= 10:
                            return False
                     if next_y >= len(grid) or grid[next_y][next_x] != 0:     
                            return False
    return validity


def absorb(current_piece,grid):
       for i in range(len(current_piece.shape[current_piece.rotate])):
              for j in range(len(current_piece.shape[current_piece.rotate][i])):
                     if current_piece.shape[current_piece.rotate][i][j] != 0:
                            grid[current_piece.y + i][current_piece.x + j]  = 1  

                            
def clear_row(grid):
       for i in range(len(grid)):
              if grid[i] == [1 for x in range(10)]:
                     del grid[i]
                     grid.insert(0, [0 for x in range(10)])
                     return True
       
       
def game_over(grid):
       for i in range(len(grid[0])):
              if grid[0][i] != 0:
                     return True


def screen_over():
       screen.fill(black)
       font = pygame.font.SysFont("Comic Sans", 24)
       text_over =  font.render("Game Over! Press R to restart", True, white)
       text_quit = font.render("Press Q to quit the game", True, white)
       screen.blit(text_over, (width/10, height/3))
       screen.blit(text_quit, (width/10, height/2))
        

def score(k):
       font = pygame.font.SysFont("Comic Sans", 16)
       j = k * 10
       text_over =  font.render("Score:" + str(j), True, white) 
       screen.blit(text_over, (400, 450))


def gamelevel(grid,level,k):
       score(k)
       if clear_row(grid) == True:
              k += 1
              if k % 10 == 0:
                     level += 0.1
       return k


def main():
       pygame.init()
       stage = get_grid()
       current_piece = blshape()
       c = 0
       k = 0
       level = 0
       game_over(stage) == False
       while True:
              c = (c + 1) * (1 + level)
              if c > 20: 
                     if validity(current_piece, stage,0,1,current_piece.rotate) == False: 
                            absorb(current_piece,stage)
                            c = 0
                            next_piece = blshape()
                            current_piece = next_piece  
                                                        
                     else:
                            current_piece.downwards()
                     c = 0
              
                   
              for event in pygame.event.get():  
                     if event.type == pygame.QUIT:      
                            pygame.quit()
                            sys.exit()
                     if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:
                                   if validity(current_piece, stage,0,1,current_piece.rotate) == True:
                                          current_piece.y += 1
                            if event.key == pygame.K_LEFT:
                                   if validity(current_piece, stage,-1,0,current_piece.rotate) == True:
                                          current_piece.x -= 1                         
                            if event.key == pygame.K_RIGHT:
                                   if validity(current_piece, stage,1,0,current_piece.rotate) == True:
                                          current_piece.x += 1
                            if event.key == pygame.K_UP: 
                                   if validity(current_piece, stage,0,0,(current_piece.rotate + 1) % 4) == True:
                                          current_piece.rotate += 1 
                                   if current_piece.rotate + 1 > 4:
                                          current_piece.rotate = 0 
                            if event.key == pygame.K_SPACE:
                                   while validity(current_piece, stage,0,1,current_piece.rotate) == True:
                                          current_piece.y += 1
                                   


              
              
              screen.fill(black)
              draw_grid(stage)
              bldraw(current_piece)
              k = gamelevel(stage,level,k)       

                     

              clock.tick(fps) 
             
              if game_over(stage) == True:
                     screen_over() 
                     for event in pygame.event.get():  
                            if event.type == pygame.KEYDOWN:
                                   if event.key == pygame.K_r:
                                          main()
                                   if event.key == pygame.K_q:
                                          pygame.quit()
                                          exit()


              
              pygame.display.flip()
                   
                   


main()        

    
          




       
        

    


























