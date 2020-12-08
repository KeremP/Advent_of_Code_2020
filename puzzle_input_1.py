path = 'input.txt'
data = []
with open(path,'r') as fp:
    for count, line in enumerate(fp):
        print("Input{}: {}".format(count,line))
        data.append(int(line))


print(data)
n = 2020
n2 = n//2
poss_answer = {n-x for x in data if x<=n2} & {x for x in data if x>n2}
pairs = [(n-x,x) for x in poss_answer]
print(pairs)
for i in pairs:
    print(i[0]*i[1])
fp.close()
