fps = 45

width = 500
height = 500
brick = 20


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (128,0,128)
orange = (255,165,0)
yellow = (255,255,0)
teal = (0,128,128)


I = [[
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
          ],
     [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
     ], 
     [
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,1,0],
     ],       
     [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
     ], 
    ]            
O = [[
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
          ],
     [
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
     ], 
     [
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
     ],       
     [
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
     ], 
    ]   
S = [[
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0],
            [0,0,0,0],
          ],
     [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0],
     ], 
     [
            [0,1,1,0],
            [1,1,0,0],
            [0,0,0,0],
            [0,0,0,0],
     ],       
     [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,0,0,0],
     ], 
    ]   
Z = [[
            [0,1,1,0],
            [0,0,1,1],
            [0,0,0,0],
            [0,0,0,0],
          ],
     [
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0],
     ], 
     [
            [0,1,1,0],
            [0,0,1,1],
            [0,0,0,0],
            [0,0,0,0],
     ],       
     [
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0],
     ], 
    ]           
L = [[
            [0,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,0,0],
          ],
     [
            [0,0,0,0],
            [0,1,1,1],
            [0,1,0,0],
            [0,0,0,0],
     ], 
     [
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,0],
            [0,0,0,0],
     ],       
     [
            [0,0,0,1],
            [0,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
     ], 
    ]   
J = [[
            [0,0,1,0],
            [0,0,1,0],
            [0,1,1,0],
            [0,0,0,0],
          ],
     [
            [0,1,0,0],
            [0,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
     ], 
     [
            [0,1,1,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,0,0,0],
     ],       
     [
            [0,1,1,1],
            [0,0,0,1],
            [0,0,0,0],
            [0,0,0,0],
     ], 
    ]   
T = [[
            [0,0,0,1],
            [0,0,1,1],
            [0,0,0,1],
            [0,0,0,0],
          ],
     [
            [0,0,1,0],
            [0,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
     ], 
     [
            [0,1,0,0],
            [0,1,1,0],
            [0,1,0,0],
            [0,0,0,0],
     ],       
     [
            [0,1,1,1],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
     ], 
    ]   

shapes = [I,O,S,Z,L,J,T]
shapes_colour = [red,orange,blue,green,teal,purple,yellow]
