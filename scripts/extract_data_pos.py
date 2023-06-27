import json

def extract_data(tagfile, ogfile): 
    with open (tagfile, 'r') as tf:
        tagged_data = tf.readlines()
    with open (ogfile, 'r') as og:
        original_data = og.readlines()
    with open ('1112v01.txt', 'w') as new:
        for i, sent in enumerate(tagged_data):
            noun_tag = 0
            verb_tag = 0
            lst_sent = sent.split() #['System_NNP', 'of_IN', 'a_DT', 'Down_JJ', 'briefly_NN', 'disbanded_VBN', 'in_IN', 'limbo_NN', '._.']
            # print(lst_sent)
            l = len(lst_sent)
            # print(l)
            sent_tag = []
            for item in lst_sent:
                tag = ((item.split('_'))[1])
                sent_tag.append(tag)
            for tag in sent_tag:
                if tag in ['NN', 'NNS', 'NNPS', 'NNP']:
                    noun_tag += 1
                elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                    verb_tag += 1
            pcg_noun = noun_tag / l
            pcg_verb = verb_tag / l
            # print(pcg_noun, pcg_verb)
            if l == 11 or l == 12 :
                if pcg_verb >= 0.0 and pcg_verb <= 0.1: #and pcg_noun > 0.3 and pcg_noun <= 0.4 :
                    new.write(original_data[i])




if __name__ == '__main__':
    # tagfile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/preprocessing/weee-tagged.txt'
    # ogfile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/preprocessing/weee.txt'
    tagfile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/nopunctuations3_train+dev_tagged.txt'
    ogfile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/train+dev.txt'
    extract_data(tagfile, ogfile) 