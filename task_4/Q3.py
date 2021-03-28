# As usual Leonard is being mocked by Sheldon for being the stupidest person in his house and to prove this he gives Leonard a task. He gives Leonard a string S, and leonard is allowed to choose exactly one substring from S and shift all its characters 1 backward. Example- ‘a’->’z, ‘c’->'b' , ‘z’->’y’ and so on. He is allowed to perform this operation only once and have to find out the lexicographically minimum string that can be obtained from S. Can you help Leonard?
def answer(string):
    new_string = ""
    for index,letter in enumerate(string) :
        if ord(letter)==97:
            new_string += string[index:]    
            break # 97 == a
        else:
            new_string += chr(ord(letter)-1) 
    return new_string

if __name__ == "__main__":
    test_case_list = [] # save list of array len and array
    total_test_case = int(input())
    for _ in range(total_test_case) :
        test_case_list.append(input().strip())    
    # take input
    for stri in test_case_list : 
        print(answer(stri))