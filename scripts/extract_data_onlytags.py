import json

def extract_data(tagfile, ogfile): 
    with open (tagfile, 'r') as tf:
        tagged_data = tf.readlines()
    with open (ogfile, 'r') as og:
        original_data = [json.loads(line) for line in og.readlines()]
    with open ('extracted.json', 'w') as new:
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
            sent_only_tag = ' '.join(sent_tag)
            for tag in sent_tag:
                if tag in ['NN', 'NNS', 'NNPS', 'NNP']:
                    noun_tag += 1
                elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                    verb_tag += 1
            pcg_noun = noun_tag / l
            pcg_verb = verb_tag / l
            # print(pcg_noun, pcg_verb)
            if l == 7 or l == 8 :
                if pcg_noun > 0.2 and pcg_noun <= 0.3 :
                    dict = {}
                    dict['claim'] = sent_only_tag
                    dict['label'] = original_data[i]['label'] #original data[i] is a string
                    json.dump(dict, new)
                    new.write('\n')



if __name__ == '__main__':
    # tagfile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/preprocessing/weee-tagged.txt'
    # ogfile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/preprocessing/weee.txt'
    tagfile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/nopunctuations_test_tagged.txt'
    ogfile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/test.json'
    extract_data(tagfile, ogfile) 