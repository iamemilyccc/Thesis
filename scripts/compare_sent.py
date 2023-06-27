#find out the wrongly tokenized sentences


def compare(infile, tagged):
    with open (infile, 'r') as f:
        data = f.readlines()
    with open (tagged, 'r') as t:
        tagsent = t.readlines()
    for i, line in enumerate(data):
        if line[0] != tagsent[i][0] and line[0] != '"':
            return i

infile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/nopunctuations_test.txt'
tagged = '/Users/emilychen/Desktop/MPLT_Thesis/Data/nopunctuations_test-tagged.txt'
print(compare(infile, tagged))
