


def add_binary(num1,num2):
    pass




def convertPos(n,l):
    while n!=0:
        l.append(n%2)
        n=n/2

def convertNeg(n,lis):
    convertPos(n,lis)
    for i in range(len(lis)):
        lis[i]=(lis[i]+1)%2
    t=0
    c=1
    while t!=len(lis) and c==1:
        if lis[t]==0:
            c=0
            lis[t]=1
        t=t+1        


def main():
    num1 = int(input("Enter First Number:"))
    num2 = int((input("Enter Second Number")))
    l1=[]
    l2=[]

