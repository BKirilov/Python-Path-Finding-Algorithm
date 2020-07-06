"""
This is my first path finding algorithm. For now it will be without UI but I will probably make one once I have a good
understanding of how the algorithm works.
"""

import queue


def create_map():  # Map 1
    map = []

    map.append(["#", "#", "#", "#", "#", "O", "#"])
    map.append(["#", " ", " ", " ", "#", " ", "#"])
    map.append(["#", "#", "#", " ", "#", " ", "#"])
    map.append(["#", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", " ", "#", "#", " ", "#"])
    map.append(["#", " ", " ", " ", "#", " ", "#"])
    map.append(["#", "X", "#", "#", "#", "#", "#"])

    return map


def create_map2():  # Map 2
    map = []

    map.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    map.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    map.append(["#", " ", " ", " ", "#", " ", "#", " ", "#"])
    map.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    map.append(["#", " ", " ", "#", "#", " ", "#", "#", "#"])
    map.append(["#", "#", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", "X", "#", "#", "#", "#", "#", "#"])

    return map


def print_map(map, path=""):
    for x, pos in enumerate(map[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(map, moves):
    for x, pos in enumerate(map[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "#"):
            return False

    return True


def find_end(map, moves):
    for x, pos in enumerate(map[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if map[j][i] == "X":
        print("Found: " + moves)
        print_map(map, moves)
        return True

    return False


# THE MAIN ALGORITHM

q = queue.Queue()  # Creating a queue.
q.put("")  # Putting a blank string inside the queue.
path = ""  # We set the path to blank string, which represents the first move/path.
map = create_map2()  # This is the map that we run through to see if we have reached the end or not.

while not find_end(map, path):  # We will loop through the maze until we find the shortest path to the end.
    path = q.get()  # Dequeue.Get the first item from the queue. "q" represents all of the different things in our queue
    # print(path)  # The valid moves are printed in a format such as "DDDLLDRR"
    for choice in ["L", "R", "U", "D"]:  # Loop through all of the possible moves.
        move = path + choice  # Whatever was in the queue + the last choice/iteration.
        if valid(map, move):  # Before the move is added it is validated. If it's invalid we go to the next one.
            q.put(move)  # The move is a valid one and it is added to the queue...the loop starts over.

# Once the loop breaks the path will be equal to whatever the last path in the queue is.
