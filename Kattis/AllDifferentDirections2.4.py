from math import radians,sin,cos,sqrt #pulls math tools from math

def keepup(v1, order, answer):
    if order=='turn':
        v1[2]+=answer
    else:
        v1[0]+=answer * cos(radians(v1[2]))
        v1[1]+=answer * sin(radians(v1[2]))


def squared(v2, v3):#retrun the squred number of the two variables
    return (v2[0] - v3[0])**2 + (v2[1] - v3[1])**2


def sloution(var):#give me the soultion for the problem
    sumy=0.0
    sumx=0.0
    collect=[]
    for i in range(var):
        var1=input().split()
        postive=list(map(float, var1[:2]))
        cmd=var1[2:]
        it=iter(cmd)
        next(it)
        postive.append(float(next(it)))
        for j in range(len(cmd) // 2 - 1):
            keepup(postive, next(it), float(next(it)))
        collect.append(tuple(postive[:2]))
        sumy+=postive[1]
        sumx+=postive[0]
    ave=(sumx / len(collect), sumy / len(collect))
    dis=0
    for p in collect:
        d=squared(p, ave)
        if d > dis:
            dis=d
    print("{:.6f} {:.6f} {:.6f}".format(ave[0], ave[1], sqrt(dis)))


if __name__ == '__main__':
    while True:
        n=int(input())
        if n==0:
            break
        sloution(n)
#I got help from stack overflow