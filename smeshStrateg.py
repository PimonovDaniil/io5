import numpy as np
import matplotlib.pyplot as plt
import gauss


# Если m1 >= m2 значит true
def sravnMass(m1, m2):
    flag = True
    for i in range(len(m1)):
        if m1[i] < m2[i]:
            flag = False
            break
    return flag


def sravnMassVertikal(m, i1, i2):
    flag = True
    for i in range(len(m)):
        if m[i][i1] > m[i][i2]:
            flag = False
            break
    return flag


def sokrStrock(m):
    flag = True
    while flag:
        flag = False
        for i in range(len(m)):
            if not flag:
                for j in range(len(m)):
                    if i != j and sravnMass(m[i], m[j]):
                        flag = True
                        del m[j]
                        break
    return m


def sokrStrockVertikal(m):
    flag = True
    while flag:
        flag = False
        for i in range(len(m[0])):
            if not flag:
                for j in range(len(m[0])):
                    if i != j and sravnMassVertikal(m, i, j):
                        flag = True
                        for i2 in range(len(m)):
                            del m[i2][j]
                        break
    return m


# Читаем с файла матрицу
m = []
with open('data2.txt', 'r') as file:
    for line in file:
        m.append(list(map(float, line.split())))

# Если сокращается - значит сократится
for i in m:
    m = sokrStrock(m)
    m = sokrStrockVertikal(m)
print(m)

pointList = []
x = np.arange(-10, 10.01, 0.01)
# фигачим все крайнии точки
pointList.append([0, (1 - m[0][0] * 0) / m[1][0]])
pointList.append([0, (1 - m[0][1] * 0) / m[1][1]])
pointList.append([(1 - m[0][1] * 0) / m[0][0], 0])
pointList.append([(1 - m[1][1] * 0) / m[0][1], 0])
pointList.append(gauss.slau(2, [[m[0][0], m[1][0], 1], [m[0][1], m[1][1], 1]]))
flag = True
while flag:  # отсекаем точки что не подходят
    flag = False
    for i in range(len(pointList)):
        if (m[0][0] * pointList[i][0] + m[1][0] * pointList[i][1] < 1) or (
                m[0][1] * pointList[i][0] + m[1][1] * pointList[i][1] < 1):
            flag = True
            del pointList[i]
            break
min = pointList[0]
for i in pointList:
    if i[0] + i[1] < min[0] + min[1]:
        min = i
u = 1 / (min[0] + min[1])
p1 = min[0] * u
p2 = min[1] * u
print("p1: " + str(p1))
print("p2: " + str(p2))

pointList = []
# фигачим все крайнии точки
pointList.append([0, (1 - m[0][0] * 0) / m[0][1]])
pointList.append([0, (1 - m[1][0] * 0) / m[1][1]])
pointList.append([(1 - m[0][1] * 0) / m[0][0], 0])
pointList.append([(1 - m[1][1] * 0) / m[1][0], 0])
pointList.append(gauss.slau(2, [[m[0][0], m[0][1], 1], [m[1][0], m[1][1], 1]]))
flag = True
while flag:  # отсекаем точки что не подходят
    flag = False
    for i in range(len(pointList)):
        if (m[0][0] * pointList[i][0] + m[0][1] * pointList[i][1] < 1) or (
                m[1][0] * pointList[i][0] + m[1][1] * pointList[i][1] < 1):
            flag = True
            del pointList[i]
            break
# print(pointList)
min = pointList[0]
for i in pointList:
    if i[0] + i[1] < min[0] + min[1]:
        min = i
u = 1 / (min[0] + min[1])
q1 = min[0] * u
q2 = min[1] * u
print("q1: " + str(q1))
print("q2: " + str(q2))


plt.plot(x, (1 - m[0][0] * x) / m[1][0], x, (1 - m[0][1] * x) / m[1][1])
plt.show()
plt.plot(x, (1 - m[0][0] * x) / m[0][1], x, (1 - m[1][0] * x) / m[1][1])
plt.show()