from __future__ import print_function

# adjacent list
Graph = {'s':{'u':10, 'x':5},       \
         'u':{'x':2, 'v':1},        \
         'x':{'u':3, 'y':2, 'v':9}, \
         'v':{'y':4},               \
         'y':{'s':7, 'v':6}         \
        }
d = {key:999 for key in Graph}
S = {key:0 for key in Graph}
pi = {key:None for key in Graph}

Q = ['s']
d['s']=0

def dequeue():
    global Q
    return Q.pop(0)

def enqueue(item):
    global Q
    for i in item:
        if (not i in Q) and S[i]==0:  #don't want duplicates and only unqueue those not in tree
            Q.extend(i)
            print ("Enqueued: ", i)
    
def sortviaEdgeCost(v):
    global Graph
    invDict = {v:k for k,v in Graph[v].items()}
    array = list(invDict.keys())
    array = sorted(array)
    neighbours_sorted = [invDict[i] for i in array]
    return neighbours_sorted

def sortViaD(l):
    global d
    invD = {v:k for k,v in d.items()}
    tmp = [d[node] for node in l]
    tmp = sorted(tmp)
    sortedViaD = [invD[j] for j in tmp]
    return sortedViaD

while(Q):
    print ("Q1: ", Q)
    u = dequeue()
    S[u]=1
    print ("chosen(dequeued): ", u)
    tmp = sortviaEdgeCost(u)
    enqueue(tmp)
    print ("Q2: ", Q)
    for v in Q:
        if(v in Graph[u]):                  # check if edge uv exist
            if(S[v]==0 and d[v] > (d[u] + Graph[u][v])):
                d[v]=d[u] + Graph[u][v]     # take the smaller cost
                pi[v] = u                   

    Q = sortViaD(Q)                         # sort queue by the distance from source

    print ("--- after processing ---")
    print ("Q: ", Q)
    print ("S: ", S)
    print ("d: ", d)
    print ("pi: ", pi)
    print ("-------------------")
        
def printPaths(dst):
    global pi
    if pi[dst]:
        printPaths(pi[dst])
        print ("-> ", dst, end='')
    else:
        print (dst, end='')


for vertex in Graph:
    print ("\n-------")
    print ("s to", vertex)
    print ("distance: ", d[vertex])
    printPaths(vertex)
