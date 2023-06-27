#calculate word density
import json
from collections import defaultdict

def get_sent(infile):
    with open(infile, 'r') as f:
        data = [line for line in f.readlines()]

    sent_lst = []
    for sent in data:
        lst_of_words = sent.split()
        sent_lst.append(lst_of_words)
       
    return sent_lst #[0:2]

def get_wdd(lst):
    lst_wdd = []
    
    for s in lst: # s =['Roman', 'Atwood', 'is', 'a', 'content', 'creator.']
        vocab_dict = defaultdict(int)
        for w in s: #'Roman'
            vocab_dict[w] += 1
        max_value = max(vocab_dict.values())
        # print(max_value)
        # print(vocab_dict)
        max_wdd = float(max_value / len(s))
        lst_wdd.append(max_wdd)
    return lst_wdd

       
# def sort_wdd(wdd_lst):
#     sent_wdd = defaultdict(int)
#     for i in wdd_lst: 
#         if i > 0 and i<= 0.1:
#             sent_wdd['0-0.1'] += 1
#         elif i > 0.1 and i <= 0.2:
#             sent_wdd['0.1-0.2'] += 1
#         elif i > 0.2 and i <= 0.3:
#             sent_wdd['0.2-0.3'] += 1
#         elif i > 0.3 and i <= 0.4:
#             sent_wdd['0.3-0.4'] += 1
#         elif i > 0.4 and i <= 0.5:
#             sent_wdd['0.4-0.5'] += 1
#         elif i > 0.5 and i <= 1:
#             sent_wdd['>0.5'] += 1
#         elif i > 1:
#             sent_wdd['>1'] += 1
        
#     print(sent_wdd)

def get_num_of_sent(wdd_lst, sent_lst):
    sent_wdd = defaultdict(int)
    for i, ele in enumerate(wdd_lst):
        if len(sent_lst[i]) == 6 or len(sent_lst[i]) == 7:
            if ele > 0 and ele <= 0.1:
                sent_wdd['6-7, 0-0.1'] += 1
            elif ele > 0.1 and ele <= 0.2:
                sent_wdd['6-7, 0.1-0.2'] += 1
            elif ele > 0.2 and ele <= 0.3:
                sent_wdd['6-7, 0.2-0.3'] += 1
        elif len(sent_lst[i]) == 8 or len(sent_lst[i]) == 9:
            if ele > 0 and ele <= 0.1:
                sent_wdd['8-9, 0-0.1'] += 1
            elif ele > 0.1 and ele <= 0.2:
                sent_wdd['8-9, 0.1-0.2'] += 1
            elif ele > 0.2 and ele <= 0.3:
                sent_wdd['8-9, 0.2-0.3'] += 1
        elif len(sent_lst[i]) == 10 or len(sent_lst[i]) == 11:
            if ele > 0 and ele <= 0.1:
                sent_wdd['10-11, 0-0.1'] += 1
            elif ele > 0.1 and ele <= 0.2:
                sent_wdd['10-11, 0.1-0.2'] += 1
            elif ele > 0.2 and ele <= 0.3:
                sent_wdd['10-11, 0.2-0.3'] += 1
    print(sent_wdd)

if __name__ == '__main__':
    to_read = '/Users/emilychen/Desktop/MPLT_Thesis/Data/train+dev_claimtext.txt'
    sent_lst = get_sent(to_read)
    wdd_lst = get_wdd(sent_lst)
    # sort_wdd(wdd_lst)
    get_num_of_sent(wdd_lst, sent_lst)
