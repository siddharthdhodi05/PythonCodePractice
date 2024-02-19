class list:
    def __init__(self,L):
        self.__sum=L
        self.sum(self.__sum)

    def sum(self,x):
        z=0
        for i in x:
            z=z+i
        print("Sum of items in list is"+" ",z)

f=[1,2,3,6]
o=list(f)
