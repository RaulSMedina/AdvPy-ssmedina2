from math import pi#importing the number pi from the math lib.

class Amsterdam:
    def __init__(mate, v, t, r):#the start of the tour
        mate.v=v
        mate.t=t
        mate.r=r
        mate.rad_unit=1/mate.t*mate.r

    def quickpath(mate,v,r1,t,r2):#finds the quickes path to the certain landmark.
        if r1==0:
            return r2
        if r2==0: #already there so it is the faste route to stay there.
            return r1
        if v==t:
            return abs(r1-r2)*mate.rad_unit
        return min(abs(v-t)*(r/mate.t)*mate.r/mate.v*pi + (abs(r-r1)+abs(r-r2))*mate.rad_unit for r in range(0,mate.t+1))

def main():
    print(Amsterdam(*(lambda a,b,c: (int(a),int(b),float(c)))(*input().split())).quickpath(*map(int,input().split())))

if __name__ == "__main__":
    main()
#I used stack overflow and youtube to help me with this problem