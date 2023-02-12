


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

        result = self.__generate_2s_compliment(list_)

        return result   


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

    
    def __generate_2s_compliment(self,list_):
        """Takes binary number(in list) as input and computes 2s compliment"""
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

        #Performing num1 - num2 
        neg_list2 = self.__convert_to_binary(-1*self.num2) 

        result = self.add_binary(self.list1,neg_list2)
        return result


    def multiply_binary(self,list1=None,list2=None):
        """Performs Binary Multiplication taking two lists and returns result"""
        result=[0]*32

        if(list1==None):
            list1 = self.list1
        
        if(list2==None):
            list2 = self.list2

        i1=len(list1)-1
        i2=len(list2)-1

        itr=31
        while i2>=0:
            rowres=[0]*32
            k=itr
            if list2[i2]==1:
                i1=len(list1)-1
                while i1>=0:
                    rowres[k]=list1[i1]
                    i1-=1
                    k-=1
                result = self.add_binary(result,rowres)    
            itr-=1
            i2-=1

        if (self.num1>0 and self.num2>0) or (self.num1<0 and self.num2<0):
            return result    

        return self.__generate_2s_compliment(result)   


    def divide_binary(self):
        """Performs Binary Division (num1/num2) and returns result"""
        result=[]
        itr=0
        cur_divi=0

        while(itr<len(self.list1)):
            cur_divi = 2*cur_divi + self.list1[itr]
            if(cur_divi>=self.num2):
                cur_divi=cur_divi-self.num2
                result.append(1)
            else:
                result.append(0) 
            itr+=1

        if (self.num1>0 and self.num2>0) or (self.num1<0 and self.num2<0):
            return result    

        return self.__generate_2s_compliment(result)   

    
    def mod_binary(self,modVal):
        pass


    def factorial_binary(self,num=None):
        """Performs Factorial on Binary Number"""

        global list_
        list_ = None
        if(num == None):
            num = self.num1
            list_ = self.list1
        else:
            list_ = self.__convert_to_binary(num)

        if(num == 0):
            return self.__convert_to_binary(1)

        if(num < 0):
            print("Invalid Number for Factorial!")
            return None
        
        result = self.__convert_to_binary(1)
        for i in range(1,num+1):
            result = self.multiply_binary(result,self.__convert_to_binary(i))

        return result


    def power_binary(self):
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


        
def main():
    num1 = int(input("Enter First Number:"))
    num2 = int((input("Enter Second Number:")))

    # Creating BinaryArthimetic Object
    binary_math = BinaryArithmetic(num1,num2)

    print("Performing Addition:")
    result_add = binary_math.add_binary()
    print(result_add,'\n')

    print("Performing Subtraction:")
    result_subtract = binary_math.sub_binary()
    print(result_subtract,'\n')

    print("Performing Multiplication:")
    result_multiply = binary_math.multiply_binary()
    print(result_multiply,'\n')

    print("Performing Division:")
    result_divide = binary_math.divide_binary()
    print(result_divide,'\n')

    print("Performing Factorial:")
    result_fact = binary_math.factorial_binary()
    print(result_fact,'\n')


 
main()