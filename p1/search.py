import sys
import collections
import time
from collections import deque

import queue as Q

DosyaAdi = ""
try:
    DosyaAdi = sys.argv[1]
    print (DosyaAdi)
except:
    print("Herhangi bir dosya parametresi gelmedi...")
MainDictionary = {}

# A:{A:0, B:6, C:4, D:3, E:0, F:0, G:0}
def DosyaOku(DosyaAdi):
    # Dosyayı Okuyoruz
    f= open(DosyaAdi,"r")
    # Herbir satırı okuyup listeye ekliyoruz
    f1 = f.readlines()
    counter = 0
    #Herbir satır içerisindeki herbir karakteri sözlük yapısını oluşturabilmek için kontrol ediyoruz.
    for x in f1:
        # Bu kısımlar ilgili aralıkları doğru yakalayabilmek için..
        if counter == 6:
            Sozluk = x[3:-1]
        else:
            Sozluk = x[3:-2]
        # Süslü parantez içlerini virgülle ayırdık.
        Sozluk = Sozluk.split(",")
        # Ek bir sözlük oluşturuyoruz.
        Sozluk1 = {}
        for i in Sozluk:
            #boşlukları temizledik
            i = i.replace(" ", "")
            # "A" : "0" yapısını diziye aktarmak için split yaptık
            Ayir = i.split(":")
            Sozluk1[Ayir[0]] = int(Ayir[1],10)
        # Sözlük içerisindeki herbir keyin, value değeri başka bir sözlük, bu yüzden atama yapıyoruz.
        MainDictionary[x[0]] = Sozluk1
        counter = counter + 1
    #Sözlük Yapısı doğru oluştu mu diye bastırıyoruz.

DosyaOku(DosyaAdi)

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

        
def DFS(visited, StartNode, GoalNode, DFSPATHS):
    if StartNode in visited:
        return DFSPATHS
    DFSPATHS.append(StartNode)
    index =(list(MainDictionary).index(StartNode))
    visited[index] = True

    if StartNode == GoalNode:
        return DFSPATHS

    values = ReturnKeyVal(StartNode)
    for key in values:
        index =(list(values).index(key))
        if visited[index] == False and values[key] != 0:
            return DFS(visited, key, GoalNode, DFSPATHS)

def UCS(start, end):
    
    queue = Q.PriorityQueue()
    queue.put((0, [start])) 
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            #print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            Node1Length = len(node[1])
            counter = 0
            for i in node[1]:
                if counter == Node1Length - 1:
                    print (i, end = "")
                else:
                    print (i, end = " - ")
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
    print("BFS : ", end = " ")               
    PathBFS = BFS(StartNode, GoalNode)
    counter = 0
    for i in PathBFS:
        if counter == len(PathBFS) - 1:
            print (i, end= "")
        else:
            print (i, end= " - ")
        counter = counter + 1
    print ("")
    visited = [False] * (len(MainDictionary))
    print("DFS : ", end = " ")  
    PathDFS = []
    PathDFS = DFS(visited, StartNode, GoalNode, PathDFS)
    counter = 0
    for i in PathDFS:
        if counter == len(PathDFS) - 1:
            print (i, end= "")
        else:
            print (i, end= " - ")
        counter = counter + 1
    
    print ("")
    print("UCS : ", end = " ") 
    UCS(StartNode, GoalNode)


if __name__ == "__main__":
    while 1:
        (StartNode, GoalNode) = Menu()
        WorkProcess(StartNode, GoalNode)