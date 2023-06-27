#remove the left

def remove(infile):
    with open(infile, 'r') as f:
        data = f.readlines()
    with open('removed-endbracketsnew.txt', 'w') as new:
        for line in data:
            clean = line[16::]
            new.write(clean)
        new.close()

infile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/train_dev_claimtext-withsbrackets-tagged.txt'
remove(infile)