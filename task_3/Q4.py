# You are given with an array of n integers. You have to find the sum of all prime numbers present in the array and then have to check whether all the digits in that sum are unique or not.

def answer(arr):
    prime_list = []
    for num in arr:
        if num > 1 :
            for i in range(2, num):
                if (num % i) == 0:
                    break # break out of loop if factor exists
            else : prime_list.append(num)
    if len(prime_list) == len(set(prime_list)):
        return "YES"
    return "NO"

if __name__ == "__main__":
    input()
    _return  = answer([int(i) for i in input().strip().split(' ')])
    print(_return)
