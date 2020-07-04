"""
This is my first path finding algorithm. For now it will be without UI but I will probably make one once I have a good
understanding of how the algorithm works.
"""

import queue

# THE MAIN ALGORITHM

q = queue.Queue()  # Creating a queue.
q.put("")  # Putting a blank string inside the queue.
path = ""  # We set the path to blank string, which represents the first move/path.
maze = createMaze()  # This is the maze that we run through to see if we have reached the end or not.

while not findEnd(maze, path):  # We will loop through the maze until we find the shortest path to the end.
    path = q.get()  # Dequeue.Get the first item from the queue. "q" represents all of the different things in our queue
    print(path)  # The valid path is printed in a format such as "DDDLLDRR"
    for choice in ["L", "R", "U", "D"]:  # Loop through all of the possible moves.
        move = path + choice  # Whatever was in the queue + the last choice/iteration.
        if valid(maze, move):  # Before the move is added it is validated. If it's invalid we go to the next one.
            q.put(move)  # The move is a valid one and it is added to the queue...the loop starts over.

# Once the loop breaks the path will be equal to whatever the last path in the queue is.
