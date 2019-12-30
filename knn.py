import csv
import math
import matplotlib.pyplot as plt

# ------------------------------------------------------
def loadDataset():
    trainSet = []
    train = open('train.csv')
    trainLines = csv.reader(train)
    trainData = list(trainLines)

    testSet = []
    test = open('test.csv')
    testLines = csv.reader(test)
    testData = list(testLines)

    for i in range(len(trainData)):
        trainSet.append(trainData[i])

    for i in range(len(testData)):
        testSet.append(testData[i])

    return testSet, trainSet


# ------------------------------------------------------
def eucledianDistance(d1, d2, length):
    distance = 0
    for x in range(length):
        d1Val = float(d1[x])
        d2Val = float(d2[x])
        distance += pow((d1Val - d2Val), 2)
    return math.sqrt(distance)


def labelReceiver(d1, length):
    labelVal = float(d1[length])
    return labelVal


# ------------------------------------------------------
def getNeighbors(tSet, tInstance, k):
    distances = []  # need this to get k distances
    labels = []  # stores the label for a specific neighbor
    length = len(tInstance) - 1
    for i in range(1, len(tSet)):
        d = eucledianDistance(tSet[i], tInstance, length)

        distances.append(d)
        labelVal = labelReceiver(tSet[i], length)
        labels.append(labelVal)

    neighborList = list(zip(distances, labels))
    neighborList.sort()
    neighbors = []
    for val in range(k):
        neighbors.append(neighborList[val])
    return neighbors


# ------------------------------------------------------

def makePrediction(tSet, tInstance, k):
    preList = getNeighbors(tSet, tInstance, k)
    prediction = 0
    for i, j in preList:
        prediction = prediction + int(j)
    prediction = prediction // k
    if prediction == 1:
        label = 1
    elif prediction == 2:
        label = 2
    elif prediction == 3:
        label = 3
    elif prediction == 0:
        label = 0
    else:
        label = 99
    return label


# ------------------------------------------------------

def exportPlot(mainArray):
    labelArr = []
    accArr = []

    for label, acc in mainArray:
        labelArr.append(label)
        accArr.append(acc)

    plt.plot(labelArr, accArr)
    plt.savefig("plot.png")
    plt.show()

# ------------------------------------------------------

# load our data
testData, trainData = loadDataset()
accuracy_array = []
for k in range(1, 11):

    kVal = k
    accuracy = 0

    for i in range(1, len(testData)):
        deneme = makePrediction(trainData, testData[i], kVal)
        if str(trainData[i][-1]) == str(deneme):
            # print("girdi")
            accuracy = accuracy + 0.1
    accuracy_array.append([k, 100 - accuracy])
    print("k:" + str(k) + " accuracy " + str(100 - accuracy))

for i in accuracy_array:
    print(i)
exportPlot(accuracy_array)
