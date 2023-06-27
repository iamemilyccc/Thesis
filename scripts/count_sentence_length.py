#count sentence length

import json
from collections import defaultdict
def get_sent_len(infile):
    with open(infile, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]
    len_dict = defaultdict(int)
    for ele in data:
        lst_of_claim_str = (ele['claim']).split()
        len_dict[len(lst_of_claim_str)] += 1
    print (len_dict)

get_sent_len('/Users/emilychen/Desktop/MPLT_Thesis/FEVER_dataset/paper_test.jsonl')
