class factorial:
    def __init__(self,n):
        self.__number=n
        self.ans=self.func(self.__number)
        print(self.ans)
    def func(self,no):
        if no==0:
            return 1
        else:
            return no*self.func(no-1)
            
