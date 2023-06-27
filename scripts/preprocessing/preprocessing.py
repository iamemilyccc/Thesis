import torch
import json
from transformers import GPT2Tokenizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_data(path):
    with open(path) as f:
        data = json.load(f)
    return data
# Load the data
data = load_data('./small_train_dict')

def extract(data):
    claims = []
    labels = []
    for key in data:
        claims.append(data[key]['claim'])
        labels.append(data[key]['label'])
    return claims, labels

claims, labels = extract(data)

# Tokenize the input text
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenized_text = [tokenizer.encode(text) for text in claims]

# Encode the labels
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Split the data into train, validation, and test sets
train_texts, val_texts, train_labels, val_labels = train_test_split(tokenized_text, encoded_labels, test_size=0.2)
train_texts, test_texts, train_labels, test_labels = train_test_split(train_texts, train_labels, test_size=0.2)

# Save the preprocessed data
torch.save((train_texts, train_labels), 'train_data.pt')
torch.save((val_texts, val_labels), 'val_data.pt')
torch.save((test_texts, test_labels), 'test_data.pt')