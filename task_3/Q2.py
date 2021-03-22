# You are given an array consisting of N integers. In every operation you perform, you are allowed to choose any 2 elements from the array and replace both of them with a new number in the array which is equal to the sum of both numbers . The position where you insert this new element does not matter . For example, from the array [5,2,1] you can have the following arrays in possibility: [5,3], [7,1] and [2,6].
# Your task is to find the maximum possible number of elements divisible by 4 that are in the array after performing the above operation any(possibly, zero) number of times.

def answer(length,arr):
    divisible_by_4 = 0

    # create the remender list
    remender_list = [i%4 for i in arr]

    # create dict of friquency
    frequency = {0:0,1:0,2:0,3:0}
    for value in remender_list:
        frequency[value] += 1

    # for 0
    divisible_by_4 += frequency[0]
    frequency[0] = 0

    # for 2 
    divisible_by_4 += frequency[2]//2
    frequency[2] %= 2

    # for 3 and 1 pair
    min_pair = min(frequency[3],frequency[1])
    divisible_by_4 += min_pair
    frequency[3] -= min_pair
    frequency[1] -= min_pair

    # four 3's
    divisible_by_4 += frequency[3]//4
    frequency[3] %= 4

    # for 1
    divisible_by_4 += frequency[1]//4
    frequency[1] %= 4

    # one and 2 condition
    if frequency[2] and frequency[1] == 2 :
            divisible_by_4 += 1

    return divisible_by_4


if __name__ == "__main__":
    test_case_list = [] # save list of array len and array
    total_test_case = int(input())
    for _ in range(total_test_case):
        test_case_list.append([
            int(input()),
            [int(i) for i in input().strip().split(' ')]
        ])

    for i in test_case_list:
        print(answer(*i))
