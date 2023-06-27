#sort the nested sentences


def sort_nested(infile):
    with open(infile, 'r') as f:
        data = f.readlines()
    with open('nobra_nonest.txt', 'w') as new:
        for line in data:
            newline = line.replace(' }_-RRB- {_-LRB- ', '\n')
            new.write(newline)
        new.close()

infile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/removed-endbracketsnew.txt'
sort_nested(infile)