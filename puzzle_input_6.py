path = 'input_6.txt'

def get_data(inpt):
    groups = []
    answers = set()
    for line in inpt:

        if line != '\n':
            resp = line.rstrip()
            for char in resp:
                answers.add(char)
        else:
            groups.append(answers)
            answers=set()
    groups.append(answers)
    return groups

with open(path,'r') as inpt:
    groups = get_data(inpt)
    #print(groups)
    counts = []
    for group in groups:
        count = len(group)
        counts.append(count)
    print(sum(counts))
inpt.close()
