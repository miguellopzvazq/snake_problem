from itertools import product
import numpy as np


def move_snake(snake,direccion):

    snake =  [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    snake =  [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    snake =  [[5,5], [5,4], [4,4], [4,5]]
 

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
    
    elif(arreq_in_list(move, snake[:-1])):   
        return False 
    
    else:
        return True
     
def valid_routes(board,snake, depth , tested_path = '', routes = []):

    # print(snake)
    
    tested_routes = routes
    new_path = ''

    if (len(tested_path) == depth):
        new_routes = routes + [tested_path]
        
        return (new_routes)
        
 
        
        
    L = np.add(snake[0], [-1,0])
    R = np.add(snake[0], [1,0])
    U = np.add(snake[0], [0,-1])
    D = np.add(snake[0], [0,1])       
    
    
    if(is_valid(L,board,snake)):

        new_path = tested_path + 'L' 
        new_snake = move_snake(snake, new_path)
        
        tested_routes = valid_routes(board, new_snake, depth, new_path, tested_routes)

       
    if(is_valid(R,board,snake)):

        new_path = tested_path + 'R'
        new_snake = move_snake(snake, new_path)
        
        tested_routes = valid_routes(board, new_snake, depth, new_path, tested_routes)
        
    
    if(is_valid(U,board,snake)):

        new_path = tested_path + 'U'
        new_snake = move_snake(snake, new_path)
        
        tested_routes = valid_routes(board, new_snake, depth, new_path, tested_routes)
    
    
    if(is_valid(D,board,snake) ):

        new_path = tested_path + 'D'
        new_snake = move_snake(snake, new_path)
        
        tested_routes = valid_routes(board, new_snake, depth, new_path, tested_routes)
    
    
    return(tested_routes)

def count_valid_routes(board, snake, depth):
    return len(valid_routes(board, snake, depth))
    

# #Test 1:
board =  [4, 3]
snake =  [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
depth =  3
print('\nTest1 - Expected result: 7      Tested result: '+ str(count_valid_routes(board, snake, depth)))

    
#Test 2:
board =  [2, 3]
snake =  [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
depth =  10
print('\nTest2 - Expected result: 1      Tested result: '+ str(count_valid_routes(board, snake, depth)))

#Test 3:
board =  [10, 10]
snake =  [[5,5], [5,4], [4,4], [4,5]]
depth =  4
print('\nTest3 - Expected result: 81     Tested result: '+ str(count_valid_routes(board, snake, depth)))


