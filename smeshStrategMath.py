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


def step(mNew):
    mins = min(mNew[len(mNew)-1])
    if mins < 0:
        bazisID = 0
        for i in range(len(mNew[0])):
            if mins == mNew[len(mNew)-1][i]:
                bazisID = i
                break
        if mNew[0][len(mNew[0])-1]/mNew[0][bazisID] < mNew[1][len(mNew[1])-1]/mNew[1][bazisID]:
            bazis = mNew[0][bazisID]
            for i in range(len(mNew[0])):
                mNew[0][i] /= bazis
            multiply = mNew[1][bazisID]
            for i in range(len(mNew[1])):
                mNew[1][i] -= (mNew[0][i] * multiply)
            multiply = mNew[2][bazisID]
            for i in range(len(mNew[2])):
                mNew[2][i] -= (mNew[0][i] * multiply)

        else:
            bazis = mNew[1][bazisID]
            for i in range(len(mNew[1])):
                mNew[1][i] /= bazis
            multiply = mNew[0][bazisID]
            for i in range(len(mNew[0])):
                mNew[0][i] -= (mNew[1][i]*multiply)
            multiply = mNew[2][bazisID]
            for i in range(len(mNew[2])):
                mNew[2][i] -= (mNew[1][i] * multiply)
        # print(mNew)
        return mNew
    else:
        return False






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

mNew = [[0, m[0][0], m[0][1], 1, 0, 1], [0, m[1][0], m[1][1], 0, 1, 1], [1, -1, -1, 0, 0, 0]]
flag = True
while flag:
    flag = False
    mNew = step(mNew)
    if min(mNew[len(mNew)-1])<0:
        flag = True
for i in mNew:
    print(i)

u = 1/mNew[len(mNew)-1][len(mNew[0])-1]
q1 = mNew[0][len(mNew[0])-1]*u
q2 = mNew[1][len(mNew[0])-1]*u
print("u: "+str(u))
print("q1: "+str(q1))
print("q2: "+str(q2))


# Читаем с файла матрицу
m = []
with open('data2.txt', 'r') as file:
    for line in file:
        m.append(list(map(float, line.split())))
# Если сокращается - значит сократится
for i in m:
    m = sokrStrock(m)
    m = sokrStrockVertikal(m)
m[0][1], m[1][0] = m[1][0], m[0][1]
# print(m)
mNew = [[0, m[0][0], m[0][1], 1, 0, 1], [0, m[1][0], m[1][1], 0, 1, 1], [1, -1, -1, 0, 0, 0]]
mNew = step(mNew)
mNew = step(mNew)
# for i in mNew:
#     print(i)

u = 1/mNew[len(mNew)-1][len(mNew[0])-1]
p1 = mNew[0][len(mNew[0])-1]*u
p2 = mNew[1][len(mNew[0])-1]*u
print("p1: "+str(p1))
print("p2: "+str(p2))

