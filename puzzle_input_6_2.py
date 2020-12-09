path = 'input_6.txt'

def get_data(inpt):
    groups = []
    answers = []
    questions = set()
    member_count = 0
    consensus = 0
    for line in inpt:

        if line != '\n':
            member_count+=1
            resp = line.rstrip()
            for char in resp:
                answers.append(char)
                questions.add(char)
        else:
            for i in questions:
                if answers.count(i) == member_count:
                    consensus+=1
            groups.append(consensus)
            answers=[]
            member_count=0
            consensus=0
    groups.append(consensus)
    return groups

with open(path,'r') as inpt:
    groups = get_data(inpt)
    #print(groups)
    print(sum(groups))
inpt.close()
