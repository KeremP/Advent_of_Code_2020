def trees_by_slope(right,down,lines):
    x = right
    y = down
    tree = 0
    while y < len(lines):
        if x > len(lines[y]) - 1:
            x = x%len(lines[y])
        if lines[y][x]=='#':
            tree+=1
        x += right
        y += down
    return tree

path = "input_3.txt"

with open(path,'r') as input:
    lines = [line for line in input]
    h = len(lines)
    w = len(lines[0])
    lines = [list(line.rstrip()) for line in lines]

    print('# of Trees:',trees_by_slope(3,1,lines))

    total_trees = []
    right = [1,3,5,7,1]
    down = [1,1,1,1,2]

    for i in range(len(right)):
        trees = trees_by_slope(right=right[i],down=down[i],lines=lines)
        total_trees.append(trees)

    answer = total_trees[0]*total_trees[1]*total_trees[2]*total_trees[3]*total_trees[4]

    print(answer)
