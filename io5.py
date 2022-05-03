# Читаем с файла матрицу
m = []
with open('data.txt', 'r') as file:
    for line in file:
        m.append(list(map(float, line.split())))

# Критерий Вальда (максимального пессимизма)
mins = []
for i in range(len(m)):
    min = [m[i][0], i, 0]
    for j in range(len(m[0])):
        if m[i][j] < min[0]:
            min = [m[i][j], i, j]
    mins.append(min)

WaldCriterion = mins[0]
for i in mins:
    if i[0] > WaldCriterion[0]:
        WaldCriterion = i
print("Критерий Вальда: " + str(WaldCriterion[0]) + " (" + str(WaldCriterion[1]) + ";" + str(WaldCriterion[2]) + ") ")

# Критерий Сейвиджа
maxs = []
for i in range(len(m[0])):
    localMax = m[0][i]
    for j in range(len(m)):
        if m[j][i] > localMax:
            localMax = m[j][i]
    maxs.append(localMax)
risksMatrix = []  # матрица рисков
for i in range(len(m)):
    localRisk = []
    for j in range(len(m[0])):
        localRisk.append(maxs[j] - m[i][j])
    risksMatrix.append(localRisk)
maxs = []
for i in range(len(risksMatrix)):
    max = [risksMatrix[i][0], i, 0]
    for j in range(len(risksMatrix[0])):
        if risksMatrix[i][j] > max[0]:
            max = [risksMatrix[i][j], i, j]
    maxs.append(max)
min = maxs[0]
for i in maxs:
    if i[0] < min[0]:
        min = i
print("Критерий Сейвиджа: " + str(min[0]) + " (" + str(min[1]) + ";" + str(min[2]) + ") ")