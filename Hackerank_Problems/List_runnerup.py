if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))



    biggest=arr[0]
    for i in arr:
        if i>biggest:
            biggest =i
   
    new_list=[x for x in arr if x != biggest]
    

    new_biggest=new_list[0]
    for i in new_list:
        if i>new_biggest:
            new_biggest=i
    print(new_biggest)

# In this prob we are suppose to print the secocnd largest number from a list

