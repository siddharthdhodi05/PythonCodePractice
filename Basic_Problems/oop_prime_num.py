class prime:
    def __init__(self):
        self.__num=int(input("Please enter the number"))
        self.is_prime(self.__num)
    def is_prime(self,n):
        if n<2:
            print("not prime")
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                print("not prime")
            else:
                print("its prime")
