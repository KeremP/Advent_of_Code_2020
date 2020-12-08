path = 'input_2.txt'

valid_cnt = 0
with open(path,'r') as fp:
    for count, line in enumerate(fp):
        phrases = line.split(' ')
        #print(phrases)
        position = []
        symbol = phrases[1].strip('\n:')
        target = phrases[2].strip('\n:')
        r = phrases[0].split('-')
        for i in r:
            position.append(int(i)-1)
        #print(min(policy))
        if bool(target[position[0]] == symbol) ^ bool(target[position[1]] == symbol):
            valid_cnt +=1
            print('Valid!')



fp.close()
print(valid_cnt)
