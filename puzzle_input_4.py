req_fields = ['ecl','pid','eyr','hcl','byr','iyr','hgt','cid']
path = 'input_4.txt'


class Scanner:
    def __init__ (self, passport):
        self.passport = passport
    def check_fields(self):
        return len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)


def get_data(inpt):
    passport = {}
    passports = []
    for line in inpt:
        if line != '\n':
            line = line.rstrip().split(' ')
            line = [field.split(':') for field in line]
            for field in line:
                passport[field[0]] = field[1]
                #print(line)
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    return passports


with open(path,'r') as inpt:
    passports = get_data(inpt)
    print (passports)
    scanned = [Scanner(passport) for passport in passports]
    valid_cnt=0
    for scan in scanned:
        if scan.check_fields():
            valid_cnt +=1
inpt.close()

print(valid_cnt)
