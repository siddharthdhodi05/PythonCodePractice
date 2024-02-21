if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    newlist=[[i,j,k] for i in range(0,x+1)  for j in range(0,y+1) for k in range(0,z+1)]
    print(newlist)
    condi=[sublist for sublist in newlist if sum(sublist)!=n]
    print(condi)

    """
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, .
Please use list comprehensions rather than multiple loops, as a learning exercise.

Example

1
2
3
2


All permutations of  are:
.
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 1, 0],
[0, 1, 1], [0, 1, 2], [0, 1, 3], [0, 2, 0], [0, 2, 1],
[0, 2, 2], [0, 2, 3], [1, 0, 0], [1, 0, 1], [1, 0, 2],
[1, 0, 3], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 1, 3],
[1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3]]
Print an array of the elements that do not sum to .
[[0, 0, 0], [0, 0, 1], [0, 0, 3], [0, 1, 0], [0, 1, 2],
[0, 1, 3], [0, 2, 1], [0, 2, 2], [0, 2, 3], [1, 0, 0],
[1, 0, 2], [1, 0, 3], [1, 1, 1], [1, 1, 2], [1, 1, 3],
[1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3]]

Input Format

Four integers  and , each on a separate line.

Constraints

Print the list in lexicographic increasing order.
"""
