def LOOK(arr, head, direction):
    # initalize the empty variables 
    seek_distance_count,distance,cur_track = 0,0,0
    seek_sequence,left,right = [],[],[]
    
    # seperate the values in seperate lists
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
    # Sorting the list left and right 
    left.sort(reverse=(direction != "left"))
    right.sort(reverse=(direction != "right"))
 
    # Runing the while loop two times right and left side 
    run = 2
    while (run):
        if (direction == "left"):
            for i in left:
                # Appending current track to seek list
                seek_sequence.append(i)
                # Calculate absolute distance and add in total seek count
                seek_distance_count +=  abs(i - head)
                # now undate the new head
                head = i
 
            direction = "right"
             
        elif (direction == "right"):
            for i in right :
                # Appending current track to seek list
                seek_sequence.append(i) 
                # Calculate absolute distance and add in the total seek count 
                seek_distance_count += abs(i - head)
                # now undate the new head
                head = i

            direction = "left"

        run -= 1

    print("Total number of seek operations =",seek_distance_count)
    print("Seek Sequence is")
    [print(i) for i in seek_sequence]

if __name__ == "__main__":
    # test case
    arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
    head = 50
    size = len(arr)

    direction = "right" 
    print("Initial position of head:", head)
    LOOK(arr, head, direction)