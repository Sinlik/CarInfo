nList = [[1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E']]

newNList = [nList[i][j] for i in range(len(nList)) for j in range(len(nList[i]))]

print(newNList)