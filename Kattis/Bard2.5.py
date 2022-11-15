
var1=int(input())
var2=int(input())
songvar=[set() for i in range(var1 + 1)]
#list of variables above
for i in range(var2):
    lib=list(map(int, input().split()))[1:]#libeary of music
    if 1 in lib:#checks to see if the song is new or not
        for j in lib:
            songvar[j].add(i)
    else:
        new=set()
        for j in lib:
            new|=songvar[j]
        for j in lib:
            songvar[j]=new.copy()


list(map(lambda v1: print(v1[0]), filter(lambda v2: v2[0] > 0 and len(v2[1]) == len(songvar[1]), enumerate(songvar))))
#used stack over flow to help me with this problem