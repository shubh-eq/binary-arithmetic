def multiply_binary(n1,n2):
    result=[0]*32
    num1 = convert_to_binary(abs(n1))
    num2 = convert_to_binary(abs(n2))

    i2=len(num2)-1
    i1=len(num1)-1
    indr=31
    while i2>=0:
        rowres=[0]*32
        k=indr
        if num2[i2]==1:
            i1=len(num1)-1
            while i1>=0:
                rowres[k]=num1[i1]
                i1-=1
                k-=1
            result=add_binary_numbers(result,rowres)    
        indr-=1
        i2-=1

    if (n1>0 and n2>0) or (n1<0 and n2<0):
        return result    

    return twoscompliment(result)      



def add_binary_numbers(list1,list2):
    """Takes two numbers as input and performs addition"""

    #Converts to binary and gets results in list
    # list1 = convert_to_binary(num1)
    # list2 = convert_to_binary(num2)

    itr=31
    carry=0
    # print("1st Input:",list1)
    # print("2nd Input:",list2)

    result=[]
    while itr>=0:
        t = list1[itr] + list2[itr] + carry 
        if (t==0) or (t==1):
            result.append(t)
            carry=0
        elif t==2:
            result.append(0)
            carry=1
        else:
            result.append(1)
            carry=1
        itr=itr-1

    result.reverse()
    return result


def subtract_binary_numbers(num1,num2):
    """Takes two numbers as input and performs Subtraction: num1-num2"""
    num2 = -1*num2

    result = add_binary_numbers(num1,num2)
    return result


def convert_binary_to_decimal(num):
    """Takes a binary number as list and converts to decimal"""
    binary = int("".join(num))
    decimal, i = 0, 0

    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    return decimal



def convertion_helper(n):
    """Helper function to convert into binary from decimal"""
    list_ = []
    while n!=0:
        list_.append(n%2)
        n=n//2
    list_.reverse()

    list_32 = [0]*32

    #Creating 32-bits length list
    list_len = len(list_) -1
    i = 0
    while(i<=list_len):
        list_32[31-list_len+i] = list_[i]
        i+=1

    return list_32

def twoscompliment(list):
    #One's Compliment (Inverting Bits)
    for i in range(len(list)):
        list[i]=(list[i]+1)%2
    
    itr=len(list)-1
    carry=1
    while itr>=0 and carry==1:
        if list[itr]==0:
            carry=0
            list[itr]=1
        else:
            list[itr]=0    
        itr=itr-1
    return list    


def convert_to_binary(n):
    """Takes a number as input and converts to binary"""

    list_=convertion_helper(abs(n))

    #Returns if input is positive
    if(n>=0):
        return list_
        
    return twoscompliment(list_)    


def main():
    num1 = int(input("Enter First Number:"))
    num2 = int((input("Enter Second Number:")))

    # print("Performing Addition:\n")
    # result_add = add_binary_numbers(num1,num2)
    # print(result_add,'\n')

    # print("Performing Subtraction:\n")
    # result_subtract = subtract_binary_numbers(num1,num2)
    # print(result_subtract,'\n')
    print(multiply_binary(num1,num2))

main()