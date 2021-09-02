from itertools import product
import numpy as np

snake_OG = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]

cont = 1

def move_snake(snake,direccion):

   
    snake =  [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    
    
    for x in direccion:
        if(x == 'L'):
            move = np.add(snake[0], [-1,0])
        elif(x == 'R'):
            move = np.add(snake[0], [1,0])
        elif(x == 'U'):
            move = np.add(snake[0], [0,-1])
        elif(x == 'D'):
            move = np.add(snake[0], [0,1])
        
        snake = snake[:-1]
        snake.insert(0, move)
        snake
        
    return snake   

def arreq_in_list(myarr, list_arrays): 
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)

def is_valid(move, board, snake):    
    if(any(x<0 for x in move)):
        return False
    elif(any(x<1 for x in np.subtract(board,move))):
        return False
    #elif(np.any(np.all(move in snake[:-1]))):
    elif(arreq_in_list(move, snake[:-1])):   
        return False 
    else:
        return True
    
def valid_moves1(board,snake, depth ,res='',paths = []):

    a= paths
    path =''

    if (len(res) == depth):
        new_paths = paths + [res]
        
        return (new_paths)
        
 
        
        
    L = np.add(snake[0], [-1,0])
    R = np.add(snake[0], [1,0])
    U = np.add(snake[0], [0,-1])
    D = np.add(snake[0], [0,1])       
    
    
    if(is_valid(L,board,snake) and res+'L' not in a):

        path = res + 'L' 
        snakeN = move_snake(snake_OG, path)
        a = valid_moves1(board,snakeN, depth, path,a)

       
    if(is_valid(R,board,snake) and res+'R' not in a):

        path = res + 'R'
        snakeN = move_snake(snake_OG, path)

        a = valid_moves1(board,snakeN, depth, path,a)
        
    
    if(is_valid(U,board,snake) and res+'U' not in a):

        path = res + 'U'
        snakeN = move_snake(snake_OG, path)
        a = valid_moves1(board,snakeN, depth, path,a)
    
    
    if(is_valid(D,board,snake) and res+'D' not in a): 

        path = res + 'D'
        snakeN = move_snake(snake_OG, path)

        a = valid_moves1(board,snakeN, depth, path,a)
    
    
    return(a)


#Test 2:
board =  [2, 3]
snake =  [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
depth =  10
#Result: 1

#Test 3:
board =  [10, 10]
snake =  [[5,5], [5,4], [4,4], [4,5]]
depth =  4
#Result: 81

# #Test 1:
# board =  [4, 3]
# snake =  [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
# depth =  3
# #Result: 7

print(is_valid([-1,2],board,snake))
print('\n'+ str(valid_moves1(board,snake, depth)))
a = valid_moves1(board,snake, depth)
#print(snake_paths(board,snake,depth))
