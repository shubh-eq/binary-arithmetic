


def add_binary(num1,num2):
    result = []
    

def convertPos(n):
    l = []
    while n!=0:
        l.append(n%2)
        n=n//2
    l.reverse()
    return l

def convertNeg(n):
    lis=convertPos(n*-1)
    for i in range(len(lis)):
        lis[i]=(lis[i]+1)%2
    t=len(lis)-1
    c=1
    while t!=len(lis) and c==1:
        if lis[t]==0:
            c=0
            lis[t]=1
        t=t+1  
    return lis      


def main():
    num1 =-7 #int(input("Enter First Number:"))
    num2 = 22#int((input("Enter Second Number")))
    l1=[]
    l2=[]
    # print(convertPos(num1))
    print(convertNeg(num1))

    #print(l1)

main()