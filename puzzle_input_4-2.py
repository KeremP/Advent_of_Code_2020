import re
path = 'input_4.txt'


class Scanner:
    def __init__ (self, passport):
        self.passport = passport
    def check_fields(self):
        return len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)
    def check_range(self, field, start, end):
        return len(self.passport[field]) == 4 and int(self.passport[field]) >= start and int(self.passport[field]) <= end
    def byr(self):
        return self.check_range('byr',1920,2002)
    def iyr(self):
        return self.check_range('iyr',2010,2020)
    def eyr(self):
        return self.check_range('eyr',2020,2030)
    def hgt(self):
        if self.passport['hgt'][-2:] == 'cm':
            return int(self.passport['hgt'][:-2]) >= 150 and int(self.passport['hgt'][:-2]) <= 193
        elif self.passport['hgt'][-2:] == 'in':
            return int(self.passport['hgt'][:-2]) >= 59 and int(self.passport['hgt'][:-2]) <= 76
    def hcl(self):
        if re.search('^#[0-9a-f]{6}$',self.passport['hcl']):
            return True
        else:
            return False
    def ecl(self):
        return self.passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']
    def pid(self):
        return len(self.passport['pid']) == 9
    def check_valid(self):
        return self.check_fields() and self.byr() and self.iyr() and self.eyr() and self.hgt() and self.hcl() and self.ecl() and self.pid()


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
    #print (passports)
    scanned = [Scanner(passport) for passport in passports]
    valid_cnt=0
    for scan in scanned:
        if scan.check_valid():
            valid_cnt +=1
inpt.close()

print(valid_cnt)
