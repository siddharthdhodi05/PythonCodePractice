
#In this problem we are asked to convert a tuple from user input to a hash value

if __name__ == '__main__':
    n = int(input())
    integer_tuple = map(int, input().split())
    integer_tuple=tuple(integer_tuple)
    hash_value =hash(integer_tuple)
    print(hash_value)
