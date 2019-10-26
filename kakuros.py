from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model

file = open("kakuro_input.txt", 'r')
lines = file.readlines()
dict = []
for i in lines:
    linesplit = i.split(",")
    for x in linesplit:
        dict.append(x)
file.close()


def kakuro_solver(sums,kakuros_Output):
    CpModel = cp_model.CpModel()
    CpSolver = cp_model.CpSolver()

    # Variables
    x1 = CpModel.NewIntVar(1, 9, 'x1')
    x2 = CpModel.NewIntVar(1, 9, 'x2')
    x3 = CpModel.NewIntVar(1, 9, 'x3')

    y1 = CpModel.NewIntVar(1, 9, 'y1')
    y2 = CpModel.NewIntVar(1, 9, 'y2')
    y3 = CpModel.NewIntVar(1, 9, 'y3')

    z1 = CpModel.NewIntVar(1, 9, 'z1')
    z2 = CpModel.NewIntVar(1, 9, 'z2')
    z3 = CpModel.NewIntVar(1, 9, 'z3')

    CpModel.Add(x1 + x2 + x3 == int(sums[3]))
    CpModel.Add(y1 + y2 + y3 == int(sums[4]))
    CpModel.Add(z1 + z2 + z3 == int(sums[5]))
    CpModel.Add(x1 + y1 + z1 == int(sums[0]))
    CpModel.Add(x2 + y2 + z2 == int(sums[1]))
    CpModel.Add(x3 + y3 + z3 == int(sums[2]))

    Row1 = [x1, x2, x3]
    Row2 = [y1, y2, y3]
    Row3= [z1, z2, z3]
    Col1 = [x1, y1, z1]
    Col2 = [x2, y2, z2]
    Col3 = [x3, y3, z3]

    CpModel.AddAllDifferent(Row1)
    CpModel.AddAllDifferent(Row2)
    CpModel.AddAllDifferent(Row3)
    CpModel.AddAllDifferent(Col1)
    CpModel.AddAllDifferent(Col2)
    CpModel.AddAllDifferent(Col3)

    status = CpSolver.Solve(CpModel)
    if status == cp_model.FEASIBLE:
        kakuros_Output.writelines(
            str(dict[3]) + "," + str(CpSolver.Value(x1)) + "," + str(CpSolver.Value(x2)) + "," + str(CpSolver.Value(x3)) + "\n")
        kakuros_Output.writelines(
            str(dict[4].strip()) + "," + str(CpSolver.Value(y1)) + "," + str(CpSolver.Value(y2)) + "," + str(CpSolver.Value(y3)) + "\n")
        kakuros_Output.writelines(
            str(dict[5].strip()) + "," + str(CpSolver.Value(z1)) + "," + str(CpSolver.Value(z2)) + "," + str(CpSolver.Value(z3)) + "\n")


kakuros_Output = open("kakuro_output.txt", 'w')
line = lines[0].strip().replace(" ", "")
kakuros_Output.writelines("x" + "," + str(line) + "\n")

kakuro_solver(dict, kakuros_Output)
