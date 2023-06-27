import random
import json

label = ['SUPPORTS', 'REFUTES', 'NOT ENOUGH INFO']
stupid = (0.5433, 0.2310, 0.2256)
randomlst1 = random.choices(label, weights = stupid, k=450)
randomlst2 = random.choices(label, weights = stupid, k=450)
randomlst3 = random.choices(label, weights = stupid, k=450)
randomlst4 = random.choices(label, weights = stupid, k=450)
randomlst5 = random.choices(label, weights = stupid, k=450)

def compute_accuracy(lst, label_file):
    guessed_right = 0 
    with open(label_file, 'r') as f:
        correct_labels = [json.loads(line) for line in f.readlines()] #correct labels in test.json
        for i, d in enumerate(correct_labels):
            correct = d['label']
            prediction = lst[i]
            if len(correct) == len(prediction):
                guessed_right += 1
        accuracy = float(guessed_right / 450)
        return accuracy
        #print('accuracy: {:.2%}'.format(accuracy))

if __name__ == "__main__":
    label_file = '/Users/emilychen/Desktop/MPLT_Thesis/Data/experiments/mdd/mddtest.json'
    acc1 = compute_accuracy(randomlst1, label_file)
    acc2 = compute_accuracy(randomlst2, label_file)
    acc3 = compute_accuracy(randomlst3, label_file)
    acc4 = compute_accuracy(randomlst4, label_file)
    acc5 = compute_accuracy(randomlst5, label_file)
    avg = (acc1 + acc2 + acc3 + acc4 + acc5) / 5
    print('avg_accuracy: {:.2%}'.format(avg))