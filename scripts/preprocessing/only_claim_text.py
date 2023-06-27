import json

def preprocess_fever(input_file, output_file): #, output_file):
    with open (input_file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()] #list
    with open (output_file, 'a') as new:
        for obj in data:
            new.write(obj['claim']+'\n')


if __name__ == '__main__':
    input_file = '/Users/emilychen/Desktop/MPLT_Thesis/FEVER_dataset/paper_test.jsonl'
    output_file = '/Users/emilychen/Desktop/MPLT_Thesis/Data/test_claimtext.txt'
    preprocess_fever(input_file, output_file) 