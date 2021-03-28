# In a class of n students, there are 5 subjects in total(Maths, Physics, Chemistry, Computer Science, English) and each subject is marked out of 100. Each student has a name and a unique admission number. Your teacher has assigned you with a task in which you have to sort the names of students in the following priority order: Students with the highest total marks in all 5 subjects are ranked first If some students have equal total marks, then sort them according to the total marks obtained in physics, chemistry and maths. If some students have the same total marks in physics, chemistry and maths then sort according to their name. If few students have the same name also, then sort them according to their admission numbers.

def answer(dic):
    # Students with the highest total marks in all
    dic.sort(key = lambda k : sum(k[2:]),reverse=True)

    # If some students have the same total marks in physics, chemistry and maths then sort according to their name
    if len(set([sum(i[2:]) for i in dic])) != len([sum(i[2:]) for i in dic]):
        dic = sorted(dic,key = lambda k : k[0] if [sum(i[2:]) for i in dic].count(sum(k[2:])) > 1 else '')
    # If few students have the same name also, then sort them according to their admission numbers.
    if len(set([i[1] for i in dic])) != len([i[1] for i in dic]):
        dic = sorted(dic ,key = lambda k : k[1] if [i[1] for i in dic].count(k[1]) else 0 )

    # if total is same for some of them then sort them according to the total marks obtained in physics, chemistry and maths.
    if len(set([sum(i[2:]) for i in dic])) != len([sum(i[2:]) for i in dic]):
        # sorting accoring to the marks of maths,physics and chemistry 
        end = 0
        highest_marks = sum(dic[0][2:])
        for index,ele in enumerate(dic) :
            if sum(ele[2:]) != highest_marks:
                end = index  
                break

        if end != 1:
            # not for only one element
            dic[0:end]=sorted(dic[0:end],key = lambda k : sum(list(k[2:5])),reverse=True)
            # If some students have the same total marks in physics, chemistry and maths then sort according to their name
            if len(set([sum(i[2:5]) for i in dic[0:end]])) != len([sum(i[2:5]) for i in dic[0:end]]):
                dic[0:end]=sorted(dic[0:end],key = lambda k : k[0])
            # If few students have the same name also, then sort them according to their admission numbers.
            if len(set([i[0] for i in dic[0:end]])) != len([i[0] for i in dic[0:end]]):
                dic[0:end]=sorted(dic[0:end],key = lambda k : k[1])

    # show output
    [print(*dic1[:2]) for dic1 in dic]

if __name__ == "__main__":
    test_case_list = [] # save list of array len and array
    total_test_case = int(input())
    for _ in range(total_test_case):
        new_list = input().strip().split(' ')
        test_case_list.append([new_list[0]]+[int(i) for i in new_list[1:]])
    # dic = [
    # ["Danish",132, 76, 66, 95, 40, 77],
    # ["Shreyansh",147, 89, 98, 99, 99, 100],
    # ["Danish ja",132, 76, 66, 95, 40, 77],
    # ["Lakshya",133, 55, 44, 97, 94, 99],
    # ["Shreyansh",144, 89, 98, 99, 99, 100],
    # ["Ayush",145, 90, 90, 90, 30, 54]
    # ]
    answer(test_case_list)