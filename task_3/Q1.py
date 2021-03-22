# Rob Stark is a prisoner in King's Landing and has demanded a trial by combat where he will fight against any opponent that Cersei Lannister choses.Cersei decided that Rob will face either of The Mountain, The Hound, Jaime and tywin. Now Rob is standing in the ring facing East Initially with The Mountain standing on the north side, the hound on the south side, Jaime on the west side and Tywin on the east side of the ring. Cersei gives Rob a binary String consisting only of 0,s and 1’s. Rob starts reading the binary string facing east initially . When he sees a '0', he turns 90 degrees to his right. When he sees a '1', he turns 90 degrees to his left.After reading the entire string, which opponent will Rob face?

def answer(binary):
    # 0 - right
    # 1 - left
    binary = str(binary)
    binary = binary.replace('0'*4,'').replace('1'*4,'').replace('01','').replace('10','')
    current_possition = person_direction
    if binary:
        for i in binary:
            if int(i) == 0:
                if current_possition < 3 : current_possition += 1
                else : current_possition = 0
            else:
                if current_possition > 0 : current_possition -= 1
                else : current_possition = 3
        return positions[current_possition]
    else : return positions[current_possition]
    
if __name__ == "__main__":
    positions = {
        0:"mountain", # north 0
        1:"tywin", # east 1
        2:"hound", # south 2
        3:"jaime"    # west 3
    }
    person_direction = 1
    binary_list = []
    total_test_case = int(input())
    for _ in range(total_test_case):
        input()
        binary_list.append(int(input()))
    
    for binary in binary_list:
        print(answer(binary))