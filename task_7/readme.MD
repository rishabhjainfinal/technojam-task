# task_7
### Implementation and theory of the LOOK algorithm in your desired language. 

## steps
1. initalize the empty variables 
```python
    seek_distance_count,distance,cur_track = 0,0,0
    seek_sequence,left,right = [],[],[]
```

2. seperate the values in seperate lists
```python
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
```

3. Sorting the list left and right  and in the reverse order if direction is not is not same 
```python
    left.sort(reverse=(direction != "left"))
    right.sort(reverse=(direction != "right"))
```

4. Runing the while loop two times right and left side 
  - using if statements to go in the direction and use perticular list 
  - use for loop to iter in the list 
      - append the head in the sequence list 
      - calculate the distace between last and this head 
      - update the head at last to the current head
  - reverse the direction 
  - run while loop second time with reversed direction
```python 
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
```