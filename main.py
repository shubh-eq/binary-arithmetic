

class BinaryArithmetic:
    """Arithmetic of two Binary Numbers"""
    num1 = None
    num2 = None

    #Storing input numbers in list as binary format
    list1 = []
    list2 = []

    def __convert_to_binary(self,n):
        """Takes a number as input and converts to binary"""

        list_= self.__convertion_helper(abs(n))

        #Returns if input is positive
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


    def __convertion_helper(self,n):
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


    #Constructor    
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2

        self.list1 = self.__convert_to_binary(num1)
        self.list2 = self.__convert_to_binary(num2)

        print("1st Input:",self.list1)
        print("2nd Input:",self.list2)   

    
    def add_binary(self,list1 = None,list2 = None):
        """Performs Binary Addition taking two lists and returns result"""
        if(list1 == None):
            list1 = self.list1
        
        if(list2 == None):
            list2 = self.list2

        itr=31
        carry=0

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

    
    def sub_binary(self):
        """Performs Binary Addition taking two lists and returns result"""
        neg_list2 = self.__convert_to_binary(-1*self.num2)

        result = self.add_binary(self.list1,neg_list2)
        return result


    def multiply_binary(self):
        pass

    def divide_binary(self):
        pass


    def convert_binary_to_decimal(self,list_):
        """Takes a binary number as list and converts to decimal"""
        for i in range(0,len(list_)):
            list_[i] = str(list_[i])

        binary = int("".join(list_))
        decimal, i = 0, 0

        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1

        return decimal




def multiply_binary_numbers(n1,n2):
    """Takes two binary numbers and multiplies them"""

    result=[0]*32
    num1 = convert_to_binary(n1)
    num2 = convert_to_binary(n2)

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
            result=add_binary_helper(result,rowres)    
        indr-=1
        i2-=1
    return result      



def add_binary_helper(list1,list2):
    """Takes two lists (binary) as input and performs addition"""

    itr=31
    carry=0
    
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



def main():
    num1 = int(input("Enter First Number:"))
    num2 = int((input("Enter Second Number:")))

    #Creating BinaryArthimetic Object
    binary_math = BinaryArithmetic(num1,num2)

    print("Performing Addition:")
    result_add = binary_math.add_binary()
    print(result_add,'\n')

    print("Performing Subtraction:")
    result_subtract = binary_math.sub_binary()
    print(result_subtract,'\n')

    # print("Performing Multiplication:\n")
    # result_multiply = multiply_binary_numbers(num1,num2)
    # print(result_multiply,'\n')


main()