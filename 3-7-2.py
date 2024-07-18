with open('sample.txt 2', 'r') as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num
    print(sum)

