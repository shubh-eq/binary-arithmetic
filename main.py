


def add_binary(num1,num2):
    result = []
    

def convertPos(n):
    l = []
    while n!=0:
        l.append(n%2)
        n=n//2
    l.reverse()
    l_32 = [0]*32
    n_len = len(l) -1
    i = 0
    while(i<=n_len):
        l_32[31-n_len+i] = l[i]
        i+=1

    return l_32

def convert_to_binary(n):
    lis=convertPos(abs(n))
    if(n>=0):
        return lis

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
    num1 = 7 #int(input("Enter First Number:"))
    num2 = 22 #int((input("Enter Second Number")))
    list1 = convert_to_binary(num1)
    list2 = convert_to_binary(num2)

    result_add = add_binary(list1,list2)



main()