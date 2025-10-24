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

hq.heappush(heap, (maze[y,x],(y,x)))

def valid(x,y):
      return 0 <= x < maze.shape[1] and 0 <= y < maze.shape[0]
while heap:
      cost, (y,x) = hq.heappop(heap) # Popping the cumulated cost  and current step that we are on
      if (y,x) == goal:
            print("Goal Reached, at the expense of:", cost)
            break


      if vis[y,x]:
            continue
      vis[y,x]=True
      
      for dx, dy in direct:
            ny, nx = y+dy, x+dx
            if valid(nx,ny):
                if not vis[ny,nx] and maze[ny,nx]!=-1:
                    hq.heappush(heap,(cost+maze[ny,nx],(ny,nx))) # Pushing the least cost value to heap and moving on to next step, for popping in the while loop
vis[4,4]= True
print(vis) # For path
      
      
      
      
      
      
