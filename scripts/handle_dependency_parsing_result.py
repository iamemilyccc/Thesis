#handle dependency parsing result

def format(infile, outfile):
    with open (infile, 'r') as f:
        data = f.readlines()
    sent = []
    for line in data:
        if line == '' or line == '\n':
            sent.append('\n')
        else:
            sent.append(line.rstrip() + '@%#')

    with open (outfile, 'a') as new:
        for claim in sent:
            new.write(claim)

if __name__ == '__main__':
    infile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/mddweee-parsed.txt'
    outfile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/mddweee-parsed-linebyline.txt'
    format(infile, outfile)