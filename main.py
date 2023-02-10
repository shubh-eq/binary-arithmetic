

def add_binary_numbers(num1,num2):
    """Takes two numbers as input and performs addition"""

    #Converts to binary and gets results in list
    list1 = convert_to_binary(num1)
    list2 = convert_to_binary(num2)

    itr=31
    carry=0
    print("1st Input:",list1)
    print("2nd Input:",list2)

    result=[]
    while itr>=0:
        t=list1[itr]+list2[itr]+carry
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

    n_len = len(list_) -1
    i = 0
    while(i<=n_len):
        list_32[31-n_len+i] = list_[i]
        i+=1

    return list_32

def convert_to_binary(n):
    """Takes a number as input and converts to binary"""
    list_=convertion_helper(abs(n))

    if(n>=0):
        return list_

    #One's Compliment (Inverting Bits)
    for i in range(len(list_)):
        list_[i]=(list_[i]+1)%2

    #Two's Compliment (Adding one)
    itr=len(list_)-1
    carry=1
    while itr>=0 and carry==1:
        if list_[itr]==0:
            carry=0
            list_[itr]=1
        else:
            list_[itr]=0    
        itr=itr-1

    return list_      


def main():
    num1 = 4 #int(input("Enter First Number:"))
    num2 = -2 #int((input("Enter Second Number")))

    result_add = add_binary_numbers(num1,num2)
    print(result_add,'\n')

    result_subtract = subtract_binary_numbers(num1,num2)
    print(result_subtract,'\n')


main()