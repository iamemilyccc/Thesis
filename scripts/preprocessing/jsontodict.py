import json

def preprocess_fever(input_file, output_file):
    with open(input_file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]
    dict = {}
    for i, claim in enumerate(data):
        claim_text = claim['claim'].replace('\n', ' ').strip()
        claim_text = claim_text.replace('"', '\\"')
        label_text = claim['label']
        dict[i] = {'claim': claim_text, 'label': label_text}

    with open(output_file, 'w') as f:
        json.dump(dict,f)
if __name__ == '__main__':
    input_file = '/Users/emilychen/Desktop/MPLT_Thesis/FEVER_dataset/small_train.jsonl'
    output_file = '/Users/emilychen/Desktop/MPLT_Thesis/jsonTodict/todict'
    preprocess_fever(input_file, output_file)