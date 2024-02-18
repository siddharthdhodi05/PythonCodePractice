class Count:
    def __init__(self, string):
        self.__string = string
        self.counter(self.__string)

    def counter(self, n):
        vowels = ["a", "e", "i", "o", "u"]
        counter1 = 0
        counter2 = 0
        for i in n:
            if i in vowels:
                counter1 += 1
            else:
                counter2 += 1
        
        print("The Number of vowels in string are:", counter1)
        print("The Number of consonants in string are:", counter2)

a = Count("siddharth")
