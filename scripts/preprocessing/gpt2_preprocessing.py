import torch
import json
import numpy as np
from datasets import load_dataset
from transformers import GPT2Tokenizer
from sklearn.model_selection import train_test_split

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def tokenize(inputfile):
    with open (inputfile, 'r') as f:
        data = [json.loads(line) for line in f.readlines()] #data = list
    for obj in data:
        dict = {}
        dict['claim'] = tokenizer(obj['claim'])
        dict['label'] = tokenizer(obj["label"])
        with open('train_trial.json', 'w') as new:
            json.dump(dict, new)
            new.write('\n')

tokenize('./train_small.json')
