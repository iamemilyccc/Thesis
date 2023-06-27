#calculate MDD (Mean of dependency distance)

from collections import defaultdict

def get_mdd(infile):
    with open (infile, 'r') as f:
        data = f.readlines()
    sum_dict = defaultdict(dict)
    dict_mdd = defaultdict(int)
    for line in data: # 'nsubj(recorded-2, Selena-1)@root(ROOT-0, recorded-2)@obj(recorded-2, music-3)@punct(recorded-2, .-4)@'
        sent_len = len(line.split('@%#')) - 2 # minus '.' + '' at the end of sent
        dis_to_count = (line.split('@%#'))[:-2] # ['nsubj(recorded-2, Selena-1)', 'root(ROOT-0, recorded-2)', 'obj(recorded-2, music-3)']
        # print(dis_to_count)
        depdis = 0 #dependency distance
        for item in dis_to_count: # 'nsubj(recorded-2, Selena-1)'
            noleft = item.replace('(', '')
            noright = noleft.replace(')', '')
            new = noright.split(', ') # ['nsubj(recorded-2', 'Selena-1)']
            value = []
            for w in new:
                if '--' in w:
                    w = w.replace('--', '@-')
                w_lst = w.split('-')
                value.append(w_lst[-1])
            # print(value)
            if len(value) != 2 :
                return line
            # print(value)
            depdis += abs(int(value[0]) - int(value[1]))
        # print(depdis)    
        mdd = depdis / sent_len
    #     if sent_len not in sum_dict:
    #         sum_dict[sent_len] = defaultdict(int)
    #         if mdd > 1 and mdd < 1.5 :
    #             sum_dict[sent_len]['mdd 1-1.5'] += 1
    #         elif mdd >= 1.5 and mdd < 2:
    #             sum_dict[sent_len]['mdd 1.5-2'] += 1
    #         elif mdd >= 2 and mdd < 2.5:
    #             sum_dict[sent_len]['mdd 2-2.5'] += 1
    #         elif mdd >= 2.5 and mdd < 3:
    #             sum_dict[sent_len]['mdd 2.5-3'] += 1
    #         elif mdd >= 3 and mdd < 3.5:
    #             sum_dict[sent_len]['mdd 3-3.5'] += 1
    #         elif mdd >= 3.5 and mdd < 4:
    #             sum_dict[sent_len]['mdd 3.5-4'] += 1
    #         elif mdd >= 4 and mdd < 4.5:
    #             sum_dict[sent_len]['mdd 4-4.5'] += 1
    #         elif mdd >= 4.5 and mdd < 5:
    #             sum_dict[sent_len]['mdd 4.5-5'] += 1
    #         elif mdd >= 5:
    #             sum_dict[sent_len]['mdd >5'] += 1
    #     else:
    #         if mdd > 1 and mdd < 1.5 :
    #             sum_dict[sent_len]['mdd 1-1.5'] += 1
    #         elif mdd >= 1.5 and mdd < 2:
    #             sum_dict[sent_len]['mdd 1.5-2'] += 1
    #         elif mdd >= 2 and mdd < 2.5:
    #             sum_dict[sent_len]['mdd 2-2.5'] += 1
    #         elif mdd >= 2.5 and mdd < 3:
    #             sum_dict[sent_len]['mdd 2.5-3'] += 1
    #         elif mdd >= 3 and mdd < 3.5:
    #             sum_dict[sent_len]['mdd 3-3.5'] += 1
    #         elif mdd >= 3.5 and mdd < 4:
    #             sum_dict[sent_len]['mdd 3.5-4'] += 1
    #         elif mdd >= 4 and mdd < 4.5:
    #             sum_dict[sent_len]['mdd 4-4.5'] += 1
    #         elif mdd >= 4.5 and mdd < 5:
    #             sum_dict[sent_len]['mdd 4.5-5'] += 1
    #         elif mdd >= 5:
    #             sum_dict[sent_len]['mdd >5'] += 1
    # return sum_dict #  # dict_mdd
        if mdd > 1 and mdd < 1.5 :
            dict_mdd['mdd 1-1.5'] += 1
        elif mdd >= 1.5 and mdd < 2:
            dict_mdd['mdd 1.5-2'] += 1
        elif mdd >= 2 and mdd < 2.5:
            dict_mdd['mdd 2-2.5'] += 1
        elif mdd >= 2.5 and mdd < 3:
            dict_mdd['mdd 2.5-3'] += 1
        elif mdd >= 3 and mdd < 3.5:
            dict_mdd['mdd 3-3.5'] += 1
        elif mdd >= 3.5 and mdd < 4:
            dict_mdd['mdd 3.5-4'] += 1
        elif mdd >= 4 and mdd < 4.5:
            dict_mdd['mdd 4-4.5'] += 1
        elif mdd >= 4.5 and mdd < 5:
            dict_mdd['mdd 4.5-5'] += 1
        elif mdd >= 5:
            dict_mdd['mdd >5'] += 1
    return dict_mdd

print(get_mdd('/Users/emilychen/Desktop/MPLT_Thesis/Data/nopun_test-parsed-linebyline.txt'))
# print(get_mdd('/Users/emilychen/Desktop/MPLT_Thesis/Data/test-parsed-linebyline.txt'))
