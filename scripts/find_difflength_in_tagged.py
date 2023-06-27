#compare sent length in og file and tagged

def compare(ogfile, tagged):
    with open (ogfile, 'r') as og:
        og_data = og.readlines() #Toy Story 3 has a sequel.
    with open(tagged, 'r') as tag:
        tagged_data = tag.readlines() #Toy_NNP Story_NNP 3_CD has_VBZ a_DT sequel_NN ._.
    for i, og_sent in enumerate(og_data):
        sent = og_sent.split() #sent[-1] = 'sequel.'
        tag_sent = tagged_data[i].split()
        last_two = (tag_sent[-2].split('_'))[0] + (tag_sent[-1].split('_'))[0]
        if last_two != sent[-1]:
            print(og_sent)
            print(tag_sent)

ogfile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/train+dev_claimtext.txt'
tagged = '/Users/emilychen/Desktop/MPLT_Thesis/Data/train_dev_claimtext-tagged.txt'

compare(ogfile, tagged)

