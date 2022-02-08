# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:09:33 2022

@author: jnguy
"""

ss = 0.5
move_list = [[-ss, 0], #move left
             [ss, 0],
             [0, ss], #move up 
             [0, -ss], #move down
             [ss,ss] # move right up
    ]

def check_in_obstacle(current_position, obstacle_list):
    """takes in current position and compares obstace list 
    if current position is equal to obstacle return True"""
    for obst in obst_list:    
        ## check if current position in obstacle list
        if current_position == obst:
            return True#return a boolean statement
        
    return False




if __name__ == '__main__':
    
    obst_list = [[1,1], [4,3]]
    
    current_position = [2,2]
    
    step_size = 0.5 
    move_list = [[step_size,0], #move left
                      [-step_size,0], #move right 
                      [0,step_size], #move up
                      [0,-step_size], #move down
                      [step_size, step_size] # move up right
                      ]
    
    visited_set = {}
    not_visited_set = {}
    for move in move_list:
        #print("move", move)
        new_position = [current_position[0]+move[0],
                  current_position[1]+move[1]]
        print("new position", new_position)
        
        #check within obstacle
        if check_in_obstacle(current_position, obst_list) == True:
            print("no bueno")
            continue
            
        #check out 
    
    
        
    
    
    

    