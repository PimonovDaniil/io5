import random


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
        if m[i][i1] >= m[i][i2]:
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
                        # del m[j]
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
