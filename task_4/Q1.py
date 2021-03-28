# You are given a 2-d matrix of size n*m, an integer d which represents the direction of traversal(clockwise or anticlockwise ) and p which represents the starting index.
# You are required to print the given array in spiral form.For example the spiral from of the following array starting from position 0,0 in clockwise manner will be :
def answer(matrix,i,j,m,n):
    if i >= m or j >= n : return

    for p in range(j,n) :
        print(matrix[p][i],end=" ")

    for p in range(i+1,m) :
        print(matrix[n-1][p],end=" ")
    
    if ((m - 1) != i):
        for p in reversed(range(j,n-1)):
            print(matrix[p][m-1],end=" ")
    
    if ((n - 1) != i):
        for p in range(i,m-2):
            print(matrix[p][m-2],end=" ")

    answer(matrix, i + 1, j + 1, m - 1, n - 1)

if __name__ == "__main__":
    matrix = [] # save list of array len and array
    row,col,d,p = [int(i) for i in input().strip().split(" ")]
    for stri in range(row) : 
        matrix.append([int(i) for i in input().strip().split(" ")])
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]# testing
    # p,d = 4,2
    if p==1 : pass
    elif p == 2:matrix = [row[::-1] for row in matrix ]
    elif p == 3:matrix = [row[::-1] for row in matrix ][::-1]
    elif p == 4:matrix = [row for row in matrix ][::-1]
    # for clock or anti clockwise
    if d == 1 : matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    # for answers 
    answer(matrix,0,0,row,col)

