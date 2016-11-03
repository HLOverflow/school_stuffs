# python 2
# 
# Question
# Given c=6, find the set of integers from 1 to 6 where the sum of integers is 6
# eg.
# 1 2 3
# 1 5
# 2 4
# 6
# find the sets of integers when c=10

# root node of the graph = 0
def sumToC(s, c):
    if sum(s)==c:       # solution found
        print s[1:]
    elif sum(s)>c:      # impossible to find solution
        pass
    else:               # possible solutions
        #valid choices (predecessor + 1) to c
        choices = [i for i in range(s[-1]+1, c+1)]  
        for j in choices:
            s.append(j)
            sumToC(s, c)    # depth first search
            s.remove(j)     # backtrack when solution found / impossible

print "when c is 6"
sumToC([0], 6)

print
print "when c is 10"
sumToC([0], 10)
            
        
