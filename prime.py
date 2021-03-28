#Take an input n and print all prime numbers less than equal to n.
def p(x):
    l=list()
    if x<=1:
        pass
    else:
        for i in range(2,x+1):
            f=1
            for j in range(2,(int(i**0.5)+1)):
                if (i%j)==0:
                    f=0
                    break
            if(f==1):
                l.append(i)
    return l
                
n=int(input())
print(p(n))
    
