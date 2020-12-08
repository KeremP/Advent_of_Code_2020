path = 'input.txt'
data = []
with open(path,'r') as fp:
    for count, line in enumerate(fp):
#        print("Input{}: {}".format(count,line))
        data.append(int(line))


#print(data)
group = set()
n = 2020
for i, item in enumerate(data):
    for j in data:
        for k in data:
            if item+j+k == n :
                group.add(item)
                group.add(j)
                group.add(k)

group = list(group)
print(group[0]*group[1]*group[2])
fp.close()
