# Given a two-dimensional array or matrix of size n*m, Write an algorithm to print the given matrix in a zigzag manner or in other words print all the diagonals from bottom to up in the matrix starting from the position p as stated below: For p=1, Start from 0,0 position For p=2, Start from 0,m-1 position For p=3, Start from n-1,m-1 position For p=4, Start from n-1,0 position
import itertools

def answer(p,matrix):
    matrix.pop(0)
    m = len(matrix[0])
    reverse_pattern = False
    if p== 1 :pass
    elif p == 2:
        [i.reverse() for i in matrix] 
    elif p == 3 :
        [i.reverse() for i in matrix] 
        matrix.reverse() 
        matrix = [[matrix[j][i] for j in range(m)] for i in range(m)] 

    elif p == 4 :
        reverse_pattern = True

    pattern = []
    for i in range(5):
        pattern.append(
            [matrix[j[0]][j[1]] for j in itertools.product(range(i+1),repeat = 2) if sum(j) == i and j[0] < m and j[1] < m ]
            )
    
    if reverse_pattern:
        pattern = reversed([reversed(i) for i in pattern])
    else:
        pattern = [reversed(i) for i in pattern]



    for i in pattern:
        for j in i:
            print(j,end=' ')
        print()


if __name__ == "__main__":
    test_cases = 4
    matrix = [
        [int(i) for i in input().strip().split(' ')],
        [int(i) for i in input().strip().split(' ')],
        [int(i) for i in input().strip().split(' ')],
        [int(i) for i in input().strip().split(' ')]
    ]
    for i in range(1,test_cases+1):
        answer(i,matrix.copy())
        print()

matrix = [
    [3 ,3, 1],
    [1 ,2, 3],
    [4 ,5 ,6],
    [7, 8, 9]
]
