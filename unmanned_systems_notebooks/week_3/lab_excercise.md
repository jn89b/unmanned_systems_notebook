

## The Teenage Mutant Ninja Turtles (mostly Donatello) have built a robot turtle to do recon. Currently this robot turtle designed to do the following:
•	Move left, right, up, and down  
•	Keep track of its local position [x,y] 
•	Identify at what location the enemy was encountered 
•	If there is an enemy teleport to the next x coordinate but keep the same y position


## The team wants to test this robot out in a simulation realm. The simulation realm is defined as follows:
•	A 5 x 5 grid map 
•	Have enemies placed at [1,2] and at [4,4] 
•	To keep it simple the robot turtle will start at coordinate [0,0] and end at [5,4]
-	Once the turtle has reached the end position it should report back location where it encountered the enemy. Where the key is the index location of this encounter and the value will be the location of the incident.
