#remove the left

def remove(infile):
    with open(infile, 'r') as f:
        data = f.readlines()
    with open('nopunctuations3.txt', 'w') as new:
        for line in data:
            # if '!' in line and 'i' not in line[-2::]:
            #     clean = line.replace('!', '')
            #     new.write(line)
            # if '.' not in line[-2::]:
            #     clean = line.rstrip() + '.' + '\n' 
            #     new.write(clean)
            if line.endswith('U.S.\n') == True:
                clean = line.replace('U.S.', 'U.S..')
                new.write(clean)
            elif line.endswith('U.N.\n') == True:
                clean = line.replace('U.N.', 'U.N..')
                new.write(clean)
            elif line.endswith('F.C.\n') == True:
                clean = line.replace('F.C.', 'F.C..')
                new.write(clean)
            elif line.endswith('X.\n') == True:
                clean = line.replace('X.', 'X..')
                new.write(clean)
            elif line.endswith('A.\n') == True:
                clean = line.replace('A.', 'A..')
                new.write(clean)
            elif line.endswith('D.C.\n') == True:
                clean = line.replace('D.C.', 'D.C..')
                new.write(clean)
            elif line.endswith('Henry IV.\n') == True:
                clean = line.replace('Henry IV.', 'Henry IV..')
                new.write(clean)
            elif line.endswith('Henry I.\n') == True:
                clean = line.replace('Henry I.', 'Henry I..')
                new.write(clean)
            # elif '.' in line and '.' not in line[-2::] and 'U.S.' not in line and 'R.Kelly' not in line:
            #     clean = line.replace('.', ',')
            #     new.write(clean)
            else:
                new.write(line)
        new.close()

infile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/nopunctuations2.txt'
remove(infile)