import json
import random

def process_and_merge_data(td_file_path, cs_file_path, output_file_paths):
    # Load the data from both GPT-generated files
    with open(td_file_path, 'r',encoding='utf-8') as file:
        td_data = json.load(file)

    with open(cs_file_path, 'r',encoding='utf-8') as file:
        cs_data = json.load(file)

    merged_data = []

    for td_entry, cs_entry in zip(td_data, cs_data):
        # Ensure the text from both entries match
        if td_entry['text'] == cs_entry['text']:
            # Extract label from the 'output' string in the textual description data
            label_str = td_entry['output'].split('\n')[-1]
            label = 0 if 'fake' in label_str else 1 if 'real' in label_str else -1  # Handling cases where label might not be found
            if label == -1:
                continue
            # Extracting and handling 'null' time values
            time_info = td_entry['input'].split('\n')[0].split(': ')[1].strip()
            if time_info == 'null':
                time_info = "Unknown Time"  # Placeholder for unknown times

            # Extracting prediction and accuracy data
            td_pred = int(td_entry['GPT_analysis_Textual_Description_answer']) if td_entry[
                'GPT_analysis_Textual_Description_answer'].isdigit() else -1
            if td_pred == -1:
                continue
            td_acc = 1 if td_pred==label else 0

            cs_pred = int(cs_entry['GPT_analysis_Commonsense_answer']) if cs_entry[
                'GPT_analysis_Commonsense_answer'].isdigit() else -1
            if cs_pred == -1:
                continue
            cs_acc = 1  if cs_pred==label else 0

            entry = {
                "content": td_entry['text'],
                "label": label,
                "time": time_info,
                "source_id": hash(td_entry['input']),  # Using hash of input as unique identifier for source_id
                "td_rationale": td_entry['output'],
                "cs_rationale": cs_entry['output'],
                "td_pred": td_pred,
                "td_acc": td_acc,
                "cs_pred": cs_pred,
                "cs_acc": cs_acc,
            }
            merged_data.append(entry)

    # Shuffle the data to ensure randomness in split
    random.shuffle(merged_data)

    # Split data according to 8:1:1 ratio
    total_len = len(merged_data)
    train_len = int(total_len * 0.8)
    val_len = int(total_len * 0.1)

    train_data = merged_data[:train_len]
    val_data = merged_data[train_len:train_len + val_len]
    test_data = merged_data[train_len + val_len:]

    # Set split field correctly
    for data in train_data:
        data['split'] = 'train'
    for data in val_data:
        data['split'] = 'val'
    for data in test_data:
        data['split'] = 'test'

    # Write the split data into different files
    with open(output_file_paths['train'], 'w',encoding='utf-8') as file:
        json.dump(train_data, file, indent=4)
    with open(output_file_paths['val'], 'w',encoding='utf-8') as file:
        json.dump(val_data, file, indent=4)
    with open(output_file_paths['test'], 'w',encoding='utf-8') as file:
        json.dump(test_data, file, indent=4)

    print("Data has been processed and split into train, val, and test datasets")

# Example usage
td_path = 'Ti-CNN_data_filtered_GPT_Textual_Description.json'
cs_path = 'Ti-CNN_data_filtered_GPT_Commonsense.json'
output_paths = {
    'train': 'train.json',
    'val': 'val.json',
    'test': 'test.json'
}
process_and_merge_data(td_path, cs_path, output_paths)