import json

def preprocess_fever(input_file, output_file):
    with open(input_file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]

    with open(output_file, 'w') as f:
        for claim in data:
            # Preprocess the claim text
            claim_text = claim['claim'].replace('\n', ' ').strip()
            claim_text = claim_text.replace('"', '\\"')
            
            # Preprocess the evidence text
            label_text = claim['label']
            
            # Write the preprocessed claim and evidence to the output file
            f.write(f'"{claim_text}", "{label_text}"\n')

if __name__ == '__main__':
    input_file = '/Users/emilychen/Desktop/MPLT_Thesis/FEVER_dataset/small_train.jsonl'
    output_file = '/Users/emilychen/Desktop/MPLT_Thesis/jsonTodict/todict'
    preprocess_fever(input_file, output_file)