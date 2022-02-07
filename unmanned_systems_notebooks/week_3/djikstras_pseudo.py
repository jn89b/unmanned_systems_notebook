# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:08:19 2022

@author: jnguy

###### INITALIZATION 
step 1 initiation:
    closed_set = {} -> visited
    open_set = {} -> unvisited 
    start_location = [start_x, start_y]
    end_location = [end_y, end_y]
    
step 2 assign start node as current position:
    set_cost = cost position
    parent = where did I come from, index (set to -1 at start)
    inital position = [0,0]
    current_node = Node(0,0,0, -1)     
    put this current node into your -> open_set 
    current_index = find_index(current_node)
    open_set[current_index] = current_node
    

###### BEGIN SEARCH
step 3: build djikstras:
    
    while not at goal point:
        
        #find minimum cost and get index -> from open_set
        current_index = min of open_set
        current_node = open_set[current_index]
        
        #delete the current index from open_set
        del current_index from open_set 
        
        #put in visited
        visited[current_index] = current_node
        
        ## loop through all moves:
            
            new_position = current_position + move
            
            - check out of bounds:
                if out of bounds:
                    continue 
            - check close to obstacle or on obstacle:
                if close to obstacle or on it:
                    continue
            - check in visited:
                continue 
            
            ## if it passes all three checks we have a legal move
            ## calculate temp node:
                
                distance 
                cost 
                parent
                temp_node = Node(new_position_x, new_position_y
                                 cost, parent_index)
                #find temp node index
                temp_node_index = find_index()
                
                #insert temp node inside the open_set:
                open_set[temp_node_index] = temp_node
                
                
    
        
        
    


""" 
