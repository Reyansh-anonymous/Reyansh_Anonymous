import numpy as np 
import heapq as hq # To find out the priority node 

maze = np.array([
    [0,  1, -1,  2,  0],
    [0, -1,  3, -1,  0],
    [0,  1,  1,  2,  -1],
    [2, -1, -1,  1,  -1],
    [-1,  0,  1,  1,  0]
])
  # A demo maze, taken from chatpgt. -1 Represents a wall, and 0 represents a free path, other numbers represent costs

 
start = (0, 0)  
goal = (4, 4)   

vis = np.zeros_like(maze,dtype = bool) # Keep an array of visited nodes, True for visited, False for not visited
cost =0
heap= [] # Maintain an empty array for heap function
y, x= start

direct = [(0,1),(1,0),(0,-1),(-1,0)] #for directions
h =8 # Initial heurestic value
hq.heappush(heap, (0,(y,x))) # initial push

def valid(x,y):
      return 0 <= x < maze.shape[1] and 0 <= y < maze.shape[0]
while heap:
      cost, (y,x) = hq.heappop(heap) # Taking out the cost in each step
      if (y,x) == goal:
            print("Goal Reached, at the expense of:", cost )
            break


      if vis[y,x]:
            continue
      vis[y,x]=True
      
      for dx, dy in direct:
            ny, nx = y+dy, x+dx
            h = abs(nx-4) + abs(ny-4) # Heurestic function using manhattan distance
            if valid(nx,ny):
                  if not vis[ny,nx] and maze[ny,nx]!=-1:
                        
                        hq.heappush(heap,(cost+maze[ny,nx] +h,(ny,nx))) # Storing the least cost and moving on to the next step, which will be popped in while loop
                        
vis[4,4]= True
print(vis) # For path
      
      
      
      
