# You are given an array of n integers. You want to make all the numbers in this array as odd. In one operation you can select two indices i and j (i≠j) and replace ai with (ai+aj).

def answer(arr):
    bin_int = 0
    for i in arr:
        if i%2 == 0:
            bin_int += 1
    
    if bin_int == len(arr):
        return -1
    else :
        return bin_int


if __name__ == "__main__":
    test_case_list = []
    total_test_case = int(input())
    for _ in range(total_test_case):
        input()
        test_case_list.append([int(i) for i in input().strip().split(' ')])

    # print(test_case_list)
    for i in test_case_list:
        print(answer(i))
