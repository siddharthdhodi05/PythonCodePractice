class checker:
    def __init__(self,string):
        self._string=string
        self.is_palin(self._string)
    def is_palin(self,n):
        n = "".join(char.lower() for char in n if char.isalnum())
        if n==n[::-1]:
            print(self._string, " " + "is a Palindrome")
        else:
            print(self._string, " " + "is not a Palindrome")
obj1=checker("akjda")


obj2=checker("did")
