import json

def extract_data(parsedfile, ogfile): 
    with open (parsedfile, 'r') as parsed:
        parsed_data = parsed.readlines()
    with open (ogfile, 'r') as og:
        original_data = og.readlines()
    with open ('extracted_mdd.txt', 'w') as extracted:
        for i, sent in enumerate(parsed_data):  # 'nsubj(recorded-2, Selena-1)@root(ROOT-0, recorded-2)@obj(recorded-2, music-3)@punct(recorded-2, .-4)@'
            sent_len = len(sent.split('@%#')) - 2 # minus '.' + '' at the end of sent
            dis_to_count = (sent.split('@%#'))[:-2] # ['nsubj(recorded-2, Selena-1)', 'root(ROOT-0, recorded-2)', 'obj(recorded-2, music-3)']
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
                    return sent
                    # print(value)
                depdis += abs(int(value[0]) - int(value[1]))  
            mdd = depdis / sent_len
            # print(mdd)
            if sent_len == 10 or sent_len == 11 :
                if mdd > 3.0 and mdd <= 3.5:
                    extracted.write(original_data[i])




if __name__ == '__main__':
    # parsedfile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/mddweee-parsed-linebyline.txt'
    # ogfile = '/Users/emilychen/Desktop/MPLT_Thesis/scripts/mddweee.txt'
    parsedfile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/nopun3_train+dev-parsed-linebyline.txt'
    ogfile = '/Users/emilychen/Desktop/MPLT_Thesis/Data/train+dev.txt'
    extract_data(parsedfile, ogfile) 