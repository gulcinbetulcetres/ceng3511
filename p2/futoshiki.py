from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model


def Function(Operation):
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    A1 = model.NewIntVar(1, 4, "A1")
    A2 = model.NewIntVar(1, 4, "A2")
    A3 = model.NewIntVar(1, 4, "A3")
    A4 = model.NewIntVar(1, 4, "A4")

    B1 = model.NewIntVar(1, 4, "B1")
    B2 = model.NewIntVar(1, 4, "B2")
    B3 = model.NewIntVar(1, 4, "B3")
    B4 = model.NewIntVar(1, 4, "B4")

    C1 = model.NewIntVar(1, 4, "C1")
    C2 = model.NewIntVar(1, 4, "C2")
    C3 = model.NewIntVar(1, 4, "C3")
    C4 = model.NewIntVar(1, 4, "C4")

    D1 = model.NewIntVar(1, 4, "D1")
    D2 = model.NewIntVar(1, 4, "D2")
    D3 = model.NewIntVar(1, 4, "D3")
    D4 = model.NewIntVar(1, 4, "D4")

    Row1 = [A1, A2, A3, A4]
    Row2 = [B1, B2, B3, B4]
    Row3 = [C1, C2, C3, C4]
    Row4 = [D1, D2, D3, D4]
    
    Col1 = [A1, B1, C1, D1]
    Col2 = [A2, B2, C2, D2]
    Col3 = [A3, B3, C3, D3]
    Col4 = [A4, B4, C4, D4]

  
    model.AddAllDifferent(Row1)
    model.AddAllDifferent(Row2)
    model.AddAllDifferent(Row3)
    model.AddAllDifferent(Row4)

    model.AddAllDifferent(Col1)
    model.AddAllDifferent(Col2)
    model.AddAllDifferent(Col3)
    model.AddAllDifferent(Col4)

    dicts = {"A1": A1, "A2": A2, "A3": A3, "A4": A4, "B1": B1, "B2": B2, "B3": B3, "B4": B4, "C1": C1, "C2": C2,
             "C3": C3,
             "C4": C4, "D1": D1, "D2": D2, "D3": D3, "D4": D4}

    for x1, x2 in Operation:
        if x2.isdigit():
            model.Add(dicts[x1] == int(x2))
        else:
            model.Add(dicts[x1] > dicts[x2])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        outputFile.write(str(solver.Value(A1)) + ", " + str(solver.Value(A2)) + ", " + str(solver.Value(A3)) + str(solver.Value(A4)) + "\n" +
                         str(solver.Value(B1)) + ", " + str(solver.Value(B2)) + ", " + str(solver.Value(B3)) + str(solver.Value(B4)) + "\n" +
                         str(solver.Value(C1)) + ", " + str(solver.Value(C2)) + ", " + str(solver.Value(C3)) + str(solver.Value(C4)) + "\n" +
                         str(solver.Value(D1)) + ", " + str(solver.Value(D2)) + ", " + str(solver.Value(D3)) + str(solver.Value(D4)))


with open("futoshiki_input.txt", "r") as inputFile:
    Values = []
    for line in inputFile.readlines():
        line = line.replace("\n", "")
        line = line.split(", ")
        Val = (line[0], line[1])
        Values.append(Val)

outputFile = open("futoshiki_output.txt", "w")
Function(Values)
