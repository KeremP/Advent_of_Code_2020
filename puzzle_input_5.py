path = 'input_5.txt'

class Seat_Finder():
    def __init__(self,ticket):
        self.ticket = ticket
    def find_row(self):
        row_id = self.ticket[:7]
        rows=[i for i in range(128)]
        for id in row_id:
            #print(rows)
            if id == 'F':
                rows = rows[:len(rows)//2]
            elif id =='B':
                rows = rows[len(rows)//2:]
        return rows
    def find_col(self):
        col_id = self.ticket[-3:]
        cols = [c for c in range(8)]
        for col in col_id:
            #print(cols)
            if col == 'R':
                cols = cols[len(cols)//2:]
            elif col == 'L':
                cols = cols[:len(cols)//2]
        return cols
seat_ids = []

with open(path,'r') as inpt:
    for line in inpt:
        finder = Seat_Finder(line.rstrip())
        row = finder.find_row()
        col = finder.find_col()
        seat_ids.append((row[0]*8+col[0]))

print(max(seat_ids))
