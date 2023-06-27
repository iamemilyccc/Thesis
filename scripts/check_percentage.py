#check noun and verb percentage

from collections import defaultdict

def get_tags(infile):
    with open (infile, 'r') as f:
        data = f.readlines()
   
    all_tags = []
    for line in data: #Adrienne_NNP Bailon_NNP is_VBZ an_DT accountant_NN ._. len=6
        lst_sent = line.split() #['System_NNP', 'of_IN', 'a_DT', 'Down_JJ', 'briefly_NN', 'disbanded_VBN', 'in_IN', 'limbo_NN', '._.']
        sent_tag = []
        for item in lst_sent:
            tag = ((item.split('_'))[1])
            sent_tag.append(tag)
        all_tags.append(sent_tag)
    return all_tags

def check_noun_percentage(lst):
    sent_dict = defaultdict(dict)
    for sent in lst:
        l = str(len(sent)) #sent_length = num of tags
        n_tags = 0
        for tag in sent:
            if tag in ['NN', 'NNS', 'NNPS', 'NNP']:
                n_tags += 1
        pcg_noun = n_tags / len(sent)
        if l in sent_dict:
            if pcg_noun >= 0.0 and pcg_noun <= 0.1 :
                sent_dict[l]['noun 0 - 10%'] += 1
            elif pcg_noun > 0.1 and pcg_noun <= 0.2 :
                sent_dict[l]['noun 10 - 20%'] += 1
            elif pcg_noun > 0.2 and pcg_noun <= 0.3 :
                sent_dict[l]['noun 20 - 30%'] += 1
            elif pcg_noun > 0.3 and pcg_noun <= 0.4 :
                sent_dict[l]['noun 30 - 40%'] += 1
            elif pcg_noun > 0.4 and pcg_noun <= 0.5 :
                sent_dict[l]['noun 40 - 50%'] += 1
            elif pcg_noun > 0.5 :
                sent_dict[l]['noun > 50%'] += 1
        else:
            sent_dict[l] = defaultdict(int)
            if pcg_noun >= 0.0 and pcg_noun <= 0.1 :
                sent_dict[l]['noun 0 - 10%'] += 1
            elif pcg_noun > 0.1 and pcg_noun <= 0.2 :
                sent_dict[l]['noun 10 - 20%'] += 1
            elif pcg_noun > 0.2 and pcg_noun <= 0.3 :
                sent_dict[l]['noun 20 - 30%'] += 1
            elif pcg_noun > 0.3 and pcg_noun <= 0.4 :
                sent_dict[l]['noun 30 - 40%'] += 1
            elif pcg_noun > 0.4 and pcg_noun <= 0.5 :
                sent_dict[l]['noun 40 - 50%'] += 1
            elif pcg_noun > 0.5 :
                sent_dict[l]['noun > 50%'] += 1
    return sent_dict


def check_verb_percentage(lst):
    sent_dict = defaultdict(dict)
    for sent in lst:
        l = str(len(sent)) #sent_length = num of tags
        v_tags = 0
        for tag in sent:
            if tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                v_tags += 1
        pcg_verb = v_tags / len(sent)
        if l in sent_dict:
            if pcg_verb >= 0.0 and pcg_verb <= 0.1 :
                sent_dict[l]['verb 0 - 10%'] += 1
            elif pcg_verb > 0.1 and pcg_verb <= 0.2 :
                sent_dict[l]['verb 10 - 20%'] += 1
            elif pcg_verb > 0.2 and pcg_verb <= 0.3 :
                sent_dict[l]['verb 20 - 30%'] += 1
            elif pcg_verb > 0.3 and pcg_verb <= 0.4 :
                sent_dict[l]['verb 30 - 40%'] += 1
            elif pcg_verb > 0.4 and pcg_verb <= 0.5 :
                sent_dict[l]['verb 40 - 50%'] += 1
            elif pcg_verb > 0.5 :
                sent_dict[l]['verb > 50%'] += 1
        else:
            sent_dict[l] = defaultdict(int)
            if pcg_verb >= 0.0 and pcg_verb <= 0.1 :
                sent_dict[l]['verb 0 - 10%'] += 1
            elif pcg_verb > 0.1 and pcg_verb <= 0.2 :
                sent_dict[l]['verb 10 - 20%'] += 1
            elif pcg_verb > 0.2 and pcg_verb <= 0.3 :
                sent_dict[l]['verb 20 - 30%'] += 1
            elif pcg_verb > 0.3 and pcg_verb <= 0.4 :
                sent_dict[l]['verb 30 - 40%'] += 1
            elif pcg_verb > 0.4 and pcg_verb <= 0.5 :
                sent_dict[l]['verb 40 - 50%'] += 1
            elif pcg_verb > 0.5 :
                sent_dict[l]['verb > 50%'] += 1
    return sent_dict


def print_sorted(dict):
    total = []
    for len_indice in dict: # '2', '4', ...
        tags = []
        for ele in dict[len_indice]: # 'noun
            tags.append(ele)
        tags.sort()
        sent = []
        for tag in tags:
            sent.append(len_indice + '$' + tag + ':' + str(dict[len_indice][tag]))
        total.append(sent)
    print(total)

senttags = get_tags('/Users/emilychen/Desktop/MPLT_Thesis/Data/nopunctuations_test_tagged.txt')
noun = check_noun_percentage(senttags)
check_verb_percentage(senttags)
# print_sorted(verb)
