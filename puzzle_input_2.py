path = 'input_2.txt'

valid_cnt = 0
with open(path,'r') as fp:
    for count, line in enumerate(fp):
        phrases = line.split(' ')
        #print(phrases)
        policy = []
        symbol = phrases[1].strip('\n:')
        target = phrases[2].strip('\n:')
        r = phrases[0].split('-')
        for i in r:
            policy.append(int(i))
        print('Symb:',symbol,type(symbol))
        print('Target:',target)
        print('Policy:',policy)
        print(type(policy[0]))
        #print(min(policy))
        symbol_count = target.count(symbol)
        print(symbol_count)
        if symbol_count >= policy[0] and symbol_count <= policy[1]:
            valid_cnt +=1
        else:
            print('Invalid')


fp.close()
print(valid_cnt)
