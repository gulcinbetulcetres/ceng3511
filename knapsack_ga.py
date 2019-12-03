# starter code for solving knapsack problem using genetic algorithm
import random


class geneClass:
    value = ''
    weight = ''

    def __init__(self, weight, value):
        self.value = value
        self.weight = weight

    def __str__(self):
        return "value : " + str(self.value) + " weight : " + str(self.weight)


class chromosome:
    age = ''
    chrom = []
    fv = ''
    wt = ''

    def __init__(self, age, chrom, fv, wt):
        self.age = age
        self.chrom = chrom
        self.fv = fv
        self.wt = wt

    def __str__(self):
        return "age : " + str(self.age) + " chrom : " + str(self.chrom) + " fv : " + str(self.fv) + " wt : " + str(
            self.wt)


fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')

c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))


def rouletteWheelSelection(chromosomes):
    pick = random.uniform(0, c)
    current = 0
    for chromosome in chromosomes:
        current = chromosome.wt
        if current < pick:
            return chromosome


def tournementSelection(chromosomes, k):
    selectedChrom: chromosome = None
    for i in range(k - 1):
        index = random.randint(0, len(chromosomes)-1)
        currentChrom = chromosomes[index]
        if (i == 0):
            currentChrom = chromosomes[index]
            selectedChrom = chromosomes[index]
        while currentChrom.wt > c:
            index = random.randint(0, len(chromosomes)-1)
            currentChrom: chromosome = chromosomes[index]
        if currentChrom.fv > selectedChrom.fv:
            selectedChrom = currentChrom
    return selectedChrom


def crossover(firstParent, secondParent, n):
    k = []
    livings = []

    for i in range(n):
        k.append(random.randint(0, len(secondParent.chrom)))
    k = sorted(k)
    firstChild = []
    secondChild = []
    lastPoint = 0
    first = False
    for pointIndex in range(0, len(k)):
        if (pointIndex == 0):
            lastPoint = 0
        if (pointIndex % 2 == 0):
            firstChild.extend(firstParent.chrom[lastPoint:k[pointIndex]])
            secondChild.extend(secondParent.chrom[lastPoint:k[pointIndex]])
            first = True
        else:
            firstChild.extend(secondParent.chrom[lastPoint:k[pointIndex]])
            secondChild.extend(firstParent.chrom[lastPoint:k[pointIndex]])
            first = False

        lastPoint = k[pointIndex]

    if (first):
        firstChild.extend(secondParent.chrom[lastPoint:])
        secondChild.extend(firstParent.chrom[lastPoint:])
    else:
        firstChild.extend(firstParent.chrom[lastPoint:])
        secondChild.extend(secondParent.chrom[lastPoint:])

    firstValue = 0
    secondValue = 0
    firstWeight = 0
    secondWeight = 0
    firstmutProb = random.uniform(0, 1)
    secondmutProb = random.uniform(0, 1)

    if firstmutProb >= mutProb:
        mutatedGene = random.randint(0, len(firstChild)-1)
        firstChild[mutatedGene] = 1 - firstChild[mutatedGene]

    if secondmutProb >= mutProb:
        mutatedGene = random.randint(0, len(secondChild)-1)
        secondChild[mutatedGene] = 1 - secondChild[mutatedGene]


    for i in range(len(w)):

        firstValue += (firstChild[i] * v[i])
        firstWeight += (firstChild[i] * w[i])

        secondValue += (secondChild[i] * v[i])
        secondWeight += (secondChild[i] * w[i])

    bornFirstChild = chromosome(0, firstChild, firstValue, firstWeight)
    bornSecondChild = chromosome(0, secondChild, secondValue, secondWeight)

    livings.append(firstParent)
    livings.append(secondParent)

    livings.append(bornFirstChild)
    livings.append(bornSecondChild)

    return livings

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

popSize = int(input('Size of population : '))
genNumber = int(input('Max number of generation : '))
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))
if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(len(w)) + ') '))

print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))

print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))

print('\nSurvival Selection\n---------------------------')
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
elitism = bool(input('Elitism? (Y or N) '))

print('\n----------------------------------------------------------')
print('initalizing population')
population = []
for i in range(popSize):
    temp = []
    for j in range(len(w)):
        temp.append(random.randint(0, 1))
    population.append(temp)

chromfitness = []

print('evaluating fitnesses')
for i, chrom in enumerate(population):
    vt = 0
    wt = 0
    for j, gene in enumerate(chrom):
        vt += gene * v[j]
        wt += gene * w[j]
    # print(i + 1, chrom, ft, wt)
    chromfitness.insert(i, chromosome(0, chrom, vt, wt))

lastPopulation = []
for k in range(genNumber):
    newPopulation = []
    for i in range(int(len(chromfitness) / 2)):
        if parentSelection == 1:
            selectedChromOne = rouletteWheelSelection(chromfitness)
            selectedChromTwo = rouletteWheelSelection(chromfitness)
            if (selectedChromOne is not None) & (selectedChromTwo is not None):
                templist = crossover(selectedChromOne, selectedChromTwo, n)
                templist[0].age = k
                templist[1].age = k
                newPopulation.extend(templist)

        else:
            selectedChromOne = tournementSelection(chromfitness, k)
            selectedChromTwo = tournementSelection(chromfitness, k)
            if (selectedChromOne is not None) & (selectedChromTwo is not None):
                templist = crossover(selectedChromOne, selectedChromTwo, n)
                templist[0] = k
                templist[1] = k
                newPopulation.extend(templist)
    chromfitness = newPopulation
    if(survivalSelection == 1 & elitism):
        maxAge = max(myChromosome.age for myChromosome in chromfitness)
    elif(survivalSelection == 2 & elitism):
        maxValue = max(myChromosome.fv for myChromosome in chromfitness)
    lastPopulation = chromfitness
base : chromosome= None
for i in lastPopulation:
    base : chromosome = i
    if i.fv > base.fv:
        base = i

fout.write('chromosome: ' + str(base.chrom) + '\n')
fout.write('weight: ' + str(base.wt) + '\n')
fout.write('value: ' + str(base.fv) + '\n')
fout.close()
##################################################################


