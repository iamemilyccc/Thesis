#compute accuracy and false positive rate
import sys
import json

def fake_positive(label_file):
    result_file = sys.argv[1]
    with open(label_file, 'r') as f:
        labels = [json.loads(line) for line in f.readlines()]
    with open(result_file, 'r') as p: 
        predictions = p.readlines()
    correct = 0
    false_positive = 0
    false_negative = 0
    s_label = 0
    s_pred = 0
    tps = 0 #true positive of label support
    fps = 0 #false positive of label support
    fns = 0 #false negative of label support
    r_label = 0
    r_pred = 0
    tpr = 0
    fpr = 0
    fnr = 0
    n_label = 0
    n_pred = 0
    tpn = 0
    fpn = 0
    fnn = 0
    for i, d in enumerate(labels):
        label = d['label']
        label = label.strip()
        prediction = ((predictions[i+1]).split('	'))[1]
        prediction = prediction.strip()
        # print(len(prediction), len(answer))
        if len(label) == 8 : #supports
            s_label += 1
            if len(prediction) == 8:
                correct += 1
                tps += 1
            elif len(prediction) == 7 or len(prediction) == 15:
                fns += 1
        elif len(label) == 7: #refutes
            r_label += 1
            if len(prediction) == 7:
                correct += 1
                tpr += 1
            elif len(prediction) == 8 or len(prediction) == 15:
                fnr += 1
        elif len(label) == 15: #NEI
            n_label += 1
            if len(prediction) == 15:
                correct +=1
                tpn += 1
            elif len(prediction) == 7 or len(prediction) == 8:
                fnn += 1
    for j, p in enumerate(predictions[1:]):
        pred = p.split('	')[1]
        pred = pred.strip()
        answer = labels[j]['label']
        answer = answer.strip()
        if len(pred) == 8: #supports
            s_pred += 1
            if len(answer) == 7 or len(answer) == 15:
                fps += 1
        elif len(pred) == 7: #refutes
            r_pred += 1
            if len(answer) == 8 or len(answer) == 15:
                fpr += 1
        elif len(pred) == 15: #NEI
            n_pred += 1
            if len(answer) == 7 or len(answer) == 8:
                fpn += 1

    accuracy = float(correct / 450)
    precision_s = tps / (tps + fps)
    precision_r = tpr / (tpr + fpr)
    precision_n = tpn / (tpn + fpn)
    recall_s = tps / (tps + fns)
    recall_r = tpr / (tpr + fnr)
    recall_n = tpn / (tpn + fnn)
    precision_average = (precision_s + precision_r + precision_n) / 3
    recall_average = (recall_s + recall_r + recall_n) / 3
    macroF1 = (2 * precision_average * recall_average) / (precision_average + recall_average)
    # print(correct)
    fps_rate = fps / s_label
    fpr_rate = fpr / r_label
    fpn_rate = fpn / n_label 
    false_positive_rate = (fps_rate + fpr_rate + fpn_rate) / 3
    print('accuracy: {:.2%}'.format(accuracy) + '\n'  + "macro F1: " + str(macroF1) + '\n' + 'false positive rate: {:.2%}'.format(false_positive_rate))
    
if __name__ == "__main__":
    label_file = '/Users/emilychen/Desktop/MPLT_Thesis/Data/experiments/pos/postest450.json'
    fake_positive(label_file)
