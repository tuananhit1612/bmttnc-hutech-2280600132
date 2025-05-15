input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(",")]

rowNum = dimensions[0]
colNum = dimensions[1]

multilist = [[0 for j in range(colNum)] for i in range(rowNum)]
for i in range(rowNum):
    for j in range(colNum):
        multilist[i][j] = i * j
print(multilist)