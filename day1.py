def left_right():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        left = []
        right = []
        for line in lines:
            left.append(int(line.split()[0]))
            right.append(int((line.split()[1])))
    left = list(set(left))
    right.sort()
    
    sum = 0
    for i in left:
        sum += i*right.count(i)

    print(sum)

left_right()