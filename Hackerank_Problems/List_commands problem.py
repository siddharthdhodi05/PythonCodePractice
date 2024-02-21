if __name__ == '__main__':
    my_list = []
    N = int(input())  # Number of commands

    for _ in range(N):
        command = input().split()

        if command[0] == 'insert':
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(my_list)
        elif command[0] == 'remove':
            my_list.remove(int(command[1]))
        elif command[0] == 'append':
            my_list.append(int(command[1]))
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()
"""sample input:
10
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""
"""output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
