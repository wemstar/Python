'''
Created on 25-10-2012

@author: wemstar
'''
def cout():
    
    x=[int(i) for i in input().rsplit()]

    
    y=x[1::2]
    x=x[::2]
    z=[]
    for j,k in zip(x,y):
        z.append([j,k])
    return z
def licz_pole(czarny,szary):
    c=0
    s=0
    for x in range(len(czarny)-1):
        c=c+czarny[x][0]*czarny[x+1][1]-czarny[x][1]*czarny[x+1][0]
    for x in range(len(szary)-1):
        s=s+szary[x][0]*szary[x+1][1]-szary[x][1]*szary[x+1][0]
    c=abs(c)
    s=abs(s)
    
    s=c*5+(s-c)*3
    return s
        
        
            
def main():
    n=int(input())
    s=[]
    for x in range(n):
        x=x
        czarny=cout()
        szary=cout()
        s.append(licz_pole(czarny,szary))
    print()
    [print(x) for x in s]
main()
    