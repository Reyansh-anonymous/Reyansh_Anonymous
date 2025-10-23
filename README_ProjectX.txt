I tried installing ROS on Windows, but ended up with a lot of errors. I did learn about system variables, and how you can make changes to the paths. Finally, after 1 day of trouble, I gave up, will try later.

Took help of chatgpt and comet for writing my 5 IR line follower bot. I learnt about PID and how it is used to correct errors in our bot. PID seems useful as of now.
I learnt about the working of a line follower bot. It seems like an easy-to-understand topic. 

I learnt about the Dijkstra( or something like that spelling) Algorithm for maze solving. It used Breadth first search graph traversing algorithm, which appears to be less efficient that depth search first. 

A* and UCS ( Uniform Cost search) Algorithms are similar to dijkstra. A* uses heurestics to find out the shortest path. UCS does not use heurestics, it directly uses path length. A* is effective if we find the right heurestic function for it. For maze solver, I have found out that it is the Manhattan Distance function. If heurestic function cannot be measured, UCS is more effective than dijkstra as it finds the length of the shortest path, whereas dijkstra finds ther lengths of all paths, then figures out the shortest one, rendering increased use of memory space and time.

I took help { A lot:( } from chatgpt to understand and write a simple python code for UCS Alogrithm. It takes in a numpy array and gives out the path and cost for shortest path using UCS Algorithm.


