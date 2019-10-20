import sys
import collections
import time
from collections import deque

import queue as Q

FileName = ""
try:
    FileName = sys.argv[1]

except:
    print("No file parameter")
MainDictionary = {}


def ReadFile(FileName):
    f = open(FileName, "r")

    f1 = f.readlines()
    counter = 0

    for x in f1:
        if counter == 6:
            Dict = x[3:-1]
        else:
            Dict = x[3:-2]
        Dict = Dict.split(",")
        Dict1 = {}
        for i in Dict:
            i = i.replace(" ", "")
            Sep = i.split(":")
            Dict1[Sep[0]] = int(Sep[1], 10)
        MainDictionary[x[0]] = Dict1
        counter = counter + 1


ReadFile(FileName)


def BFS(StartKey, GoalKey):
    Queue = []
    VisitedNodes = []
    Queue.append([StartKey])

    if StartKey == GoalKey:
        return [StartKey]

    while Queue:
        s = Queue.pop(0)
        node = s[-1]

        if node not in VisitedNodes:
            NeighbourNodes = ReturnKeyVal(node)
            for neighbour in NeighbourNodes:
                if NeighbourNodes[neighbour] != 0:
                    new_path = list(s)
                    new_path.append(neighbour)
                    Queue.append(new_path)
                    if neighbour == GoalKey:
                        return new_path
        VisitedNodes.append(node)


def dfs_paths(start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    values = ReturnKeyVal(start)
    for i in values:
        if values[i] != 0:
            for next in set(i) - set(path):
                yield from dfs_paths(next, goal, path + [next])


def UCS(start, end):
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            # print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            Node1Length = len(node[1])
            counter = 0
            for i in node[1]:
                if counter == Node1Length - 1:
                    print(i, end="")
                else:
                    print(i, end=" - ")
                counter = counter + 1
            break

        cost = node[0]
        values = ReturnKeyVal(current)
        for neighbor in values:
            if values[neighbor] != 0:
                temp = node[1][:]
                temp.append(neighbor)
                queue.put((cost + values[neighbor], temp))


def ReturnKeyVal(Target):
    for keys, values in MainDictionary.items():
        if keys == Target:
            return values


def Menu():
    print()
    StartNode = input("Please enter the start state : ")
    GoalNode = input("Please enter the goal state : ")
    StartNode = StartNode.upper()
    GoalNode = GoalNode.upper()
    return StartNode, GoalNode


def WorkProcess(StartNode, GoalNode):
    print("BFS : ", end=" ")
    PathBFS = BFS(StartNode, GoalNode)
    counter = 0
    for i in PathBFS:
        if counter == len(PathBFS) - 1:
            print(i, end="")
        else:
            print(i, end=" - ")
        counter = counter + 1
    print("")

    print("DFS : ", end=" ")

    Paths = list(dfs_paths(StartNode, GoalNode))
    PathDFS = Paths[0]
    counter = 0

    try:
        for i in PathDFS:
            if counter == len(PathDFS) - 1:
                print(i, end="")
            else:
                print(i, end=" - ")
            counter = counter + 1
    except:
        print("Error")

    print("")
    print("UCS : ", end=" ")
    UCS(StartNode, GoalNode)


if __name__ == "__main__":
    while 1:
        (StartNode, GoalNode) = Menu()
        WorkProcess(StartNode, GoalNode)
sys.exit(0)
