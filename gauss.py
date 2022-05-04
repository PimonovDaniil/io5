import numpy

def slau(r, mat):
    #Прямой ход (преобразование матрицы к треугольному виду)
    M = numpy.array(mat)
    # print("Исходная матрица:")
    # print(M, end="\n\n")

    #print(M[0][0])
    M[0] /= M[0][0]

    precision = 0.1**(10)
    if abs(M[0][0]) < precision:
        raise IOError("Нулевой элемент на диагонали. Ошибка!")

    # print("Формируем треугольную матрицу:")
    # print(M, end="\n\n")
    for i in range(1,r):
        for j in range(i, r):
            M[j] -= (M[i-1]*M[j][i-1])
        #print(i)
        M[i] /= M[i][i]
        # print("Формируем треугольную матрицу:")
        # print(M, end="\n\n")

        if abs(M[i][i]) < precision:
            raise IOError("Нулевой элемент на диагонали. Ошибка!")

    # обратный ход
    result = [0]*r
    for i in range(r-1,-1,-1):
        memory  = M[i][r]
        for j in range(i+1, r):
            memory -= M[i][j] * result[j]
        result[i] = memory
        # print("Вычисляем корни:")
        # print(result, end="\n\n")

    # считаем точность
    nevyzka = []
    M = numpy.array(mat)
    for i in range(r):
        sum = 0.0
        for j in range(r):
            sum += M[i][j]*result[j]
        nevyzka.append(sum-M[i][r])
    # print("Вектор невязки: ", nevyzka)
    # print("Норма вектора невязки: ", numpy.linalg.norm(nevyzka),end="\n\n")
    return result

def determinant(r, mat):
    # Прямой ход (преобразование матрицы к треугольному виду)
    M = numpy.array(mat)
    determinant = M[0][0]
    M[0] /= M[0][0]

    precision = 1 ** (-10)
    if abs(M[0][0]) < precision:
        raise IOError("Нулевой элемент на диагонали. Ошибка!")
    for i in range(1, r):
        for j in range(i, r):
            M[j] -= (M[i - 1] * M[j][i - 1])
        determinant *= M[i][i]
        M[i] /= M[i][i]

        if abs(M[i][i]) < precision:
            raise IOError("Нулевой элемент на диагонали. Ошибка!")
    return determinant

def obratnMatrix(r, mat):
    def obrHod(M):
        result = [0] * r
        for i in range(r - 1, -1, -1):
            memory = M[i][r]
            for j in range(i + 1, r):
                memory -= M[i][j] * result[j]
            result[i] = memory
        return result

    #если матрица не квадратная, обрезаем её
    if len(mat[0]) > r:
        for i in range(len(mat)):
            mat[i].pop()

    M = numpy.array(mat)

    # print("Исходная матрица:")
    # print(M, end="\n\n")

    #генерируем единичную матрицу
    EdMatrix = []
    for i in range(r):
        memory = [0] * r
        memory[i]=1
        EdMatrix.append(memory)
    res = numpy.array([[]]*r)
    EdMatrixForVyzka = numpy.array(EdMatrix)

    #считаем треугольную матрицу и преобразуем единичную
    M2 = numpy.array(mat)
    for g in range(len(EdMatrix)):
        EdMatrix[g][0] /= M2[0][0]
    M2[0] /= M2[0][0]
    precision = 0.1 ** (10)
    if abs(M2[0][0]) < precision:
        raise IOError("Нулевой элемент на диагонали. Ошибка!")
    # print("Формируем треугольную матрицу:")
    # print(M2, end="\n\n")
    for i in range(1, r):
        for j in range(i, r):
            for g in range(len(EdMatrix)):
                EdMatrix[g][j] -= (EdMatrix[g][i-1] * M2[j][i - 1])
            M2[j] -= (M2[i - 1] * M2[j][i - 1])
        for g in range(len(EdMatrix)):
            EdMatrix[g][i] /= M2[i][i]
        M2[i] /= M2[i][i]
        # print("Формируем треугольную матрицу:")
        # print(M2, end="\n\n")
        if abs(M2[i][i]) < precision:
            raise IOError("Нулевой элемент на диагонали. Ошибка!")
    # print("Изменённая единичная матрица:")
    # print(numpy.array(EdMatrix), end="\n\n")
    for i in range(r):
        memory = numpy.array([EdMatrix[i]])
        mem = numpy.array([obrHod(numpy.concatenate((M2, memory.T), axis=1))])
        res = numpy.concatenate((res, mem.T), axis=1)

    # считаем точность
    nevyzka = numpy.dot(numpy.array(mat),res)-EdMatrixForVyzka
    # print("Матрица невязки (AX – E):\n",nevyzka,end="\n\n")
    # print("Норма матрицы невязки: ", numpy.linalg.norm(nevyzka), end="\n\n")
    return res

