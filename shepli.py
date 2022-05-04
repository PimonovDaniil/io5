a1 = 8
b1 = 7
a2 = 4
b2 = 7
a3 = 9
b3 = 7


def getVarik(varik):
    a = 0
    b = 0
    oldProfit = 0
    res = [0, 0, 0]
    if varik[0] == "a":
        a += a1
        b += b1
        res[0] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[0] == "b":
        a += a2
        b += b2
        res[1] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[0] == "c":
        a += a3
        b += b3
        res[2] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[1] == "a":
        a += a1
        b += b1
        res[0] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[1] == "b":
        a += a2
        b += b2
        res[1] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[1] == "c":
        a += a3
        b += b3
        res[2] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[2] == "a":
        a += a1
        b += b1
        res[0] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[2] == "b":
        a += a2
        b += b2
        res[1] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    if varik[2] == "c":
        a += a3
        b += b3
        res[2] = (min(a, b) * 100) - oldProfit
        oldProfit = (min(a, b) * 100)
    return res


vectorShepli = [getVarik("abc"), getVarik("bac"), getVarik("acb"), getVarik("bca"), getVarik("cab"), getVarik("cba")]

a = 0
b = 0
c = 0
for i in range(len(vectorShepli)):
    print(vectorShepli[i])
    a += vectorShepli[i][0]
    b += vectorShepli[i][1]
    c += vectorShepli[i][2]
print("\nВывод:")
print([a/len(vectorShepli), b/len(vectorShepli), c/len(vectorShepli)])
