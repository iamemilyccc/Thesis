import json

def preprocess_fever(input_file, output_file): #, output_file):
    output = []
    with open (input_file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()] #list
    for obj in data:
        dict = {}
        # dict['id'] = obj['id']
        dict['label'] = obj['label']
        dict['claim'] = obj['claim']
        dict['evidence'] = obj['evidence']
        # output.append(dict)
        with open (output_file, 'a') as new:
            json.dump(dict, new)
            new.write('\n')


if __name__ == '__main__':
    input_file = '/Users/emilychen/Desktop/MPLT_Thesis/FEVER_dataset/train+dev.jsonl'
    output_file = '/Users/emilychen/Desktop/MPLT_Thesis/Data/train+dev_withevidence.json'
    preprocess_fever(input_file, output_file) 