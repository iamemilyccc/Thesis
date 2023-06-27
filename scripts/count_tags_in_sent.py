#count tags in each sentence

from collections import defaultdict

# def sent_len_lst(infile): #infile = tagged sent
#     with open (infile, 'r') as f:
#         data = f.readlines()
#     sent_len_lst = []
#     for line in data:
#         num_words = line.split()
#         sent_len_lst.append(len(num_words))

def count_tags(infile):
    with open (infile, 'r') as f:
        data = f.readlines()

    sent_dict = defaultdict(dict)
    tag_dict = defaultdict(int)
    for line in data: #Adrienne_NNP Bailon_NNP is_VBZ an_DT accountant_NN ._. len=6
        lst_sent = line.split() #['System_NNP', 'of_IN', 'a_DT', 'Down_JJ', 'briefly_NN', 'disbanded_VBN', 'in_IN', 'limbo_NN', '._.']
        l = str(len(lst_sent))
        if l in sent_dict:
            sent_dict[l]['num'] += 1
        else:
            sent_dict[l] = defaultdict(int)
            sent_dict[l]['num'] += 1
        for word in lst_sent: #word = 'System_NNP', 'of_IN' ...
            tag = (word.split('_'))[1]
            if tag in ['NN', 'NNS', 'NNPS', 'NNP']:
                sent_dict[l]['Noun'] += 1
            elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                sent_dict[l]['Verb'] += 1
                #tag_dict[tag] += 1
    return sent_dict

    
d = count_tags('/Users/emilychen/Desktop/MPLT_Thesis/Data/nopunctuations3tagged.txt')
print(d)
